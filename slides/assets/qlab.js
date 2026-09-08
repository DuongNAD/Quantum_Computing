/* ═══════════════════════════════════════════════════════════════════════════
   QLab — phòng thí nghiệm lượng tử nhúng thẳng vào slide
   ---------------------------------------------------------------------------
   Gồm 2 tầng:
     1) Sim   — simulator state-vector viết bằng JS thuần (không thư viện ngoài).
                Dùng đúng thuật toán "pairwise indexing" mà bạn sẽ tự viết ở
                Phase 1 (NumPy) và Phase 3 (Rust) — đọc file này cũng là học.
     2) Widget — biến <div class="qlab"> trong HTML thành mạch bấm được,
                bảng biên độ, đĩa pha, Bloch sphere, và nút chạy shots.

   Cách nhúng vào slide:
     <div class="qlab" data-n="1" data-gates="H" data-title="Thử cổng H"></div>

   Thuộc tính:
     data-n      số qubit (1–4)
     data-gates  mạch nạp sẵn, cách nhau bởi dấu phẩy:  H0, X1, CX0-1, RZ0:0.5
     data-title  tiêu đề hiện trên đầu widget
     data-lock   "1" = chỉ xem, giấu bảng cổng (dùng khi minh hoạ cố định)
     data-hide   danh sách panel muốn ẩn: bloch,hist,amp,circ
     data-goal   mô tả mục tiêu bài tập, hiện dưới dạng gợi ý
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  /* ───────────────────────────────────────────────────────────────────────
     TẦNG 1 · SIMULATOR
     Trạng thái n qubit = 2^n biên độ phức. Ta giữ 2 mảng số thực song song
     (re[], im[]) thay vì mảng object {re,im} — nhanh hơn nhiều và giống hệt
     cách numpy/Rust lưu trong bộ nhớ.
     Quy ước bit: qubit 0 là bit THẤP NHẤT của chỉ số  →  giống Qiskit.
     Ví dụ n=2, chỉ số 2 = nhị phân "10" = q1=1, q0=0.
     ─────────────────────────────────────────────────────────────────────── */
  const S2 = Math.SQRT1_2;

  /* Mỗi cổng 1 qubit là ma trận 2×2 phức, viết phẳng thành 8 số:
     [a.re,a.im, b.re,b.im, c.re,c.im, d.re,d.im]  cho  [[a,b],[c,d]] */
  const G1 = {
    I:  [1,0, 0,0, 0,0, 1,0],
    X:  [0,0, 1,0, 1,0, 0,0],
    Y:  [0,0, 0,-1, 0,1, 0,0],
    Z:  [1,0, 0,0, 0,0, -1,0],
    H:  [S2,0, S2,0, S2,0, -S2,0],
    S:  [1,0, 0,0, 0,0, 0,1],
    SDG:[1,0, 0,0, 0,0, 0,-1],
    T:  [1,0, 0,0, 0,0, S2,S2],
    TDG:[1,0, 0,0, 0,0, S2,-S2],
  };

  /* Cổng có tham số góc (radian). */
  function rot(name, t) {
    const c = Math.cos(t / 2), s = Math.sin(t / 2);
    switch (name) {
      case "RX": return [c,0, 0,-s, 0,-s, c,0];
      case "RY": return [c,0, -s,0, s,0, c,0];
      case "RZ": return [Math.cos(-t/2),Math.sin(-t/2), 0,0, 0,0, Math.cos(t/2),Math.sin(t/2)];
      case "P":  return [1,0, 0,0, 0,0, Math.cos(t),Math.sin(t)];
      default:   return G1.I;
    }
  }

  function matOf(g) {
    if (G1[g.op]) return G1[g.op];
    return rot(g.op, g.arg || 0);
  }

  function newState(n) {
    const N = 1 << n;
    const st = { n: n, N: N, re: new Float64Array(N), im: new Float64Array(N) };
    st.re[0] = 1;                       // khởi tạo |00…0⟩
    return st;
  }

  function clone(st) {
    return { n: st.n, N: st.N, re: st.re.slice(), im: st.im.slice() };
  }

  /* ── Trái tim của cả simulator ──────────────────────────────────────────
     Áp ma trận 2×2 lên qubit `t`. KHÔNG dựng ma trận 2^n × 2^n.
     Ta duyệt toàn bộ chỉ số, chỉ xử lý những chỉ số có bit t = 0, rồi ghép
     nó với "người bạn song sinh" i|bit_t = 1. Mỗi cặp là một phép nhân 2×2.
     Đây chính là "pairwise indexing" — mốc 2 của Phase 1.
     ────────────────────────────────────────────────────────────────────── */
  function apply1(st, m, t, controls) {
    const bit = 1 << t;
    const cmask = (controls || []).reduce((a, c) => a | (1 << c), 0);
    for (let i = 0; i < st.N; i++) {
      if (i & bit) continue;                       // chỉ lấy nửa dưới của cặp
      if ((i & cmask) !== cmask) continue;         // control chưa đủ 1 → bỏ qua
      const j = i | bit;
      const ar = st.re[i], ai = st.im[i];
      const br = st.re[j], bi = st.im[j];
      st.re[i] = m[0]*ar - m[1]*ai + m[2]*br - m[3]*bi;
      st.im[i] = m[0]*ai + m[1]*ar + m[2]*bi + m[3]*br;
      st.re[j] = m[4]*ar - m[5]*ai + m[6]*br - m[7]*bi;
      st.im[j] = m[4]*ai + m[5]*ar + m[6]*bi + m[7]*br;
    }
  }

  function applySwap(st, a, b) {
    const ba = 1 << a, bb = 1 << b;
    for (let i = 0; i < st.N; i++) {
      if ((i & ba) && !(i & bb)) {
        const j = (i & ~ba) | bb;
        let t = st.re[i]; st.re[i] = st.re[j]; st.re[j] = t;
        t = st.im[i]; st.im[i] = st.im[j]; st.im[j] = t;
      }
    }
  }

  /* Đo qubit t và làm sập trạng thái (dùng cho cổng "M" giữa mạch). */
  function collapse(st, t, rnd) {
    const bit = 1 << t;
    let p1 = 0;
    for (let i = 0; i < st.N; i++) if (i & bit) p1 += st.re[i]*st.re[i] + st.im[i]*st.im[i];
    const got1 = (rnd === undefined ? Math.random() : rnd) < p1;
    const p = got1 ? p1 : 1 - p1;
    const norm = p > 1e-12 ? 1 / Math.sqrt(p) : 0;
    for (let i = 0; i < st.N; i++) {
      const on = (i & bit) !== 0;
      if (on === got1) { st.re[i] *= norm; st.im[i] *= norm; }
      else { st.re[i] = 0; st.im[i] = 0; }
    }
    return got1 ? 1 : 0;
  }

  function applyGate(st, g) {
    if (g.op === "SWAP") return applySwap(st, g.t, g.t2);
    if (g.op === "M")    return collapse(st, g.t);
    apply1(st, matOf(g), g.t, g.ctrl);
  }

  /* Chạy mạch tới đúng bước `upto` (mặc định: hết mạch). */
  function run(n, gates, upto) {
    const st = newState(n);
    const k = upto === undefined ? gates.length : upto;
    for (let i = 0; i < k; i++) applyGate(st, gates[i]);
    return st;
  }

  function probs(st) {
    const p = new Float64Array(st.N);
    for (let i = 0; i < st.N; i++) p[i] = st.re[i]*st.re[i] + st.im[i]*st.im[i];
    return p;
  }

  /* Lấy mẫu shots lần từ phân bố xác suất — chính là việc máy thật làm. */
  function sample(st, shots) {
    const p = probs(st), cum = new Float64Array(st.N);
    let s = 0;
    for (let i = 0; i < st.N; i++) { s += p[i]; cum[i] = s; }
    const counts = new Int32Array(st.N);
    for (let k = 0; k < shots; k++) {
      const r = Math.random() * s;
      let lo = 0, hi = st.N - 1;
      while (lo < hi) { const mid = (lo + hi) >> 1; if (cum[mid] < r) lo = mid + 1; else hi = mid; }
      counts[lo]++;
    }
    return counts;
  }

  /* Vector Bloch (x,y,z) của qubit 0 khi n = 1. */
  function bloch(st) {
    const ar = st.re[0], ai = st.im[0], br = st.re[1], bi = st.im[1];
    return {
      x: 2 * (ar * br + ai * bi),
      y: 2 * (ar * bi - ai * br),
      z: ar*ar + ai*ai - (br*br + bi*bi),
    };
  }

  /* Trạng thái n qubit có bị vướng víu không? Với n=2: kiểm tra định thức
     ma trận 2×2 [[c00,c01],[c10,c11]] — khác 0 nghĩa là không tách được. */
  function entangled2(st) {
    if (st.n !== 2) return false;
    const dr = st.re[0]*st.re[3] - st.im[0]*st.im[3] - (st.re[1]*st.re[2] - st.im[1]*st.im[2]);
    const di = st.re[0]*st.im[3] + st.im[0]*st.re[3] - (st.re[1]*st.im[2] + st.im[1]*st.re[2]);
    return Math.hypot(dr, di) > 1e-6;
  }

  const Sim = { newState, clone, apply1, applyGate, run, probs, sample, bloch, entangled2, G1, rot, collapse };

  /* ───────────────────────────────────────────────────────────────────────
     TẦNG 2 · WIDGET
     ─────────────────────────────────────────────────────────────────────── */

  const PALETTE = [
    { op: "H",  label: "H",  hint: "Hadamard — tạo chồng chập đều" },
    { op: "X",  label: "X",  hint: "NOT lượng tử — đổi chỗ α và β" },
    { op: "Y",  label: "Y",  hint: "Quay 180° quanh trục Y" },
    { op: "Z",  label: "Z",  hint: "Đổi dấu |1⟩ — xác suất không đổi" },
    { op: "S",  label: "S",  hint: "Pha 90° cho |1⟩" },
    { op: "T",  label: "T",  hint: "Pha 45° cho |1⟩" },
    { op: "RX", label: "Rx", hint: "Quay quanh X một góc tuỳ ý", arg: true },
    { op: "RY", label: "Ry", hint: "Quay quanh Y một góc tuỳ ý", arg: true },
    { op: "RZ", label: "Rz", hint: "Quay quanh Z một góc tuỳ ý", arg: true },
    { op: "CX", label: "CX", hint: "CNOT — lật target khi control = 1", two: true },
    { op: "CZ", label: "CZ", hint: "Đổi dấu khi cả hai đều 1", two: true },
    { op: "SWAP", label: "SW", hint: "Tráo hai qubit", two: true },
    { op: "M",  label: "M",  hint: "Đo giữa mạch — phá huỷ pha" },
  ];

  const FRAC = { 0: "0", 0.25: "π/4", 0.5: "π/2", 0.75: "3π/4", 1: "π", 1.5: "3π/2", 2: "2π" };

  function fmtAngle(t) {
    const u = t / Math.PI;
    const r = Math.round(u * 8) / 8;
    if (FRAC[Math.abs(r)]) return (r < 0 ? "−" : "") + FRAC[Math.abs(r)];
    return u.toFixed(2) + "π";
  }

  function fmtC(re, im) {
    const r = Math.abs(re) < 1e-9 ? 0 : re;
    const i = Math.abs(im) < 1e-9 ? 0 : im;
    if (i === 0) return r.toFixed(3);
    if (r === 0) return (i < 0 ? "−" : "") + Math.abs(i).toFixed(3) + "i";
    return r.toFixed(3) + (i < 0 ? " − " : " + ") + Math.abs(i).toFixed(3) + "i";
  }

  function bits(i, n) {
    let s = "";
    for (let k = n - 1; k >= 0; k--) s += (i >> k) & 1;
    return s;
  }

  function el(tag, cls, html) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  /* Chuỗi mạch  "H0, CX0-1, RZ1:0.5"  →  danh sách cổng */
  function parseGates(str) {
    if (!str) return [];
    return str.split(",").map(function (tok) {
      tok = tok.trim();
      if (!tok) return null;
      const m = /^([A-Za-z]+)(\d)(?:-(\d))?(?::(-?[\d.]+))?$/.exec(tok);
      if (!m) return null;
      const op = m[1].toUpperCase();
      const a = +m[2], b = m[3] === undefined ? null : +m[3];
      const arg = m[4] === undefined ? undefined : parseFloat(m[4]) * Math.PI;
      if (op === "CX") return { op: "X", t: b, ctrl: [a] };
      if (op === "CZ") return { op: "Z", t: b, ctrl: [a] };
      if (op === "SWAP") return { op: "SWAP", t: a, t2: b };
      return { op: op, t: a, arg: arg };
    }).filter(Boolean);
  }

  function gateLabel(g) {
    if (g.op === "SWAP") return "×";
    if (g.op === "M") return "M";
    const base = { RX: "Rx", RY: "Ry", RZ: "Rz", P: "P", SDG: "S†", TDG: "T†" }[g.op] || g.op;
    if (g.arg !== undefined && g.arg !== null) return base;
    return base;
  }

  /* ── vẽ mạch ────────────────────────────────────────────────────────── */
  function renderCirc(box, W) {
    const n = W.n, gates = W.gates;
    box.innerHTML = "";
    const grid = el("div", "ql-circ");
    grid.style.gridTemplateColumns = "3rem repeat(" + Math.max(gates.length, 1) + ", 46px) 1fr";

    for (let q = 0; q < n; q++) {
      const lbl = el("span", "ql-wlbl", "q<sub>" + q + "</sub>");
      lbl.style.gridRow = q + 1;
      lbl.style.gridColumn = 1;
      grid.appendChild(lbl);
      const line = el("span", "ql-wire");
      line.style.gridRow = q + 1;
      line.style.gridColumn = "2 / -1";
      grid.appendChild(line);
    }

    gates.forEach(function (g, k) {
      const col = k + 2;
      const dim = W.step !== null && k >= W.step;
      const targets = g.op === "SWAP" ? [g.t, g.t2] : [g.t];
      const ctrls = g.ctrl || [];

      /* dây nối dọc giữa control và target */
      if (ctrls.length || g.op === "SWAP") {
        const all = targets.concat(ctrls);
        const lo = Math.min.apply(null, all), hi = Math.max.apply(null, all);
        if (hi > lo) {
          const link = el("span", "ql-link" + (dim ? " dim" : ""));
          link.style.gridColumn = col;
          link.style.gridRow = (lo + 1) + " / " + (hi + 2);
          grid.appendChild(link);
        }
      }

      ctrls.forEach(function (c) {
        const d = el("span", "ql-ctrl" + (dim ? " dim" : ""), "<b></b>");
        d.style.gridRow = c + 1; d.style.gridColumn = col;
        grid.appendChild(d);
      });

      targets.forEach(function (t) {
        let cls = "ql-g";
        if (g.op === "M") cls += " meas";
        if (ctrls.length && g.op === "X") cls += " targ";
        if (g.op === "SWAP") cls += " swap";
        if (dim) cls += " dim";
        const b = el("button", cls, g.op === "SWAP" ? "×" : (ctrls.length && g.op === "X" ? "⊕" : gateLabel(g)));
        b.type = "button";
        b.title = "Bấm để xoá cổng này" + (g.arg !== undefined ? " · góc " + fmtAngle(g.arg) : "");
        if (g.arg !== undefined && g.arg !== null && g.op !== "M") {
          b.appendChild(el("i", "ql-arg", fmtAngle(g.arg)));
        }
        b.style.gridRow = t + 1; b.style.gridColumn = col;
        if (!W.lock) b.addEventListener("click", function () { W.removeAt(k); });
        grid.appendChild(b);
      });
    });

    box.appendChild(grid);
  }

  /* ── bảng biên độ ───────────────────────────────────────────────────── */
  function renderAmp(box, W, st, p) {
    box.innerHTML = "";
    const head = el("div", "ql-amp-head",
      "<span>cơ sở</span><span>biên độ α (số phức)</span><span>pha</span><span>xác suất</span>");
    box.appendChild(head);
    for (let i = 0; i < st.N; i++) {
      const pr = p[i];
      const row = el("div", "ql-amp-row" + (pr < 1e-9 ? " zero" : ""));
      const ph = Math.atan2(st.im[i], st.re[i]);
      const dial = pr < 1e-9 ? '<span class="ql-dial off"></span>'
        : '<span class="ql-dial" style="--a:' + (ph * 180 / Math.PI).toFixed(1) + 'deg"><i></i></span>';
      row.innerHTML =
        '<span class="ql-ket">|' + bits(i, st.n) + "⟩</span>" +
        '<span class="ql-c">' + fmtC(st.re[i], st.im[i]) + "</span>" +
        '<span class="ql-ph">' + dial + "</span>" +
        '<span class="ql-p"><span class="ql-ptrack"><i style="width:' + (pr * 100).toFixed(2) + '%"></i></span>' +
        '<b>' + (pr * 100).toFixed(1) + "%</b></span>";
      box.appendChild(row);
    }
  }

  /* ── Bloch sphere (SVG, chỉ khi n = 1) ──────────────────────────────── */
  function renderBloch(box, st) {
    const v = bloch(st);
    const R = 68, cx = 88, cy = 88;
    /* chiếu đẳng cự: nhìn từ hướng (1, -1, 0.6) cho dễ đọc cả 3 trục */
    const px = function (x, y, z) { return [cx + (x * 0.87 - y * 0.5) * R, cy - (z - (x * 0.29 + y * 0.5) * 0.42) * R]; };
    const tip = px(v.x, v.y, v.z);
    const axis = function (x, y, z, lab, col) {
      const a = px(-x, -y, -z), b = px(x, y, z);
      return '<line x1="' + a[0].toFixed(1) + '" y1="' + a[1].toFixed(1) + '" x2="' + b[0].toFixed(1) +
        '" y2="' + b[1].toFixed(1) + '" stroke="' + col + '" stroke-width="1" stroke-dasharray="3 3"/>' +
        '<text x="' + (b[0] + 4).toFixed(1) + '" y="' + (b[1] - 3).toFixed(1) + '" fill="' + col +
        '" font-size="10">' + lab + "</text>";
    };
    box.innerHTML =
      '<svg viewBox="0 0 176 176" class="ql-bloch-svg">' +
      '<ellipse cx="88" cy="88" rx="' + R + '" ry="' + R + '" fill="rgba(94,234,212,.045)" stroke="rgba(255,255,255,.14)"/>' +
      '<ellipse cx="88" cy="88" rx="' + R + '" ry="' + (R * 0.34).toFixed(1) + '" fill="none" stroke="rgba(255,255,255,.10)"/>' +
      axis(1, 0, 0, "x", "#6f7a92") + axis(0, 1, 0, "y", "#6f7a92") + axis(0, 0, 1, "z", "#6f7a92") +
      '<text x="88" y="14" fill="#5eead4" font-size="11" text-anchor="middle">|0⟩</text>' +
      '<text x="88" y="172" fill="#c4a2ff" font-size="11" text-anchor="middle">|1⟩</text>' +
      '<line x1="88" y1="88" x2="' + tip[0].toFixed(1) + '" y2="' + tip[1].toFixed(1) +
      '" stroke="#5eead4" stroke-width="2.4" stroke-linecap="round"/>' +
      '<circle cx="' + tip[0].toFixed(1) + '" cy="' + tip[1].toFixed(1) + '" r="4.5" fill="#5eead4"/>' +
      "</svg>" +
      '<div class="ql-blabel">x <b>' + v.x.toFixed(2) + "</b> · y <b>" + v.y.toFixed(2) +
      "</b> · z <b>" + v.z.toFixed(2) + "</b></div>";
  }

  /* ── histogram shots ────────────────────────────────────────────────── */
  function renderHist(box, W, st) {
    const counts = sample(st, W.shots);
    const n = st.n;
    box.innerHTML = "";
    const head = el("div", "ql-hist-head",
      "<span>Kết quả " + W.shots + " lần đo</span>");
    box.appendChild(head);
    const wrap = el("div", "ql-hist-bars");
    let max = 1;
    for (let i = 0; i < counts.length; i++) max = Math.max(max, counts[i]);
    for (let i = 0; i < counts.length; i++) {
      const b = el("div", "ql-hb" + (counts[i] === 0 ? " zero" : ""));
      b.innerHTML = '<span class="k">|' + bits(i, n) + "⟩</span>" +
        '<span class="tr"><i style="width:' + (counts[i] / max * 100).toFixed(1) + '%"></i></span>' +
        '<span class="v">' + counts[i] + "</span>";
      wrap.appendChild(b);
    }
    box.appendChild(wrap);
  }

  /* ── mã Qiskit tương ứng, để nối slide với việc gõ code thật ────────── */
  function qiskitCode(W) {
    const L = ["from qiskit import QuantumCircuit", "", "qc = QuantumCircuit(" + W.n + ")"];
    W.gates.forEach(function (g) {
      const a = g.arg !== undefined && g.arg !== null ? (g.arg / Math.PI).toFixed(3) + "*np.pi, " : "";
      if (g.op === "SWAP") L.push("qc.swap(" + g.t + ", " + g.t2 + ")");
      else if (g.op === "M") L.push("qc.measure_all()   # đo giữa mạch");
      else if (g.ctrl && g.ctrl.length) L.push("qc." + (g.op === "X" ? "cx" : "cz") + "(" + g.ctrl[0] + ", " + g.t + ")");
      else L.push("qc." + g.op.toLowerCase() + "(" + a + g.t + ")");
    });
    L.push("qc.measure_all()");
    return L.join("\n");
  }

  /* ── widget chính ───────────────────────────────────────────────────── */
  function build(root) {
    const W = {
      n: Math.min(4, Math.max(1, +(root.dataset.n || 1))),
      gates: parseGates(root.dataset.gates),
      lock: root.dataset.lock === "1",
      hide: (root.dataset.hide || "").split(",").map(function (s) { return s.trim(); }),
      shots: +(root.dataset.shots || 1024),
      step: null,          // null = chạy hết mạch; số = dừng trước cổng thứ k
      target: 0,
      target2: (root.dataset.n && +root.dataset.n > 1) ? 1 : 0,
      angle: Math.PI / 2,
    };
    root._qlab = W;
    const initial = W.gates.slice();
    const show = function (k) { return W.hide.indexOf(k) === -1; };

    root.innerHTML = "";
    root.classList.add("qlab-ready");

    /* đầu widget */
    const head = el("div", "ql-head");
    head.innerHTML =
      '<span class="ql-tag">Thử ngay</span>' +
      '<span class="ql-title">' + (root.dataset.title || "Mạch tương tác") + "</span>";
    const tools = el("div", "ql-tools");
    head.appendChild(tools);
    root.appendChild(head);

    if (root.dataset.goal) root.appendChild(el("p", "ql-goal", "🎯 " + root.dataset.goal));

    const circBox = el("div", "ql-circ-box");
    root.appendChild(circBox);

    /* thanh bước: xem trạng thái sau từng cổng */
    const stepBar = el("div", "ql-steps");
    root.appendChild(stepBar);

    /* bảng cổng */
    let pal = null;
    if (!W.lock) {
      pal = el("div", "ql-pal");
      root.appendChild(pal);
    }

    const body = el("div", "ql-body");
    root.appendChild(body);

    const ampBox = show("amp") ? el("div", "ql-amp") : null;
    const sideBox = el("div", "ql-side");
    if (ampBox) body.appendChild(ampBox);
    body.appendChild(sideBox);

    const blochBox = (W.n === 1 && show("bloch")) ? el("div", "ql-bloch") : null;
    if (blochBox) sideBox.appendChild(blochBox);
    const histBox = show("hist") ? el("div", "ql-hist") : null;
    if (histBox) sideBox.appendChild(histBox);

    const readout = el("div", "ql-readout");
    root.appendChild(readout);

    const codeWrap = el("details", "ql-code");
    codeWrap.innerHTML = "<summary>Mạch này viết bằng Qiskit thì trông thế nào?</summary>";
    const codePre = el("pre", "code");
    codePre.dataset.lang = "python";
    codeWrap.appendChild(codePre);
    root.appendChild(codeWrap);

    /* ── thao tác ─────────────────────────────────────────────────────── */
    W.add = function (op, arg) {
      if (W.gates.length >= 12) return;
      const two = op === "CX" || op === "CZ" || op === "SWAP";
      if (two && W.n < 2) return;
      let g;
      if (two) {
        const a = W.target;
        let b = (W.target2 !== undefined && W.target2 !== a) ? W.target2 : ((a + 1) % W.n);
        g = op === "SWAP" ? { op: "SWAP", t: a, t2: b }
          : { op: op === "CX" ? "X" : "Z", t: b, ctrl: [a] };
      } else {
        g = { op: op, t: W.target };
        if (arg) g.arg = W.angle;
      }
      W.gates.push(g);
      W.step = null;
      draw();
    };
    W.loadGates = function (strOrArray) {
      W.gates = typeof strOrArray === "string" ? parseGates(strOrArray) : strOrArray.slice();
      W.step = null;
      draw();
    };
    W.removeAt = function (k) { W.gates.splice(k, 1); W.step = null; draw(); };
    W.reset = function () { W.gates = initial.slice(); W.step = null; draw(); };
    W.clear = function () { W.gates = []; W.step = null; draw(); };

    /* ── thanh công cụ ────────────────────────────────────────────────── */
    if (!W.lock) {
      const bReset = el("button", "ql-btn", "↺ về mạch gốc");
      bReset.type = "button";
      bReset.addEventListener("click", W.reset);
      const bClear = el("button", "ql-btn", "✕ xoá hết");
      bClear.type = "button";
      bClear.addEventListener("click", W.clear);
      tools.appendChild(bReset);
      tools.appendChild(bClear);
    }
    if (histBox) {
      const bRun = el("button", "ql-btn primary", "▶ đo " + W.shots + " lần");
      bRun.type = "button";
      bRun.addEventListener("click", function () { renderHist(histBox, W, currentState()); });
      tools.appendChild(bRun);
    }

    /* ── dựng bảng cổng ───────────────────────────────────────────────── */
    if (pal) {
      const qsel = el("div", "ql-qsel");
      qsel.appendChild(el("span", "ql-plabel", W.n >= 2 ? "qubit (ctrl):" : "đặt lên:"));
      const qbtns1 = [];
      const qbtns2 = [];

      function updateQBtns() {
        qbtns1.forEach((b, q) => {
          b.classList.toggle("on", q === W.target);
        });
        qbtns2.forEach((b, q) => {
          b.classList.toggle("on", q === W.target2);
          b.classList.toggle("dim", q === W.target);
          b.disabled = (q === W.target);
        });
        pal.querySelectorAll(".ql-pbtn.two").forEach(b => {
          const op = b.dataset.op || b.textContent.trim();
          const t2 = (W.target2 !== undefined && W.target2 !== W.target) ? W.target2 : ((W.target + 1) % W.n);
          if (op === "CX") {
            b.title = `CNOT: control q${W.target} → target q${t2}`;
          } else if (op === "CZ") {
            b.title = `CZ: q${W.target} và q${t2}`;
          } else if (op === "SWAP") {
            b.title = `SWAP: tráo q${W.target} ↔ q${t2}`;
          }
        });
      }

      for (let q = 0; q < W.n; q++) {
        const b = el("button", "ql-qbtn" + (q === W.target ? " on" : ""), "q" + q);
        b.type = "button";
        b.dataset.q = q;
        b.addEventListener("click", function () {
          W.target = +this.dataset.q;
          if (W.target === W.target2) {
            W.target2 = (W.target + 1) % W.n;
          }
          updateQBtns();
        });
        qbtns1.push(b);
        qsel.appendChild(b);
      }
      pal.appendChild(qsel);

      if (W.n >= 2) {
        const qsel2 = el("div", "ql-qsel");
        qsel2.appendChild(el("span", "ql-plabel", "đích (CX/CZ/SW):"));
        for (let q = 0; q < W.n; q++) {
          const b = el("button", "ql-qbtn" + (q === W.target2 ? " on" : "") + (q === W.target ? " dim" : ""), "q" + q);
          b.type = "button";
          b.dataset.q = q;
          if (q === W.target) b.disabled = true;
          b.addEventListener("click", function () {
            if (+this.dataset.q !== W.target) {
              W.target2 = +this.dataset.q;
              updateQBtns();
            }
          });
          qbtns2.push(b);
          qsel2.appendChild(b);
        }
        pal.appendChild(qsel2);
      }

      const gwrap = el("div", "ql-gates");
      PALETTE.forEach(function (P) {
        if (P.two && W.n < 2) return;
        const b = el("button", "ql-pbtn" + (P.two ? " two" : "") + (P.op === "M" ? " meas" : ""), P.label);
        b.type = "button";
        b.dataset.op = P.op;
        b.title = P.hint;
        b.addEventListener("click", function () { W.add(P.op, P.arg); });
        gwrap.appendChild(b);
      });
      pal.appendChild(gwrap);

      const ang = el("div", "ql-ang");
      ang.innerHTML = '<span class="ql-plabel">góc cho Rx/Ry/Rz</span>';
      const sl = el("input", "ql-slider");
      sl.type = "range"; sl.min = "0"; sl.max = "2"; sl.step = "0.125"; sl.value = "0.5";
      const av = el("span", "ql-angv", "π/2");
      sl.addEventListener("input", function () {
        W.angle = parseFloat(sl.value) * Math.PI;
        av.textContent = fmtAngle(W.angle);
      });
      ang.appendChild(sl); ang.appendChild(av);
      pal.appendChild(ang);
      updateQBtns();
    }

    function currentState() { return run(W.n, W.gates, W.step === null ? undefined : W.step); }

    /* ── vẽ lại toàn bộ ───────────────────────────────────────────────── */
    function draw() {
      renderCirc(circBox, W);

      /* thanh bước */
      stepBar.innerHTML = "";
      if (W.gates.length) {
        stepBar.appendChild(el("span", "ql-plabel", "xem trạng thái sau bước"));
        for (let k = 0; k <= W.gates.length; k++) {
          const on = (W.step === null ? W.gates.length : W.step) === k;
          const b = el("button", "ql-sbtn" + (on ? " on" : ""), k === 0 ? "đầu" : String(k));
          b.type = "button";
          b.dataset.k = k;
          b.addEventListener("click", function () {
            W.step = (+this.dataset.k === W.gates.length) ? null : +this.dataset.k;
            draw();
          });
          stepBar.appendChild(b);
        }
      }

      const st = currentState();
      const p = probs(st);
      if (ampBox) renderAmp(ampBox, W, st, p);
      if (blochBox) renderBloch(blochBox, st);

      /* dòng đọc hiểu — giải thích trạng thái bằng tiếng Việt */
      const nz = [];
      for (let i = 0; i < st.N; i++) if (p[i] > 1e-9) nz.push(i);
      let msg;
      if (nz.length === 1) {
        msg = "Trạng thái <b>xác định</b>: đo bao nhiêu lần cũng ra <span class='ql-ket'>|" +
          bits(nz[0], st.n) + "⟩</span>.";
      } else {
        const even = nz.every(function (i) { return Math.abs(p[i] - p[nz[0]]) < 1e-6; });
        msg = "Chồng chập của <b>" + nz.length + "</b> trạng thái cơ sở" +
          (even ? ", xác suất <b>chia đều</b>" : ", xác suất <b>không đều</b>") + ".";
      }
      if (st.n === 2 && entangled2(st)) {
        msg += " Hai qubit đang <b class='ql-ent'>vướng víu</b> — không tách rời được thành hai qubit độc lập.";
      }
      /* Chỉ pha TƯƠNG ĐỐI mới có ý nghĩa vật lý. Pha toàn cục (mọi biên độ
         cùng quay một góc) không quan sát được bằng bất kỳ phép đo nào. */
      if (nz.length > 1) {
        const ph0 = Math.atan2(st.im[nz[0]], st.re[nz[0]]);
        const relPhase = nz.some(function (i) {
          let d = Math.atan2(st.im[i], st.re[i]) - ph0;
          while (d > Math.PI) d -= 2 * Math.PI;
          while (d < -Math.PI) d += 2 * Math.PI;
          return Math.abs(d) > 1e-6;
        });
        if (relPhase) msg += " Các nhánh có <b>pha lệch nhau</b> — phép đo không thấy, nhưng cổng tiếp theo sẽ biến nó thành kết quả đo được.";
      } else if (nz.length === 1 && Math.abs(Math.atan2(st.im[nz[0]], st.re[nz[0]])) > 1e-6) {
        msg += " (Biên độ đang mang một <b>pha toàn cục</b> — không quan sát được, bỏ qua nó.)";
      }
      readout.innerHTML = msg;

      codePre.dataset.painted = "";
      codePre.textContent = qiskitCode(W);
      if (window.QZH && window.QZH.paintCode) window.QZH.paintCode();
    }

    draw();
    if (histBox) renderHist(histBox, W, currentState());
  }

  function init(scope) {
    (scope || document).querySelectorAll(".qlab:not(.qlab-ready)").forEach(build);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { init(); });
  else init();

  window.QLab = {
    Sim: Sim,
    init: init,
    parseGates: parseGates,
    getWidget: function (el) { return el ? el._qlab : null; },
    getGates: function (el) { return el && el._qlab ? el._qlab.gates : []; },
    loadGates: function (el, gates) { if (el && el._qlab) el._qlab.loadGates(gates); }
  };
})();
