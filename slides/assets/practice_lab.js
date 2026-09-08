/* ═══════════════════════════════════════════════════════════════════════════
   Quantum Zero→Hero · Practice Laboratory & Interactive Explorer Engine
   Phòng luyện tập & khám phá trực quan lượng tử tương tác:
     1) 12 Thử thách mạch lượng tử (Mini-Katas trực quan với tự chấm điểm)
     2) Quả cầu Bloch 3D / Isometric tương tác động
     3) Bàn thí nghiệm Ghép cặp biên độ (Pairwise Indexing - Phase 1 & 3)
     4) Vòng xoay không gian Grover & Khuếch đại biên độ (Phase 2)
     5) Phòng thí nghiệm Mã sửa lỗi lượng tử (QEC Bit-Flip & Syndrome - Phase 4)
     6) Trò chơi bất đẳng thức Bell CHSH (Bell Violation Game - Phase 4)
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  // ── Web Audio Synthesizer ───────────────────────────────────────────────
  let audioCtx = null;
  function sound(freq = 440, type = 'sine', duration = 0.09) {
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = type;
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    } catch (e) {}
  }

  function soundSuccess() {
    sound(523.25, 'triangle', 0.12);
    setTimeout(() => sound(659.25, 'triangle', 0.12), 100);
    setTimeout(() => sound(783.99, 'triangle', 0.15), 200);
    setTimeout(() => sound(1046.50, 'sine', 0.25), 320);
  }

  function soundFail() {
    sound(320, 'sawtooth', 0.1);
    setTimeout(() => sound(240, 'sawtooth', 0.2), 120);
  }

  // ── State Fidelity Calculator ───────────────────────────────────────────
  // Tính độ tương đồng lượng tử (quantum state fidelity F = |<ψ|φ>|^2)
  // cho hai vector trạng thái độ dài N. Bỏ qua pha toàn cục e^(iγ).
  function computeFidelity(stA, stB) {
    if (stA.N !== stB.N) return 0;
    let dotR = 0, dotI = 0;
    for (let i = 0; i < stA.N; i++) {
      dotR += stA.re[i] * stB.re[i] + stA.im[i] * stB.im[i];
      dotI += stA.re[i] * stB.im[i] - stA.im[i] * stB.re[i];
    }
    return dotR * dotR + dotI * dotI;
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 1: 12 INTERACTIVE CHALLENGES (MINI-KATAS)
  // ═════════════════════════════════════════════════════════════════════════
  const S2 = Math.SQRT1_2;

  function makeTargetState(n, entries) {
    const N = 1 << n;
    const st = { n: n, N: N, re: new Float64Array(N), im: new Float64Array(N) };
    for (let k = 0; k < entries.length; k++) {
      const idx = entries[k][0];
      st.re[idx] = entries[k][1];
      if (entries[k][2] !== undefined) st.im[idx] = entries[k][2];
    }
    return st;
  }

  function gateToString(g) {
    if (!g) return "";
    if (g.op === "SWAP") return `SWAP${g.t}-${g.t2}`;
    if (g.ctrl && g.ctrl.length > 0) {
      const c = g.ctrl[0];
      if (g.op === "X") return `CX${c}-${g.t}`;
      if (g.op === "Z") return `CZ${c}-${g.t}`;
      return `C${g.op}${c}-${g.t}`;
    }
    return `${g.op}${g.t}` + (g.arg !== undefined ? `:${(g.arg / Math.PI).toFixed(4)}` : "");
  }

  const CHALLENGES = [
    {
      id: 1,
      title: "Chồng Chập Cơ Bản (Superposition)",
      level: "Cơ bản",
      qubits: 1,
      presetGates: "",
      targetDesc: "|+⟩ = (|0⟩ + |1⟩) / √2",
      expected: () => makeTargetState(1, [[0, S2], [1, S2]]),
      desc: "Từ trạng thái ban đầu |0⟩, hãy áp cổng phù hợp để tạo ra trạng thái chồng chập đều |+⟩ (50% cơ hội đo ra 0 và 50% cơ hội đo ra 1).",
      hints: [
        "Cổng nào biến |0⟩ thành (|0⟩+|1⟩)/√2?",
        "Hãy thử dùng cổng Hadamard (H) lên qubit 0.",
        "Lời giải: Chỉ cần đặt 1 cổng H lên q0."
      ],
      solution: "H0",
      explain: "Cổng Hadamard (H) biến trạng thái cơ sở tính toán (|0⟩ hoặc |1⟩) thành trạng thái chồng chập (|+⟩ hoặc |−⟩). Đây là cổng khởi đầu cho hầu hết mọi thuật toán lượng tử!"
    },
    {
      id: 2,
      title: "Đảo Pha Tạo Trạng Thái |−⟩",
      level: "Cơ bản",
      qubits: 1,
      presetGates: "",
      targetDesc: "|−⟩ = (|0⟩ − |1⟩) / √2",
      expected: () => makeTargetState(1, [[0, S2], [1, -S2]]),
      desc: "Tạo trạng thái |−⟩ từ |0⟩. Trạng thái này có cùng xác suất đo 50/50 như |+⟩ nhưng mang pha âm (−) ở nhánh |1⟩.",
      hints: [
        "Cách 1: Lật |0⟩ thành |1⟩ trước bằng X0, rồi mới áp Hadamard H0.",
        "Cách 2: Áp Hadamard H0 để được |+⟩, rồi áp cổng lật pha Z0.",
        "Lời giải: X0, H0 hoặc H0, Z0."
      ],
      solution: "X0, H0",
      explain: "X biến |0⟩ thành |1⟩, sau đó H biến |1⟩ thành (|0⟩−|1⟩)/√2 = |−⟩. Dấu trừ này tuy mắt thường và phép đo cơ sở Z không thấy được, nhưng nó là chìa khóa của giao thoa lượng tử!"
    },
    {
      id: 3,
      title: "Cặp Bell Chuẩn |Φ⁺⟩",
      level: "Trung cấp",
      qubits: 2,
      presetGates: "",
      targetDesc: "|Φ⁺⟩ = (|00⟩ + |11⟩) / √2",
      expected: () => makeTargetState(2, [[0, S2], [3, S2]]),
      desc: "Tạo trạng thái vướng víu tối đa nổi tiếng nhất của hai qubit: Bell state |Φ⁺⟩. Khi đo, hai qubit luôn luôn cho cùng một kết quả (00 hoặc 11).",
      hints: [
        "Bước 1: Tạo chồng chập trên qubit 0.",
        "Bước 2: Vướng víu qubit 0 sang qubit 1 bằng một cổng 2-qubit có điều khiển.",
        "Lời giải: H0, rồi CX0-1 (CNOT control=q0, target=q1)."
      ],
      solution: "H0, CX0-1",
      explain: "H0 đưa q0 vào chồng chập (|0⟩+|1⟩)/√2. CNOT lấy q0 làm điều khiển: nếu q0=|0⟩ thì q1 giữ 0; nếu q0=|1⟩ thì q1 bị lật thành 1. Kết quả là (|00⟩+|11⟩)/√2 — hai qubit đã hòa thành một!"
    },
    {
      id: 4,
      title: "Cặp Bell Đối Pha |Φ⁻⟩",
      level: "Trung cấp",
      qubits: 2,
      presetGates: "",
      targetDesc: "|Φ⁻⟩ = (|00⟩ − |11⟩) / √2",
      expected: () => makeTargetState(2, [[0, S2], [3, -S2]]),
      desc: "Tạo trạng thái Bell |Φ⁻⟩ = (|00⟩ − |11⟩)/√2. Hai qubit vẫn vướng víu 100%, nhưng nhánh |11⟩ mang pha âm.",
      hints: [
        "Bắt đầu từ |Φ⁺⟩ (H0, CX0-1), bạn cần cổng nào để đổi dấu nhánh |11⟩?",
        "Cổng Z lên q0 sẽ đổi dấu nhánh có q0=1 (chính là |11⟩)!",
        "Lời giải: H0, CX0-1, Z0."
      ],
      solution: "H0, CX0-1, Z0",
      explain: "Sau khi tạo |Φ⁺⟩, đặt Z lên q0 sẽ nhân −1 vào mọi thành phần có q0=1, biến |11⟩ thành −|11⟩ mà không ảnh hưởng tới |00⟩. Ta thu được |Φ⁻⟩!"
    },
    {
      id: 5,
      title: "Cặp Singlet Vướng Víu |Ψ⁻⟩",
      level: "Trung cấp",
      qubits: 2,
      presetGates: "",
      targetDesc: "|Ψ⁻⟩ = (|01⟩ − |10⟩) / √2",
      expected: () => makeTargetState(2, [[1, S2], [2, -S2]]),
      desc: "Tạo trạng thái Singlet |Ψ⁻⟩ = (|01⟩ − |10⟩)/√2. Đây là trạng thái phản tương quan hoàn toàn: nếu An đo ra 0 thì Bình chắc chắn đo ra 1 và ngược lại!",
      hints: [
        "Bước 1: Tạo Bell đối pha |Φ⁻⟩ bằng H0, CX0-1, Z0.",
        "Bước 2: Áp cổng X lên qubit 0 (X0) để lật nhánh 00 thành 01 và nhánh 11 thành 10!",
        "Lời giải: H0, CX0-1, Z0, X0."
      ],
      solution: "H0, CX0-1, Z0, X0",
      explain: "Trạng thái Singlet là trạng thái đối xứng quay duy nhất trong cơ học lượng tử — bất biến dưới phép quay cùng góc trên cả hai qubit! Đây là trạng thái được John Bell dùng trong chứng minh định lý Bell."
    },
    {
      id: 6,
      title: "Hiện Tượng Phase Kickback Kỳ Diệu",
      level: "Nâng cao",
      qubits: 2,
      presetGates: "",
      targetDesc: "|1-⟩ (q0=1, q1=|−⟩)",
      expected: () => makeTargetState(2, [[1, S2], [3, -S2]]),
      desc: "Thiết lập mạch Kickback: Đưa q0 vào |+⟩, q1 vào |−⟩, sau đó áp CX(control=q0, target=q1), rồi áp H lên q0. Chứng minh rằng cổng CNOT làm 'đá ngược' pha lên qubit điều khiển khiến q0 sụp đổ thành |1⟩!",
      hints: [
        "1. Chuẩn bị q0 ở |+⟩ bằng H0.",
        "2. Chuẩn bị q1 ở |−⟩ bằng X1, H1.",
        "3. Áp CNOT từ q0 sang q1: CX0-1.",
        "4. Đọc pha trên q0 bằng H0.",
        "Lời giải: H0, X1, H1, CX0-1, H0."
      ],
      solution: "H0, X1, H1, CX0-1, H0",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const hasCX = gStrs.includes("CX0-1");
        const h0Count = gStrs.filter(s => s === "H0").length;
        if (!hasCX || h0Count < 2) {
          return {
            valid: false,
            message: "Thử thách yêu cầu thiết lập mạch Phase Kickback hoàn chỉnh (chuẩn bị |+⟩ với H0, áp cổng có điều khiển CX0-1, và đo giao thoa pha bằng H0)!"
          };
        }
        return { valid: true };
      },
      explain: "Vì target ở |−⟩ là trạng thái riêng của cổng X với trị riêng −1, CNOT |x⟩|−⟩ = (−1)ˣ |x⟩|−⟩. Dấu −1 bị đá ngược về nhánh control x=1! Khi áp H cuối lên q0, nhánh |+⟩ đã biến thành |−⟩ và được H chuyển thành |1⟩ xác định 100%!"
    },
    {
      id: 7,
      title: "Giao Thoa Triệt Tiêu (H·H = I)",
      level: "Cơ bản",
      qubits: 1,
      presetGates: "",
      targetDesc: "|0⟩ (xác suất 100% về |0⟩)",
      expected: () => makeTargetState(1, [[0, 1]]),
      desc: "Từ trạng thái ban đầu |0⟩, hãy áp 2 cổng Hadamard liên tiếp lên qubit 0: H·H. Quan sát xem vì sao từ trạng thái 50/50 ngẫu nhiên, áp H lần thứ hai lại triệt tiêu hoàn toàn nhánh |1⟩ và phục hồi 100% |0⟩!",
      hints: [
        "Chỉ cần áp 2 cổng H liên tiếp lên q0.",
        "Quan sát bảng biên độ sau bước 1 và bước 2.",
        "Lời giải: H0, H0."
      ],
      solution: "H0, H0",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const h0Count = gStrs.filter(s => s === "H0").length;
        if (h0Count < 2) {
          return {
            valid: false,
            message: "Thử thách yêu cầu áp dụng ít nhất 2 cổng Hadamard liên tiếp trên qubit 0 (H0, H0) để quan sát hiện tượng giao thoa triệt tiêu!"
          };
        }
        return { valid: true };
      },
      explain: "H|0⟩ = (|0⟩+|1⟩)/√2. Áp H lần nữa: H(|0⟩) + H(|1⟩) = (|0⟩+|1⟩ + |0⟩−|1⟩)/2 = 2|0⟩/2 = |0⟩. Hai nhánh dẫn tới |1⟩ có biên độ (+1/2) và (−1/2) ngược pha nhau, tự triệt tiêu (giao thoa huỷ diệt)!"
    },
    {
      id: 8,
      title: "Chế Tạo Cổng SWAP Từ 3 CNOT",
      level: "Nâng cao",
      qubits: 2,
      presetGates: "X0",
      targetDesc: "SWAP(q0, q1) khi đầu vào q0=1, q1=0 -> q0=0, q1=1 (|10⟩)",
      expected: () => makeTargetState(2, [[2, 1]]),
      desc: "Mạch đã có sẵn X0 (q0=1, q1=0). Hãy dùng đúng 3 cổng CNOT đan xen để hoán đổi hoàn toàn trạng thái giữa q0 và q1 thành |10⟩ (q1=1, q0=0)!",
      hints: [
        "Mạch đã bắt đầu với X0 ở đầu.",
        "Quy tắc 3 CNOT hoán đổi: CX0-1, CX1-0, CX0-1.",
        "Lời giải: X0, CX0-1, CX1-0, CX0-1."
      ],
      solution: "X0, CX0-1, CX1-0, CX0-1",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        if (gStrs.length === 0 || gStrs[0] !== "X0") {
          return {
            valid: false,
            message: "Thử thách yêu cầu giữ nguyên cổng khởi tạo X0 ở đầu mạch!"
          };
        }
        const afterPreset = gStrs.slice(1);
        if (afterPreset.length < 3) {
          return {
            valid: false,
            message: "Thử thách yêu cầu thêm đúng 3 cổng CNOT đan xen (CX0-1, CX1-0, CX0-1) sau X0 để thực hiện phép tráo SWAP!"
          };
        }
        const is3Cnot = afterPreset.length === 3 &&
          afterPreset[0] === "CX0-1" &&
          afterPreset[1] === "CX1-0" &&
          afterPreset[2] === "CX0-1";
        if (!is3Cnot) {
          return {
            valid: false,
            message: "Thử thách yêu cầu dùng đúng 3 cổng CNOT đan xen (CX0-1, CX1-0, CX0-1) sau X0 để thực hiện phép tráo SWAP!"
          };
        }
        return { valid: true };
      },
      explain: "Mẹo kinh điển: a = a ⊕ b; b = b ⊕ a; a = a ⊕ b. Ba phép XOR đối xứng hoán đổi hai bit mà không cần biến tạm — và trên máy tính lượng tử, CNOT chính là phép XOR!"
    },
    {
      id: 9,
      title: "Bernstein-Vazirani: Tìm Chuỗi Bí Mật s=11",
      level: "Nâng cao",
      qubits: 3,
      presetGates: "",
      targetDesc: "Đo q0, q1 ra chính xác 11 (index 3 trong 2 qubit)",
      expected: () => makeTargetState(3, [[3, S2], [7, -S2]]),
      desc: "Thuật toán Bernstein-Vazirani: Tìm chuỗi bí mật s=11 chỉ trong 1 lần gọi hàm f(x) = s·x! Qubit 0,1 là thanh ghi nhập, Qubit 2 là ancilla.",
      hints: [
        "1. Tạo superposition: H0, H1.",
        "2. Đưa ancilla q2 vào |−⟩: X2, H2.",
        "3. Oracle cho s=11: CX0-2, CX1-2.",
        "4. Giao thoa ngược: H0, H1.",
        "Lời giải: H0, H1, X2, H2, CX0-2, CX1-2, H0, H1."
      ],
      solution: "H0, H1, X2, H2, CX0-2, CX1-2, H0, H1",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const hasOracle = gStrs.includes("CX0-2") && gStrs.includes("CX1-2");
        const h0Count = gStrs.filter(s => s === "H0").length;
        const h1Count = gStrs.filter(s => s === "H1").length;
        if (!hasOracle || h0Count < 2 || h1Count < 2) {
          return {
            valid: false,
            message: "Thử thách yêu cầu áp dụng thuật toán Bernstein-Vazirani đầy đủ với các cổng Hadamard (H0, H1 cả trước và sau oracle) và oracle truy vấn bí mật (CX0-2, CX1-2)!"
          };
        }
        return { valid: true };
      },
      explain: "Máy tính cổ điển cần n lần hỏi để xác định chuỗi bí mật n-bit. Thuật toán Bernstein-Vazirani chỉ cần đúng 1 lần truy vấn lượng tử nhờ phase kickback song song trên toàn bộ các nhánh!"
    },
    {
      id: 10,
      title: "Grover Search 2-Qubit: Tìm |11⟩",
      level: "Anh Hùng",
      qubits: 2,
      presetGates: "",
      targetDesc: "|11⟩ với xác suất 100%",
      expected: () => makeTargetState(2, [[3, 1]]),
      desc: "Thuật toán tìm kiếm Grover: Trong 4 trạng thái |00⟩, |01⟩, |10⟩, |11⟩, hãy khuếch đại biên độ của trạng thái mục tiêu |11⟩ lên chính xác 100% trong đúng 1 vòng lặp!",
      hints: [
        "1. Trải đều: H0, H1.",
        "2. Oracle đánh dấu |11⟩: Cổng CZ0-1.",
        "3. Bộ khuếch đại (Diffuser): H0, H1, X0, X1, CZ0-1, X0, X1, H0, H1.",
        "Lời giải: H0, H1, CZ0-1, H0, H1, X0, X1, CZ0-1, X0, X1, H0, H1."
      ],
      solution: "H0, H1, CZ0-1, H0, H1, X0, X1, CZ0-1, X0, X1, H0, H1",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const czCount = gStrs.filter(s => s === "CZ0-1" || s === "CZ1-0").length;
        const hCount = gStrs.filter(s => s === "H0" || s === "H1").length;
        const hasX = gStrs.includes("X0") && gStrs.includes("X1");
        const endsWithH = gStrs.length >= 2 && (gStrs[gStrs.length - 1] === "H0" || gStrs[gStrs.length - 1] === "H1");
        if (czCount < 2 || hCount < 6 || !hasX || !endsWithH) {
          return {
            valid: false,
            message: "Thử thách yêu cầu triển khai thuật toán Grover đầy đủ (Oracle CZ0-1 và bộ khuếch đại Diffuser gồm Hadamard, X, và CZ0-1), không dùng cổng X đơn lẻ để lật bit trực tiếp!"
          };
        }
        return { valid: true };
      },
      explain: "Grover gồm 2 bước đối xứng: Oracle lật dấu mục tiêu qua trục hoành, và Diffuser lật toàn bộ các biên độ qua giá trị trung bình. Sau 1 vòng lặp, biên độ của |11⟩ đạt cực đại 100%!"
    },
    {
      id: 11,
      title: "Trạng Thái GHZ 3-Qubit",
      level: "Trung cấp",
      qubits: 3,
      presetGates: "",
      targetDesc: "|GHZ⟩ = (|000⟩ + |111⟩) / √2",
      expected: () => makeTargetState(3, [[0, S2], [7, S2]]),
      desc: "Tạo trạng thái vướng víu Greenberger–Horne–Zeilinger (GHZ) trên 3 qubit. Khi đo 1 qubit, 2 qubit còn lại lập tức sụp đổ theo cùng giá trị!",
      hints: [
        "1. Đưa q0 vào chồng chập: H0.",
        "2. Vướng q0 sang q1: CX0-1.",
        "3. Vướng tiếp q1 sang q2: CX1-2.",
        "Lời giải: H0, CX0-1, CX1-2."
      ],
      solution: "H0, CX0-1, CX1-2",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const cxCount = gStrs.filter(s => s.startsWith("CX")).length;
        if (!gStrs.includes("H0") || cxCount < 2) {
          return {
            valid: false,
            message: "Thử thách yêu cầu dùng cổng H0 và ít nhất 2 cổng CNOT liên hoàn để tạo trạng thái GHZ vướng víu 3 qubit!"
          };
        }
        return { valid: true };
      },
      explain: "Trạng thái GHZ là mở rộng tự nhiên của Bell pair lên 3 hạt. Nó là nền tảng cho mã sửa lỗi lượng tử Shor và các giao thức mật mã lượng tử đa bên!"
    },
    {
      id: 12,
      title: "Mã Sửa Lỗi Bit-Flip 3-Qubit",
      level: "Anh Hùng",
      qubits: 3,
      presetGates: "H0, CX0-1, CX0-2, X1",
      targetDesc: "Mã hóa |+⟩ thành (|000⟩ + |111⟩)/√2 rồi sửa lỗi lật bit",
      expected: () => makeTargetState(3, [[0, S2], [7, S2]]),
      desc: "Mạch đã mã hoá 1 qubit thành 3 qubit logic và bị lỗi lật bit X lên q1 (H0, CX0-1, CX0-2, X1). Hãy thêm cổng sửa lỗi để khôi phục trạng thái về chuẩn (|000⟩+|111⟩)/√2!",
      hints: [
        "Mạch ban đầu: H0, CX0-1, CX0-2, X1 (đang bị lỗi ở q1).",
        "Vì biết lỗi đang ở q1, chỉ cần áp thêm 1 cổng X lên q1 (X1) để hoàn nguyên bit!",
        "Lời giải: H0, CX0-1, CX0-2, X1, X1."
      ],
      solution: "H0, CX0-1, CX0-2, X1, X1",
      validate: (gates, gStrs) => {
        gStrs = (gStrs && Array.isArray(gStrs)) ? gStrs : (gates || []).map(gateToString);
        const preset = ["H0", "CX0-1", "CX0-2", "X1"];
        const matchesPreset = preset.every((p, idx) => gStrs[idx] === p);
        if (!matchesPreset) {
          return {
            valid: false,
            message: "Thử thách yêu cầu giữ nguyên mạch mã hóa và mô phỏng lỗi ban đầu: H0, CX0-1, CX0-2, X1!"
          };
        }
        const correctionGates = gStrs.slice(preset.length);
        const hasCorrection = correctionGates.length >= 1 && correctionGates.includes("X1");
        if (!hasCorrection) {
          return {
            valid: false,
            message: "Hãy thêm cổng sửa lỗi X1 sau các cổng có sẵn để sửa lỗi lật bit trên qubit 1!"
          };
        }
        return { valid: true };
      },
      explain: "Trong mã 3-qubit bit-flip, nếu phát hiện hội chứng syndrome cho thấy qubit 1 bị lỗi, ta chỉ cần áp cổng X1 để hoàn nguyên qubit về trạng thái ban đầu mà không làm hỏng thông tin pha!"
    }
  ];

  // ═════════════════════════════════════════════════════════════════════════
  // CHALLENGE CONTROLLER & UI RENDERER
  // ═════════════════════════════════════════════════════════════════════════
  let curChIndex = 0;
  let chProgress = {};

  function loadProgress() {
    try {
      const s = localStorage.getItem("qzh_kata_progress");
      if (s) chProgress = JSON.parse(s);
    } catch (e) {}
  }

  function saveProgress() {
    try {
      localStorage.setItem("qzh_kata_progress", JSON.stringify(chProgress));
    } catch (e) {}
  }

  function selectChallenge(idx) {
    curChIndex = Math.max(0, Math.min(CHALLENGES.length - 1, idx));
    renderChallengeUI();
    sound(480, 'sine', 0.06);
    try {
      if ((document.querySelector(".prac-tabs") || document.getElementById("ch-sidebar-list")) && window.history && window.history.replaceState) {
        window.history.replaceState(null, "", "#ch-" + (curChIndex + 1));
      }
    } catch (e) {}
  }
  window.selectChallenge = selectChallenge;

  function nextChallenge() {
    if (curChIndex < CHALLENGES.length - 1) {
      selectChallenge(curChIndex + 1);
    }
  }
  window.nextChallenge = nextChallenge;

  function prevChallenge() {
    if (curChIndex > 0) {
      selectChallenge(curChIndex - 1);
    }
  }
  window.prevChallenge = prevChallenge;

  let curHintTier = 0;
  function showChallengeHint() {
    const ch = CHALLENGES[curChIndex];
    curHintTier = Math.min(ch.hints.length, curHintTier + 1);
    const box = document.getElementById("ch-hint-box");
    if (!box) return;
    box.style.display = "block";
    box.innerHTML = ch.hints.slice(0, curHintTier).map((h, i) =>
      `<div class="ch-hint-line">💡 <b>Gợi ý ${i + 1}:</b> ${h}</div>`
    ).join("");
    sound(400 + curHintTier * 60, 'sine', 0.08);
  }
  window.showChallengeHint = showChallengeHint;

  function showChallengeSolution() {
    const ch = CHALLENGES[curChIndex];
    const box = document.getElementById("ch-hint-box");
    if (!box) return;
    box.style.display = "block";
    box.innerHTML += `
      <div class="ch-sol-line" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.6rem">
        <span>🔑 <b>Mạch lời giải:</b> <code>${ch.solution}</code></span>
        <button class="ql-btn primary" onclick="loadChallengeSolution()" style="padding:0.25rem 0.75rem;font-size:0.78rem">
          ⚡ Nạp lời giải vào mạch
        </button>
      </div>`;
    sound(350, 'sine', 0.1);
  }
  window.showChallengeSolution = showChallengeSolution;

  function loadChallengeSolution() {
    const ch = CHALLENGES[curChIndex];
    const qlabEl = document.getElementById("ch-qlab-instance");
    if (!qlabEl) return;
    window.QLab.loadGates(qlabEl, ch.solution);
    sound(587.33, 'triangle', 0.1);
    verifyChallenge();
  }
  window.loadChallengeSolution = loadChallengeSolution;

  function verifyChallenge() {
    const ch = CHALLENGES[curChIndex];
    const qlabEl = document.getElementById("ch-qlab-instance");
    if (!qlabEl) return;

    const widget = window.QLab.getWidget(qlabEl);
    const gates = widget ? widget.gates : window.QLab.parseGates(qlabEl.getAttribute("data-current-gates") || qlabEl.getAttribute("data-gates") || "");
    const meterEl = document.getElementById("ch-fidelity-meter");
    const valEl = document.getElementById("ch-fidelity-val");
    const statusEl = document.getElementById("ch-result-status");

    // 1. Chống False-Pass khi mạch trống
    if (!gates || gates.length === 0) {
      soundFail();
      if (meterEl) meterEl.style.width = "0%";
      if (valEl) valEl.innerText = "0.0%";
      if (statusEl) {
        statusEl.className = "ch-result-card fail";
        statusEl.innerHTML = `
          <div class="ch-res-head">⚠️ <b>MẠCH ĐANG TRỐNG</b></div>
          <p class="ch-res-body">Bạn chưa thêm cổng lượng tử nào vào mạch! Hãy chọn qubit và bấm vào cổng ở bảng điều khiển bên dưới để xây dựng mạch trước khi kiểm tra.</p>
        `;
        statusEl.style.display = "block";
      }
      return;
    }

    const gStrs = gates.map(gateToString);

    // 2. Kiểm tra điều kiện cấu trúc mạch riêng của thử thách (nếu có)
    if (typeof ch.validate === "function") {
      const vRes = ch.validate(gates, gStrs);
      let isValid = true;
      let errorMsg = "";
      if (typeof vRes === "boolean") {
        isValid = vRes;
      } else if (typeof vRes === "string") {
        isValid = false;
        errorMsg = vRes;
      } else if (vRes && typeof vRes === "object") {
        isValid = vRes.valid !== false;
        errorMsg = vRes.message || "";
      }

      if (!isValid) {
        soundFail();
        if (meterEl) meterEl.style.width = "0%";
        if (valEl) valEl.innerText = "0.0%";
        if (statusEl) {
          statusEl.className = "ch-result-card fail";
          statusEl.innerHTML = `
            <div class="ch-res-head">⚠️ <b>YÊU CẦU MẠCH CHƯA ĐẠT</b></div>
            <p class="ch-res-body">${errorMsg || "Mạch chưa thỏa mãn cấu trúc yêu cầu của bài toán."}</p>
          `;
          statusEl.style.display = "block";
        }
        return;
      }
    }

    const currentState = window.QLab.Sim.run(ch.qubits, gates);
    const expectedState = ch.expected();

    const fidelity = computeFidelity(currentState, expectedState);
    const pct = Math.min(100, Math.max(0, fidelity * 100));

    if (meterEl) meterEl.style.width = pct.toFixed(1) + "%";
    if (valEl) valEl.innerText = pct.toFixed(1) + "%";

    if (fidelity >= 0.999) {
      soundSuccess();
      chProgress[ch.id] = true;
      saveProgress();
      renderChallengeList();

      if (statusEl) {
        statusEl.className = "ch-result-card success";
        statusEl.innerHTML = `
          <div class="ch-res-head">🎉 <b>CHÍNH XÁC 100%! BẠN ĐÃ VƯỢT QUA THỬ THÁCH</b></div>
          <p class="ch-res-body">${ch.explain}</p>
          <div class="ch-res-nav">
            ${curChIndex < CHALLENGES.length - 1
              ? `<button class="ql-btn primary" onclick="nextChallenge()">Sang bài ${curChIndex + 2} →</button>`
              : `<span class="badge green">🏆 Chúc mừng bạn đã hoàn thành toàn bộ 12 thử thách!</span>`}
          </div>
        `;
        statusEl.style.display = "block";
      }
    } else {
      soundFail();
      if (statusEl) {
        statusEl.className = "ch-result-card fail";
        statusEl.innerHTML = `
          <div class="ch-res-head">❌ <b>CHƯA KHỚP (Độ trùng khớp: ${pct.toFixed(1)}%)</b></div>
          <p class="ch-res-body">Trạng thái mạch hiện tại chưa đạt mục tiêu <code>${ch.targetDesc}</code>. Hãy kiểm tra lại thứ tự cổng hoặc bấm nút Gợi Ý để nhận chỉ dẫn từng bước.</p>
        `;
        statusEl.style.display = "block";
      }
    }
  }
  window.verifyChallenge = verifyChallenge;

  function renderChallengeList() {
    const listEl = document.getElementById("ch-sidebar-list");
    if (!listEl) return;
    const completedCount = Object.keys(chProgress).length;
    const countEl = document.getElementById("ch-completed-count");
    if (countEl) countEl.innerText = `${completedCount}/${CHALLENGES.length}`;

    listEl.innerHTML = CHALLENGES.map((c, i) => {
      const isDone = !!chProgress[c.id];
      const isCur = i === curChIndex;
      return `
        <button onclick="selectChallenge(${i})" class="ch-item-btn ${isCur ? 'active' : ''} ${isDone ? 'done' : ''}">
          <span class="ch-dot">${isDone ? '✓' : (i + 1)}</span>
          <div class="ch-item-info">
            <div class="ch-item-t">${c.title}</div>
            <div class="ch-item-sub">${c.qubits} Qubit · ${c.level}</div>
          </div>
        </button>
      `;
    }).join('');
  }

  function renderChallengeUI() {
    const ch = CHALLENGES[curChIndex];
    curHintTier = 0;
    renderChallengeList();

    const titleEl = document.getElementById("ch-cur-title");
    const descEl = document.getElementById("ch-cur-desc");
    const targetEl = document.getElementById("ch-cur-target");
    const hintBox = document.getElementById("ch-hint-box");
    const statusEl = document.getElementById("ch-result-status");
    const meterEl = document.getElementById("ch-fidelity-meter");
    const valEl = document.getElementById("ch-fidelity-val");

    if (titleEl) titleEl.innerText = `Bài ${ch.id}: ${ch.title}`;
    if (descEl) descEl.innerText = ch.desc;
    if (targetEl) targetEl.innerText = ch.targetDesc;
    if (hintBox) { hintBox.style.display = "none"; hintBox.innerHTML = ""; }
    if (statusEl) statusEl.style.display = "none";
    if (meterEl) meterEl.style.width = "0%";
    if (valEl) valEl.innerText = "0%";

    const mount = document.getElementById("ch-qlab-mount");
    if (mount) {
      const preset = ch.presetGates || "";
      mount.innerHTML = `
        <div class="qlab" id="ch-qlab-instance" data-n="${ch.qubits}" data-gates="${preset}" data-shots="1024"
             data-title="Bàn Thao Tác Mạch · Bài ${ch.id}"></div>
      `;
      window.QLab.init(mount);
    }
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 2: INTERACTIVE 3D/ISOMETRIC BLOCH SPHERE EXPLORER
  // ═════════════════════════════════════════════════════════════════════════
  let canvasBloch, ctxBloch;
  let blochState = { theta: Math.PI / 2, phi: 0 };
  let blochAnimVector = { x: 1, y: 0, z: 0 };
  let blochTargetVector = { x: 1, y: 0, z: 0 };
  let blochYaw = 0.55, blochPitch = 0.35;
  let isDraggingBloch = false;
  let lastMouseX = 0, lastMouseY = 0;
  let isBlochInited = false;
  let blochLoopStarted = false;

  function resizeBlochCanvas() {
    if (!canvasBloch || !canvasBloch.parentElement) return;
    const rect = canvasBloch.parentElement.getBoundingClientRect();
    if (rect.width > 0) {
      canvasBloch.width = rect.width;
      canvasBloch.height = 340;
    }
  }

  function initBlochExplorer() {
    canvasBloch = document.getElementById("canvas-bloch-interactive");
    if (!canvasBloch) return;
    ctxBloch = canvasBloch.getContext("2d");

    resizeBlochCanvas();

    if (!isBlochInited) {
      isBlochInited = true;
      window.addEventListener("resize", resizeBlochCanvas);

      canvasBloch.addEventListener("mousedown", (e) => {
        isDraggingBloch = true;
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
      });
      window.addEventListener("mouseup", () => isDraggingBloch = false);
      window.addEventListener("mousemove", (e) => {
        if (!isDraggingBloch) return;
        const dx = e.clientX - lastMouseX;
        const dy = e.clientY - lastMouseY;
        blochYaw += dx * 0.012;
        blochPitch = Math.max(-1.4, Math.min(1.4, blochPitch + dy * 0.012));
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
      });
    }

    if (!blochLoopStarted) {
      blochLoopStarted = true;
      renderBlochLoop();
    }
    updateBlochUI();
  }

  function project3D(x, y, z, cx, cy, R) {
    const cosY = Math.cos(blochYaw), sinY = Math.sin(blochYaw);
    const x1 = x * cosY - y * sinY;
    const y1 = x * sinY + y * cosY;

    const cosP = Math.cos(blochPitch), sinP = Math.sin(blochPitch);
    const y2 = y1 * cosP - z * sinP;
    const z2 = y1 * sinP + z * cosP;

    return {
      px: cx + x1 * R,
      py: cy - z2 * R,
      depth: y2
    };
  }

  function renderBlochLoop() {
    if (!ctxBloch) return;
    const w = canvasBloch.width;
    const h = canvasBloch.height;
    if (w <= 0 || h <= 0) {
      requestAnimationFrame(renderBlochLoop);
      return;
    }
    ctxBloch.clearRect(0, 0, w, h);

    const cx = w * 0.5;
    const cy = h * 0.52;
    const R = Math.min(w, h) * 0.38;

    blochAnimVector.x += (blochTargetVector.x - blochAnimVector.x) * 0.12;
    blochAnimVector.y += (blochTargetVector.y - blochAnimVector.y) * 0.12;
    blochAnimVector.z += (blochTargetVector.z - blochAnimVector.z) * 0.12;

    // Sphere Outline
    ctxBloch.beginPath();
    ctxBloch.arc(cx, cy, R, 0, Math.PI * 2);
    ctxBloch.fillStyle = "rgba(94, 234, 212, 0.035)";
    ctxBloch.fill();
    ctxBloch.strokeStyle = "rgba(255, 255, 255, 0.18)";
    ctxBloch.lineWidth = 1.5;
    ctxBloch.stroke();

    // Equator ring
    ctxBloch.beginPath();
    ctxBloch.strokeStyle = "rgba(255, 255, 255, 0.12)";
    ctxBloch.setLineDash([4, 4]);
    for (let a = 0; a <= Math.PI * 2; a += 0.1) {
      const p = project3D(Math.cos(a), Math.sin(a), 0, cx, cy, R);
      if (a === 0) ctxBloch.moveTo(p.px, p.py);
      else ctxBloch.lineTo(p.px, p.py);
    }
    ctxBloch.stroke();
    ctxBloch.setLineDash([]);

    // Axes
    function drawAxis(x, y, z, label, col) {
      const p0 = project3D(-x, -y, -z, cx, cy, R);
      const p1 = project3D(x, y, z, cx, cy, R);
      ctxBloch.beginPath();
      ctxBloch.moveTo(p0.px, p0.py);
      ctxBloch.lineTo(p1.px, p1.py);
      ctxBloch.strokeStyle = "rgba(255, 255, 255, 0.14)";
      ctxBloch.lineWidth = 1;
      ctxBloch.stroke();

      ctxBloch.fillStyle = col;
      ctxBloch.font = 'bold 11px "JetBrains Mono", monospace';
      ctxBloch.fillText(label, p1.px + 6, p1.py + 4);
    }

    drawAxis(1.2, 0, 0, "+X |+⟩", "#5eead4");
    drawAxis(0, 1.2, 0, "+Y |i⟩", "#818cf8");
    drawAxis(0, 0, 1.2, "+Z |0⟩", "#fbbf24");

    const pSouth = project3D(0, 0, -1.2, cx, cy, R);
    ctxBloch.fillStyle = "#c4a2ff";
    ctxBloch.font = 'bold 11px "JetBrains Mono", monospace';
    ctxBloch.fillText("-Z |1⟩", pSouth.px + 6, pSouth.py + 4);

    const pTip = project3D(blochAnimVector.x, blochAnimVector.y, blochAnimVector.z, cx, cy, R);

    // Shadow projections
    const pShadow = project3D(blochAnimVector.x, blochAnimVector.y, 0, cx, cy, R);
    ctxBloch.beginPath();
    ctxBloch.moveTo(cx, cy);
    ctxBloch.lineTo(pShadow.px, pShadow.py);
    ctxBloch.strokeStyle = "rgba(94, 234, 212, 0.25)";
    ctxBloch.lineWidth = 1.2;
    ctxBloch.setLineDash([2, 3]);
    ctxBloch.stroke();
    ctxBloch.lineTo(pTip.px, pTip.py);
    ctxBloch.stroke();
    ctxBloch.setLineDash([]);

    // Glow halo
    ctxBloch.beginPath();
    ctxBloch.arc(pTip.px, pTip.py, 16, 0, Math.PI * 2);
    ctxBloch.fillStyle = "rgba(94, 234, 212, 0.2)";
    ctxBloch.fill();

    // Vector
    ctxBloch.beginPath();
    ctxBloch.moveTo(cx, cy);
    ctxBloch.lineTo(pTip.px, pTip.py);
    ctxBloch.strokeStyle = "#5eead4";
    ctxBloch.lineWidth = 3;
    ctxBloch.stroke();

    ctxBloch.beginPath();
    ctxBloch.arc(pTip.px, pTip.py, 6.5, 0, Math.PI * 2);
    ctxBloch.fillStyle = "#ffffff";
    ctxBloch.fill();
    ctxBloch.strokeStyle = "#2dd4bf";
    ctxBloch.lineWidth = 2;
    ctxBloch.stroke();

    requestAnimationFrame(renderBlochLoop);
  }

  function updateBlochFromAngles() {
    const th = blochState.theta;
    const ph = blochState.phi;
    blochTargetVector = {
      x: Math.sin(th) * Math.cos(ph),
      y: Math.sin(th) * Math.sin(ph),
      z: Math.cos(th)
    };
    updateBlochUI();
  }

  function updateBlochUI() {
    const th = blochState.theta;
    const ph = blochState.phi;
    const p0 = Math.cos(th / 2) ** 2;
    const p1 = Math.sin(th / 2) ** 2;

    const elX = document.getElementById("bloch-val-x");
    const elY = document.getElementById("bloch-val-y");
    const elZ = document.getElementById("bloch-val-z");
    const elP0 = document.getElementById("bloch-val-p0");
    const elP1 = document.getElementById("bloch-val-p1");
    const elBar0 = document.getElementById("bloch-bar-0");
    const elBar1 = document.getElementById("bloch-bar-1");
    const elStateEq = document.getElementById("bloch-state-eq");

    if (elX) elX.innerText = blochTargetVector.x.toFixed(3);
    if (elY) elY.innerText = blochTargetVector.y.toFixed(3);
    if (elZ) elZ.innerText = blochTargetVector.z.toFixed(3);
    if (elP0) elP0.innerText = (p0 * 100).toFixed(1) + "%";
    if (elP1) elP1.innerText = (p1 * 100).toFixed(1) + "%";
    if (elBar0) elBar0.style.width = (p0 * 100).toFixed(1) + "%";
    if (elBar1) elBar1.style.width = (p1 * 100).toFixed(1) + "%";

    const a = Math.cos(th / 2).toFixed(3);
    const b = Math.sin(th / 2).toFixed(3);
    const phDeg = (ph * 180 / Math.PI).toFixed(0);
    if (elStateEq) {
      elStateEq.innerHTML = `|ψ⟩ = <b>${a}</b>|0⟩ + <b>${b}</b> e<sup>i(${phDeg}°)</sup>|1⟩`;
    }
  }

  function applyBlochGate(op) {
    sound(500, 'sine', 0.08);
    switch (op) {
      case '0': blochState.theta = 0; blochState.phi = 0; break;
      case '1': blochState.theta = Math.PI; blochState.phi = 0; break;
      case 'X':
        blochState.theta = Math.PI - blochState.theta;
        blochState.phi = -blochState.phi;
        break;
      case 'Y':
        blochState.theta = Math.PI - blochState.theta;
        blochState.phi = Math.PI - blochState.phi;
        break;
      case 'Z':
        blochState.phi = blochState.phi + Math.PI;
        break;
      case 'H':
        if (Math.abs(blochState.theta) < 0.05) { blochState.theta = Math.PI / 2; blochState.phi = 0; }
        else if (Math.abs(blochState.theta - Math.PI) < 0.05) { blochState.theta = Math.PI / 2; blochState.phi = Math.PI; }
        else if (Math.abs(blochState.theta - Math.PI / 2) < 0.05 && Math.abs(blochState.phi) < 0.05) { blochState.theta = 0; }
        else {
          const v = blochTargetVector;
          const nx = v.z, ny = -v.y, nz = v.x;
          blochState.theta = Math.acos(Math.max(-1, Math.min(1, nz)));
          blochState.phi = Math.atan2(ny, nx);
        }
        break;
      case 'S':
        blochState.phi = blochState.phi + Math.PI / 2;
        break;
      case 'T':
        blochState.phi = blochState.phi + Math.PI / 4;
        break;
    }
    // Normalize phi to [0, 2*PI)
    blochState.phi = ((blochState.phi % (Math.PI * 2)) + Math.PI * 2) % (Math.PI * 2);
    updateBlochFromAngles();
  }
  window.applyBlochGate = applyBlochGate;

  function measureBlochQubit() {
    const p0 = Math.cos(blochState.theta / 2) ** 2;
    const is0 = Math.random() < p0;
    sound(is0 ? 660 : 440, 'triangle', 0.15);

    const resBox = document.getElementById("bloch-meas-result");
    if (resBox) {
      resBox.className = "elab-badge " + (is0 ? "cyan" : "indigo");
      resBox.innerText = `Sụp đổ về |${is0 ? '0' : '1'}⟩!`;
    }

    blochState.theta = is0 ? 0 : Math.PI;
    blochState.phi = 0;
    updateBlochFromAngles();
  }
  window.measureBlochQubit = measureBlochQubit;

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 3: PAIRWISE INDEXING EXPLORER (PHASE 1 & 3 SIMULATOR HEART)
  // ═════════════════════════════════════════════════════════════════════════
  let pairN = 3;
  let pairTarget = 1;
  let pairCtrl = null;

  function setPairN(n) {
    pairN = n;
    pairTarget = Math.min(pairTarget, pairN - 1);
    if (pairCtrl !== null && (pairCtrl >= pairN || pairCtrl === pairTarget)) {
      pairCtrl = null;
    }
    renderPairwiseLab();
  }
  window.setPairN = setPairN;

  function setPairTarget(t) {
    pairTarget = t;
    if (pairCtrl === t) {
      pairCtrl = null;
    }
    renderPairwiseLab();
  }
  window.setPairTarget = setPairTarget;

  function setPairCtrl(c) {
    pairCtrl = (c === -1 || c === pairTarget || c >= pairN) ? null : c;
    renderPairwiseLab();
  }
  window.setPairCtrl = setPairCtrl;

  function renderPairwiseLab() {
    const root = document.getElementById("pairwise-lab-mount");
    if (!root) return;

    const N = 1 << pairN;
    const bit = 1 << pairTarget;
    const pairs = [];

    for (let i = 0; i < N; i++) {
      if ((i & bit) === 0) {
        const j = i | bit;
        const ctrlPass = pairCtrl === null ? true : ((i & (1 << pairCtrl)) !== 0);
        pairs.push({ i, j, ctrlPass });
      }
    }

    root.innerHTML = `
      <div class="pw-controls">
        <div class="pw-control-group">
          <span class="ql-plabel">Số Qubit (N):</span>
          ${[1, 2, 3, 4].map(n =>
            `<button onclick="setPairN(${n})" class="ql-sbtn ${n === pairN ? 'on' : ''}">${n}</button>`
          ).join('')}
        </div>
        <div class="pw-control-group">
          <span class="ql-plabel">Qubit Đích (Target t):</span>
          ${Array.from({ length: pairN }, (_, k) =>
            `<button onclick="setPairTarget(${k})" class="ql-sbtn ${k === pairTarget ? 'on' : ''}">q${k}</button>`
          ).join('')}
        </div>
        <div class="pw-control-group">
          <span class="ql-plabel">Qubit Điều Khiển (Control):</span>
          <button onclick="setPairCtrl(-1)" class="ql-sbtn ${pairCtrl === null ? 'on' : ''}">Không (1-qubit)</button>
          ${Array.from({ length: pairN }, (_, k) =>
            k === pairTarget ? '' :
            `<button onclick="setPairCtrl(${k})" class="ql-sbtn ${k === pairCtrl ? 'on' : ''}">q${k}</button>`
          ).join('')}
        </div>
      </div>

      <div class="pw-summary-banner">
        Tổng <b>2<sup>${pairN}</sup> = ${N}</b> biên độ chia thành <b>2<sup>${pairN}-1</sup> = ${pairs.length}</b> cặp độc lập.
        Mỗi cặp chỉ khác nhau ở bit <b>q<sub>${pairTarget}</sub></b> (trọng số 2<sup>${pairTarget}</sup> = ${bit}).
        ${pairCtrl !== null ? `Chỉ áp ma trận lên cặp có bit <b>q<sub>${pairCtrl}</sub> = 1</b> (cổng điều khiển).` : ''}
      </div>

      <div class="pw-grid">
        ${pairs.map((p, idx) => {
          const binI = p.i.toString(2).padStart(pairN, '0');
          const binJ = p.j.toString(2).padStart(pairN, '0');
          return `
            <div class="pw-card ${p.ctrlPass ? 'active-pair' : 'skipped-pair'}">
              <div class="pw-card-head">
                <span class="pw-pair-badge">Cặp #${idx + 1}</span>
                <span class="pw-status-badge">${p.ctrlPass ? '✓ Độc lập O(1)' : 'Bỏ qua (Ctrl=0)'}</span>
              </div>
              <div class="pw-indices">
                <div class="pw-idx-item">
                  <span class="pw-idx-no">i = ${p.i}</span>
                  <span class="pw-ket-label">|${binI}⟩</span>
                  <span class="pw-bit-hl">(bit ${pairTarget} = 0)</span>
                </div>
                <div class="pw-arrow">⟷</div>
                <div class="pw-idx-item">
                  <span class="pw-idx-no">j = ${p.j}</span>
                  <span class="pw-ket-label">|${binJ}⟩</span>
                  <span class="pw-bit-hl">(bit ${pairTarget} = 1)</span>
                </div>
              </div>
              <div class="pw-formula">
                <code>state[${p.i}]' = U₀₀·state[${p.i}] + U₀₁·state[${p.j}]</code><br>
                <code>state[${p.j}]' = U₁₀·state[${p.i}] + U₁₁·state[${p.j}]</code>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 4: GROVER 2D ROTATION & AMPLITUDE AMPLIFICATION
  // ═════════════════════════════════════════════════════════════════════════
  let groverN = 4;
  let groverK = 0;
  let canvasGrover, ctxGrover;

  let isGroverInited = false;

  function resizeGroverCanvas() {
    if (!canvasGrover || !canvasGrover.parentElement) return;
    const rect = canvasGrover.parentElement.getBoundingClientRect();
    if (rect.width > 0) {
      canvasGrover.width = rect.width;
      canvasGrover.height = 280;
      drawGroverCanvas();
    }
  }

  function setGroverN(n) {
    groverN = n;
    groverK = 0;
    document.querySelectorAll("[data-gn]").forEach(b => {
      b.classList.toggle("on", +b.dataset.gn === n);
    });
    updateGroverUI();
  }
  window.setGroverN = setGroverN;

  function setGroverK(k) {
    groverK = Math.max(0, Math.min(10, k));
    updateGroverUI();
  }
  window.setGroverK = setGroverK;

  function initGroverExplorer() {
    canvasGrover = document.getElementById("canvas-grover-2d");
    if (!canvasGrover) return;
    ctxGrover = canvasGrover.getContext("2d");

    resizeGroverCanvas();

    if (!isGroverInited) {
      isGroverInited = true;
      window.addEventListener("resize", resizeGroverCanvas);
    }
    updateGroverUI();
  }

  function updateGroverUI() {
    const theta = Math.asin(1 / Math.sqrt(groverN));
    const curAngle = (2 * groverK + 1) * theta;
    const targetProb = Math.sin(curAngle) ** 2;
    const optK = Math.round((Math.PI / 4) * Math.sqrt(groverN) - 0.5);

    const elProb = document.getElementById("grover-val-prob");
    const elAngle = document.getElementById("grover-val-angle");
    const elOptK = document.getElementById("grover-val-optk");
    const elSlider = document.getElementById("grover-slider-k");
    const elBadge = document.getElementById("grover-status-badge");

    if (elProb) elProb.innerText = (targetProb * 100).toFixed(1) + "%";
    if (elAngle) elAngle.innerText = (curAngle * 180 / Math.PI).toFixed(1) + "°";
    if (elOptK) elOptK.innerText = optK;
    if (elSlider) elSlider.value = groverK;

    if (elBadge) {
      if (groverK === optK) {
        elBadge.className = "elab-badge success";
        elBadge.innerText = "⭐ TỐI ƯU CỰC ĐẠI!";
      } else if (groverK > optK) {
        elBadge.className = "elab-badge danger";
        elBadge.innerText = "⚠ QUÁ VÒNG (OVER-ROTATION) — XÁC SUẤT BỊ TỤT!";
      } else {
        elBadge.className = "elab-badge";
        elBadge.innerText = `Vòng ${groverK} / ${optK}`;
      }
    }

    drawGroverCanvas();
  }

  function drawGroverCanvas() {
    if (!ctxGrover) return;
    const w = canvasGrover.width;
    const h = canvasGrover.height;
    if (w <= 0 || h <= 0) return;
    ctxGrover.clearRect(0, 0, w, h);

    const cx = w * 0.18;
    const cy = h * 0.82;
    const R = Math.min(w * 0.7, h * 0.72);

    // Axis 1: |w_perp>
    ctxGrover.beginPath();
    ctxGrover.moveTo(cx, cy);
    ctxGrover.lineTo(cx + R + 25, cy);
    ctxGrover.strokeStyle = "rgba(255, 255, 255, 0.2)";
    ctxGrover.lineWidth = 1.5;
    ctxGrover.stroke();
    ctxGrover.fillStyle = "#818cf8";
    ctxGrover.font = 'bold 11px "JetBrains Mono", monospace';
    ctxGrover.fillText("|ω^⊥⟩ (Mọi phần tử sai)", cx + R + 32, cy + 4);

    // Axis 2: |w>
    ctxGrover.beginPath();
    ctxGrover.moveTo(cx, cy);
    ctxGrover.lineTo(cx, cy - R - 25);
    ctxGrover.strokeStyle = "rgba(255, 255, 255, 0.2)";
    ctxGrover.lineWidth = 1.5;
    ctxGrover.stroke();
    ctxGrover.fillStyle = "#5eead4";
    ctxGrover.fillText("|ω⟩ (Mục tiêu đúng)", cx - 18, cy - R - 32);

    // Arc
    ctxGrover.beginPath();
    ctxGrover.arc(cx, cy, R, 0, -Math.PI / 2, true);
    ctxGrover.strokeStyle = "rgba(255, 255, 255, 0.1)";
    ctxGrover.setLineDash([3, 3]);
    ctxGrover.stroke();
    ctxGrover.setLineDash([]);

    const theta = Math.asin(1 / Math.sqrt(groverN));
    const curAngle = (2 * groverK + 1) * theta;

    const vx = cx + Math.cos(curAngle) * R;
    const vy = cy - Math.sin(curAngle) * R;

    ctxGrover.beginPath();
    ctxGrover.moveTo(vx, cy);
    ctxGrover.lineTo(vx, vy);
    ctxGrover.lineTo(cx, vy);
    ctxGrover.strokeStyle = "rgba(94, 234, 212, 0.25)";
    ctxGrover.setLineDash([2, 3]);
    ctxGrover.stroke();
    ctxGrover.setLineDash([]);

    ctxGrover.beginPath();
    ctxGrover.moveTo(cx, cy);
    ctxGrover.lineTo(vx, vy);
    ctxGrover.strokeStyle = "#5eead4";
    ctxGrover.lineWidth = 3.5;
    ctxGrover.stroke();

    ctxGrover.beginPath();
    ctxGrover.arc(vx, vy, 7, 0, Math.PI * 2);
    ctxGrover.fillStyle = "#ffffff";
    ctxGrover.fill();
    ctxGrover.strokeStyle = "#2dd4bf";
    ctxGrover.lineWidth = 2;
    ctxGrover.stroke();

    // Chart on right
    const chartX = w * 0.65;
    const chartY = h * 0.18;
    const chartW = w * 0.32;
    const chartH = h * 0.65;

    ctxGrover.fillStyle = "rgba(0, 0, 0, 0.35)";
    ctxGrover.fillRect(chartX, chartY, chartW, chartH);
    ctxGrover.strokeStyle = "rgba(255, 255, 255, 0.1)";
    ctxGrover.strokeRect(chartX, chartY, chartW, chartH);

    ctxGrover.fillStyle = "#a7b0c4";
    ctxGrover.font = '10px -apple-system, sans-serif';
    ctxGrover.fillText("Đường cong xác suất P(k)", chartX + 8, chartY + 16);

    const maxChartK = 10;
    ctxGrover.beginPath();
    ctxGrover.strokeStyle = "#818cf8";
    ctxGrover.lineWidth = 1.8;
    for (let x = 0; x <= chartW; x += 2) {
      const kVal = (x / chartW) * maxChartK;
      const ang = (2 * kVal + 1) * theta;
      const p = Math.sin(ang) ** 2;
      const y = chartY + chartH - p * (chartH - 28) - 6;
      if (x === 0) ctxGrover.moveTo(chartX + x, y);
      else ctxGrover.lineTo(chartX + x, y);
    }
    ctxGrover.stroke();

    const ptX = chartX + (groverK / maxChartK) * chartW;
    const ptP = Math.sin(curAngle) ** 2;
    const ptY = chartY + chartH - ptP * (chartH - 28) - 6;

    ctxGrover.beginPath();
    ctxGrover.arc(ptX, ptY, 5, 0, Math.PI * 2);
    ctxGrover.fillStyle = "#5eead4";
    ctxGrover.fill();
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 5: QUANTUM ERROR CORRECTION (QEC) LABORATORY
  // ═════════════════════════════════════════════════════════════════════════
  let qecErrorQubit = null;
  let qecSyndrome = null;
  let qecCorrected = false;

  function injectQecError(q) {
    qecErrorQubit = q === -1 ? null : q;
    qecSyndrome = null;
    qecCorrected = false;
    sound(380, 'sine', 0.08);
    renderQecUI();
  }
  window.injectQecError = injectQecError;

  function runQecSyndrome() {
    sound(540, 'triangle', 0.1);
    if (qecCorrected || qecErrorQubit === null) qecSyndrome = "00";
    else if (qecErrorQubit === 0) qecSyndrome = "10";
    else if (qecErrorQubit === 1) qecSyndrome = "11";
    else if (qecErrorQubit === 2) qecSyndrome = "01";
    renderQecUI();
  }
  window.runQecSyndrome = runQecSyndrome;

  function applyQecCorrection() {
    soundSuccess();
    qecCorrected = true;
    qecSyndrome = "00";
    renderQecUI();
  }
  window.applyQecCorrection = applyQecCorrection;

  function renderQecUI() {
    const root = document.getElementById("qec-lab-mount");
    if (!root) return;

    const synDesc = {
      "00": "Không phát hiện lỗi lật bit",
      "10": "Qubit 0 bị lật bit!",
      "11": "Qubit 1 bị lật bit!",
      "01": "Qubit 2 bị lật bit!"
    };

    root.innerHTML = `
      <div class="qec-station">
        <div class="qec-step-card">
          <h4>1. Trạng Thái Đã Mã Hóa (3 Qubit)</h4>
          <p class="tiny">|ψ⟩ = α|000⟩ + β|111⟩</p>
          <div class="qec-qubit-row">
            ${[0, 1, 2].map(q => `
              <div class="qec-qubit-chip ${qecErrorQubit === q ? (qecCorrected ? 'c-fixed' : 'c-err') : 'c-ok'}">
                <span>Qubit ${q}</span>
                <b>${qecErrorQubit === q ? (qecCorrected ? '✓ Đã sửa' : '💥 Bị lật X') : 'Bình thường'}</b>
              </div>
            `).join('')}
          </div>
        </div>

        <div class="qec-step-card">
          <h4>2. Giả Lập Môi Trường Gây Nhiễu</h4>
          <div class="qec-btn-row">
            <button onclick="injectQecError(-1)" class="ql-btn ${qecErrorQubit === null ? 'primary' : ''}">Không lỗi</button>
            <button onclick="injectQecError(0)" class="ql-btn ${qecErrorQubit === 0 ? 'primary' : ''}">Lật Bit Q0</button>
            <button onclick="injectQecError(1)" class="ql-btn ${qecErrorQubit === 1 ? 'primary' : ''}">Lật Bit Q1</button>
            <button onclick="injectQecError(2)" class="ql-btn ${qecErrorQubit === 2 ? 'primary' : ''}">Lật Bit Q2</button>
          </div>
        </div>

        <div class="qec-step-card">
          <h4>3. Đo Hội Chứng (Syndrome Measurement)</h4>
          <div class="row">
            <button onclick="runQecSyndrome()" class="ql-btn primary">▶ Đo Hội Chứng Ancilla</button>
            <span class="qec-syn-val">${qecSyndrome ? `Hội chứng: <b>[${qecSyndrome}]</b>` : 'Chưa đo'}</span>
          </div>
          ${qecSyndrome ? `
            <div class="qec-diagnosis">
              🔍 <b>Chẩn đoán:</b> ${synDesc[qecSyndrome]}
              ${qecErrorQubit !== null && !qecCorrected ? `
                <button onclick="applyQecCorrection()" class="ql-btn green" style="margin-left:auto">Sửa Lỗi Tự Động →</button>
              ` : ''}
            </div>
          ` : ''}
          ${qecCorrected ? `
            <div class="qec-success-box">
              ✨ <b>Thành công:</b> Cổng Pauli X đã được áp đúng lên Qubit ${qecErrorQubit}, phục hồi trạng thái nguyên vẹn 100%!
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 6: CHSH BELL INEQUALITY GAME
  // ═════════════════════════════════════════════════════════════════════════
  let chshRounds = 0;
  let chshWins = 0;
  let chshStrategy = 'quantum';
  let chshHistory = [];

  function setChshStrategy(strat) {
    chshStrategy = strat;
    chshRounds = 0;
    chshWins = 0;
    chshHistory = [];
    renderChshUI();
  }
  window.setChshStrategy = setChshStrategy;

  function playChshRound() {
    const x = Math.random() < 0.5 ? 0 : 1;
    const y = Math.random() < 0.5 ? 0 : 1;
    let a = 0, b = 0;

    if (chshStrategy === 'classical') {
      a = 0; b = 0;
    } else {
      const winProb = Math.cos(Math.PI / 8) ** 2;
      const isWin = Math.random() < winProb;
      if (isWin) {
        a = Math.random() < 0.5 ? 0 : 1;
        b = a ^ (x * y);
      } else {
        a = Math.random() < 0.5 ? 0 : 1;
        b = a ^ ((x * y) ^ 1);
      }
    }

    const won = (a ^ b) === (x * y);
    chshRounds++;
    if (won) chshWins++;
    chshHistory.unshift({ round: chshRounds, x, y, a, b, won });
    if (chshHistory.length > 8) chshHistory.pop();

    sound(won ? 650 : 320, 'sine', 0.08);
    renderChshUI();
  }
  window.playChshRound = playChshRound;

  function simulateChsh100() {
    const batchLast = [];
    for (let k = 0; k < 100; k++) {
      const x = Math.random() < 0.5 ? 0 : 1;
      const y = Math.random() < 0.5 ? 0 : 1;
      let a = 0, b = 0;
      if (chshStrategy === 'classical') {
        a = 0; b = 0;
      } else {
        const winProb = Math.cos(Math.PI / 8) ** 2;
        const isWin = Math.random() < winProb;
        if (isWin) {
          a = Math.random() < 0.5 ? 0 : 1;
          b = a ^ (x * y);
        } else {
          a = Math.random() < 0.5 ? 0 : 1;
          b = a ^ ((x * y) ^ 1);
        }
      }
      chshRounds++;
      const won = (a ^ b) === (x * y);
      if (won) chshWins++;
      if (k >= 95) {
        batchLast.push({ round: chshRounds, x, y, a, b, won });
      }
    }
    for (let i = batchLast.length - 1; i >= 0; i--) {
      chshHistory.unshift(batchLast[i]);
    }
    while (chshHistory.length > 8) chshHistory.pop();
    soundSuccess();
    renderChshUI();
  }
  window.simulateChsh100 = simulateChsh100;

  function renderChshUI() {
    const root = document.getElementById("chsh-game-mount");
    if (!root) return;

    const rate = chshRounds > 0 ? (chshWins / chshRounds * 100).toFixed(1) : "0.0";

    root.innerHTML = `
      <div class="chsh-box">
        <div class="chsh-strat-sel">
          <button onclick="setChshStrategy('classical')" class="ql-btn ${chshStrategy === 'classical' ? 'primary' : ''}">
            Chiến Lược Cổ Điển (Trần 75%)
          </button>
          <button onclick="setChshStrategy('quantum')" class="ql-btn ${chshStrategy === 'quantum' ? 'primary' : ''}">
            Chiến Lược Lượng Tử Vướng Víu (Trần ~85.4%)
          </button>
        </div>

        <div class="chsh-score-board">
          <div class="chsh-metric">
            <span class="chsh-lbl">Số Vòng Đã Chơi</span>
            <span class="chsh-num">${chshRounds}</span>
          </div>
          <div class="chsh-metric">
            <span class="chsh-lbl">Số Vòng Thắng</span>
            <span class="chsh-num">${chshWins}</span>
          </div>
          <div class="chsh-metric">
            <span class="chsh-lbl">Tỉ Lệ Thắng Thực Tế</span>
            <span class="chsh-num highlight">${rate}%</span>
          </div>
          <div class="chsh-metric">
            <span class="chsh-lbl">Giới Hạn Lý Thuyết</span>
            <span class="chsh-num">${chshStrategy === 'classical' ? '75.0%' : '85.4% (Tsirelson)'}</span>
          </div>
        </div>

        <div class="chsh-actions">
          <button onclick="playChshRound()" class="ql-btn primary">▶ Chơi 1 Vòng</button>
          <button onclick="simulateChsh100()" class="ql-btn">⚡ Mô Phỏng Nhanh 100 Vòng</button>
        </div>

        <div class="chsh-table">
          <div class="chsh-th"><span>Vòng</span><span>Câu hỏi (x, y)</span><span>Câu trả lời (a, b)</span><span>Điều kiện a⊕b = x·y</span><span>Kết quả</span></div>
          ${chshHistory.map((h, idx) => `
            <div class="chsh-tr ${h.won ? 'win' : 'lose'}">
              <span>#${h.round || (chshRounds - idx)}</span>
              <span>x=${h.x}, y=${h.y}</span>
              <span>a=${h.a}, b=${h.b}</span>
              <span>${h.a}^${h.b}=${h.a^h.b} vs ${h.x}·${h.y}=${h.x*h.y}</span>
              <span><b>${h.won ? '✓ THẮNG' : '✗ THUA'}</b></span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // ═════════════════════════════════════════════════════════════════════════
  // MODULE 7: SIMULATOR RAM & COMPLEXITY CALCULATOR (PHASE 3)
  // ═════════════════════════════════════════════════════════════════════════
  function fmtBytes(b) {
    if (b < 1024) return b + " B";
    if (b < 1024 ** 2) return (b / 1024).toFixed(1) + " KB";
    if (b < 1024 ** 3) return (b / (1024 ** 2)).toFixed(1) + " MB";
    if (b < 1024 ** 4) return (b / (1024 ** 3)).toFixed(2) + " GB";
    if (b < 1024 ** 5) return (b / (1024 ** 4)).toFixed(2) + " TB";
    return (b / (1024 ** 5)).toFixed(2) + " PB";
  }

  function updateRamCalc(n) {
    const elN = document.getElementById("ram-n-val");
    const elStates = document.getElementById("ram-states-val");
    const elVec = document.getElementById("ram-vec-val");
    const elMat = document.getElementById("ram-mat-val");
    const elPairs = document.getElementById("ram-pairs-val");
    const elStatus = document.getElementById("ram-status-card");

    if (elN) elN.innerText = n;
    const states = 2 ** n;
    if (elStates) elStates.innerText = states.toLocaleString();

    // 16 bytes per Complex64 (f64 real + f64 imag)
    const vecBytes = states * 16;
    if (elVec) elVec.innerText = fmtBytes(vecBytes);

    // Full matrix: 2^n * 2^n * 16 bytes
    // For n > 26, 2^(2n) exceeds 2^53 safe integer, so calculate in GB/TB directly
    let matStr = "";
    if (n <= 16) {
      matStr = fmtBytes((2 ** (2 * n)) * 16);
    } else {
      const gb = 16 * Math.pow(2, 2 * n - 30);
      if (gb < 1024) matStr = gb.toFixed(1) + " GB";
      else if (gb < 1024 * 1024) matStr = (gb / 1024).toFixed(1) + " TB";
      else matStr = (gb / (1024 * 1024)).toFixed(1) + " PB";
    }
    if (elMat) elMat.innerText = matStr;

    const pairs = states / 2;
    if (elPairs) elPairs.innerText = pairs.toLocaleString() + " cặp";

    if (elStatus) {
      if (n <= 25) {
        elStatus.className = "ram-metric-card good";
        elStatus.innerHTML = `
          <span class="ram-lbl">Đánh Giá Phần Cứng</span>
          <b style="color:var(--green)">🟢 Cực nhanh trên Laptop thông thường (RAM &lt; 1 GB)</b>
        `;
      } else if (n <= 29) {
        elStatus.className = "ram-metric-card";
        elStatus.innerHTML = `
          <span class="ram-lbl">Đánh Giá Phần Cứng</span>
          <b style="color:var(--amber)">🟡 Laptop 16GB RAM bắt đầu tới giới hạn (${fmtBytes(vecBytes)})</b>
        `;
      } else {
        elStatus.className = "ram-metric-card danger";
        elStatus.innerHTML = `
          <span class="ram-lbl">Đánh Giá Phần Cứng</span>
          <b style="color:var(--rose)">🔴 Tràn bộ nhớ (OOM)! Cần máy trạm HPC hoặc Siêu máy tính</b>
        `;
      }
    }
  }
  window.updateRamCalc = updateRamCalc;

  // ═════════════════════════════════════════════════════════════════════════
  // TAB NAVIGATION & BOOTSTRAP
  // ═════════════════════════════════════════════════════════════════════════
  function switchPracticeTab(tabId) {
    document.querySelectorAll(".prac-tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".prac-pane").forEach(p => p.classList.remove("active"));

    const btn = document.getElementById(`tab-btn-${tabId}`);
    const pane = document.getElementById(`tab-pane-${tabId}`);
    if (btn) btn.classList.add("active");
    if (pane) pane.classList.add("active");

    sound(480, 'sine', 0.05);

    if (tabId === 'bloch') {
      if (window.initBlochExplorer) initBlochExplorer();
      if (window.resizeBlochCanvas) resizeBlochCanvas();
    }
    if (tabId === 'pairwise') renderPairwiseLab();
    if (tabId === 'grover') {
      if (window.initGroverExplorer) initGroverExplorer();
      if (window.resizeGroverCanvas) resizeGroverCanvas();
    }
    if (tabId === 'qec') renderQecUI();
    if (tabId === 'chsh') renderChshUI();

    try {
      if ((document.querySelector(".prac-tabs") || document.getElementById("ch-sidebar-list")) && window.history && window.history.replaceState) {
        if (tabId === "challenges") {
          window.history.replaceState(null, "", "#ch-" + (curChIndex + 1));
        } else {
          window.history.replaceState(null, "", "#" + tabId);
        }
      }
    } catch (e) {}
  }
  window.switchPracticeTab = switchPracticeTab;

  function handleHashNav() {
    if (!document.querySelector(".prac-tabs") && !document.getElementById("ch-sidebar-list")) return;
    const h = (window.location.hash || "").replace(/^#/, "");
    if (!h) return;
    if (["challenges", "bloch", "pairwise", "grover", "qec", "chsh"].includes(h)) {
      window.switchPracticeTab(h);
      return;
    }
    const m = /^ch-(\d+)$/.exec(h);
    if (m) {
      window.switchPracticeTab("challenges");
      const idx = parseInt(m[1], 10) - 1;
      if (idx >= 0 && idx < CHALLENGES.length) {
        window.selectChallenge(idx);
      }
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    loadProgress();
    if (document.getElementById("ch-sidebar-list")) {
      renderChallengeList();
      renderChallengeUI();
    }
    if (document.getElementById("canvas-bloch-interactive")) initBlochExplorer();
    if (document.getElementById("pairwise-lab-mount")) renderPairwiseLab();
    if (document.getElementById("canvas-grover-2d")) initGroverExplorer();
    if (document.getElementById("qec-lab-mount")) renderQecUI();
    if (document.getElementById("chsh-game-mount")) renderChshUI();
    if (document.getElementById("ram-slider") && window.updateRamCalc) {
      window.updateRamCalc(+document.getElementById("ram-slider").value);
    }
    handleHashNav();
  });

  window.addEventListener("hashchange", handleHashNav);
  window.handleHashNav = handleHashNav;

  window.QuantumPractice = {
    CHALLENGES,
    computeFidelity,
    selectChallenge,
    getCurChIndex: () => curChIndex,
    verifyChallenge,
    showChallengeHint,
    showChallengeSolution,
    loadChallengeSolution,
    gateToString,
    switchPracticeTab,
    handleHashNav
  };
})();
