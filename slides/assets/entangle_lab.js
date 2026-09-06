/* ═══════════════════════════════════════════════════════════════════════════
   Quantum Zero→Hero · Entanglement Interactive Laboratory Engine
   Tự lo toàn bộ logic mô phỏng, đồ họa canvas, âm thanh và mini quiz.
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  // Web Audio Synthesizer (optional pleasant feedback)
  let audioCtx = null;
  function playTone(freq = 440, type = 'sine', duration = 0.08) {
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = type;
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    } catch (e) {
      // Audio not supported or blocked
    }
  }

  // ── Tab Switching Logic ──────────────────────────────────────────────────
  window.switchElabTab = function (tabId) {
    const root = document.getElementById('entangle-lab');
    if (!root) return;

    root.querySelectorAll('.elab-pane').forEach(p => p.classList.remove('active'));
    root.querySelectorAll('.elab-tab-btn').forEach(b => b.classList.remove('active'));

    const pane = document.getElementById(`elab-pane-${tabId}`);
    const btn = document.getElementById(`elab-tab-${tabId}`);
    if (pane) pane.classList.add('active');
    if (btn) btn.classList.add('active');

    playTone(520, 'sine', 0.05);

    if (tabId === 'intuition' && window.resizeElabCanvas) {
      window.resizeElabCanvas();
    }
    if (tabId === 'teleport' && window.renderTeleCanvas) {
      window.renderTeleCanvas();
    }
  };

  // ── Tab 1: Intuition Live Canvas ─────────────────────────────────────────
  let canvasIntuit, ctxIntuit;
  let intuitAngle = 0;
  let intuitMeasured = false;
  let intuitVal = null;
  let animIdIntuit = null;

  function initIntuition() {
    canvasIntuit = document.getElementById('canvas-elab-intuition');
    if (!canvasIntuit) return;
    ctxIntuit = canvasIntuit.getContext('2d');

    window.resizeElabCanvas = function () {
      if (!canvasIntuit || !canvasIntuit.parentElement) return;
      const rect = canvasIntuit.parentElement.getBoundingClientRect();
      canvasIntuit.width = rect.width;
      canvasIntuit.height = 190;
    };

    window.resizeElabCanvas();
    window.addEventListener('resize', window.resizeElabCanvas);
    animLoopIntuition();
  }

  function animLoopIntuition() {
    if (!ctxIntuit) return;
    const w = canvasIntuit.width;
    const h = canvasIntuit.height;
    ctxIntuit.clearRect(0, 0, w, h);

    // Subtle background grid
    ctxIntuit.strokeStyle = 'rgba(255, 255, 255, 0.04)';
    ctxIntuit.lineWidth = 1;
    for (let x = 0; x < w; x += 28) {
      ctxIntuit.beginPath();
      ctxIntuit.moveTo(x, 0);
      ctxIntuit.lineTo(x, h);
      ctxIntuit.stroke();
    }

    const ax = w * 0.22;
    const bx = w * 0.78;
    const cy = h * 0.48;

    // Entanglement bridge wave
    ctxIntuit.beginPath();
    ctxIntuit.strokeStyle = intuitMeasured ? 'rgba(74, 222, 128, 0.7)' : 'rgba(94, 234, 212, 0.65)';
    ctxIntuit.lineWidth = intuitMeasured ? 2.5 : 2;
    for (let x = ax; x <= bx; x += 4) {
      const p = (x - ax) / (bx - ax);
      const wave = Math.sin(p * Math.PI * 4 - intuitAngle * 2.2) * (intuitMeasured ? 3 : 10);
      if (x === ax) ctxIntuit.moveTo(x, cy + wave);
      else ctxIntuit.lineTo(x, cy + wave);
    }
    ctxIntuit.stroke();

    // Draw Particles
    drawNode(ctxIntuit, ax, cy, 'An (Qubit 0)', intuitMeasured, intuitVal, intuitAngle, '#5eead4');
    drawNode(ctxIntuit, bx, cy, 'Bình (Qubit 1)', intuitMeasured, intuitVal, intuitAngle, '#818cf8');

    if (!intuitMeasured) {
      intuitAngle += 0.045;
    }
    animIdIntuit = requestAnimationFrame(animLoopIntuition);
  }

  function drawNode(ctx, x, y, label, isMeasured, val, angle, color) {
    ctx.save();
    // Halo
    ctx.beginPath();
    ctx.arc(x, y, 36, 0, Math.PI * 2);
    ctx.fillStyle = isMeasured ? 'rgba(74, 222, 128, 0.08)' : 'rgba(94, 234, 212, 0.08)';
    ctx.fill();

    // Orbit Ring
    ctx.beginPath();
    ctx.arc(x, y, 26, 0, Math.PI * 2);
    ctx.strokeStyle = isMeasured ? '#4ade80' : color;
    ctx.lineWidth = 1.5;
    if (!isMeasured) ctx.setLineDash([3, 3]);
    ctx.stroke();
    ctx.setLineDash([]);

    if (!isMeasured) {
      const ox = x + Math.cos(angle) * 16;
      const oy = y + Math.sin(angle) * 16;
      ctx.beginPath();
      ctx.arc(ox, oy, 5, 0, Math.PI * 2);
      ctx.fillStyle = '#38bdf8';
      ctx.fill();

      ctx.fillStyle = '#a7b0c4';
      ctx.font = 'bold 11px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.fillText('|?⟩', x, y + 4);
    } else {
      ctx.beginPath();
      ctx.arc(x, y, 14, 0, Math.PI * 2);
      ctx.fillStyle = val === 1 ? '#5eead4' : '#c4a2ff';
      ctx.fill();

      ctx.fillStyle = '#070912';
      ctx.font = 'bold 12px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.fillText(`|${val}⟩`, x, y + 4.5);
    }

    ctx.fillStyle = '#e8ecf4';
    ctx.font = '600 11px -apple-system, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(label, x, y + 48);
    ctx.restore();
  }

  window.measureIntuition = function (by) {
    if (intuitMeasured) return;
    playTone(680, 'triangle', 0.12);
    intuitMeasured = true;
    intuitVal = Math.random() > 0.5 ? 1 : 0;

    const bAn = document.getElementById('elab-an-state');
    const bBinh = document.getElementById('elab-binh-state');
    if (bAn) {
      bAn.innerText = `Đo ra |${intuitVal}⟩`;
      bAn.className = 'elab-badge success';
    }
    if (bBinh) {
      bBinh.innerText = `Tức thì ra |${intuitVal}⟩`;
      bBinh.className = 'elab-badge success';
    }

    const btnA = document.getElementById('btn-elab-meas-an');
    const btnB = document.getElementById('btn-elab-meas-binh');
    if (btnA) btnA.disabled = true;
    if (btnB) btnB.disabled = true;

    const res = document.getElementById('elab-intuit-result');
    if (res) res.classList.remove('hidden');
  };

  window.resetIntuition = function () {
    intuitMeasured = false;
    intuitVal = null;
    const bAn = document.getElementById('elab-an-state');
    const bBinh = document.getElementById('elab-binh-state');
    if (bAn) {
      bAn.innerText = 'Chồng chập |?⟩';
      bAn.className = 'elab-badge';
    }
    if (bBinh) {
      bBinh.innerText = 'Chồng chập |?⟩';
      bBinh.className = 'elab-badge';
    }

    const btnA = document.getElementById('btn-elab-meas-an');
    const btnB = document.getElementById('btn-elab-meas-binh');
    if (btnA) btnA.disabled = false;
    if (btnB) btnB.disabled = false;

    const res = document.getElementById('elab-intuit-result');
    if (res) res.classList.add('hidden');
    playTone(320, 'sine', 0.08);
  };

  // ── Tab 2: No-Signaling Simulator ────────────────────────────────────────
  let noSigPattern = '1011';
  let isNoSigBusy = false;

  window.setNoSigPattern = function (pat) {
    if (isNoSigBusy) return;
    noSigPattern = pat;
    document.querySelectorAll('.elab-pill-nosig').forEach(b => {
      if (b.innerText === pat) b.classList.add('active');
      else b.classList.remove('active');
    });
    renderNoSigGrid();
    const exp = document.getElementById('elab-nosig-exp');
    if (exp) exp.classList.add('hidden');
  };

  function renderNoSigGrid() {
    const bits = noSigPattern.split('');
    const aTarget = document.getElementById('elab-ns-target');
    const aMeas = document.getElementById('elab-ns-an-meas');
    const bMeas = document.getElementById('elab-ns-binh-meas');

    if (aTarget) {
      aTarget.innerHTML = bits.map((b, i) => `
        <div class="elab-bit-row">
          <span style="color:var(--text-3)">Bit #${i+1}:</span>
          <b style="color:var(--rose)">Muốn gửi: ${b}</b>
        </div>
      `).join('');
    }

    if (aMeas) {
      aMeas.innerHTML = bits.map((_, i) => `
        <div id="elab-ns-a-${i}" class="elab-bit-row">
          <span style="color:var(--text-3)">Đo hạt #${i+1}:</span>
          <span style="color:var(--text-3);font-style:italic">Chưa đo</span>
        </div>
      `).join('');
    }

    if (bMeas) {
      bMeas.innerHTML = bits.map((_, i) => `
        <div id="elab-ns-b-${i}" class="elab-bit-row">
          <span style="color:var(--text-3)">Bình thấy:</span>
          <span style="color:var(--text-3);font-style:italic">Chưa đo</span>
        </div>
      `).join('');
    }
  }

  window.runNoSigSim = function () {
    if (isNoSigBusy) return;
    isNoSigBusy = true;
    const btn = document.getElementById('btn-run-nosig');
    if (btn) btn.disabled = true;
    const exp = document.getElementById('elab-nosig-exp');
    if (exp) exp.classList.add('hidden');

    const bits = noSigPattern.split('');
    let step = 0;

    const timer = setInterval(() => {
      if (step >= bits.length) {
        clearInterval(timer);
        isNoSigBusy = false;
        if (btn) btn.disabled = false;
        if (exp) exp.classList.remove('hidden');
        playTone(300, 'sawtooth', 0.2);
        return;
      }

      playTone(450 + step * 65, 'sine', 0.08);
      const randOutcome = Math.random() > 0.5 ? '1' : '0';

      const elA = document.getElementById(`elab-ns-a-${step}`);
      if (elA) {
        elA.innerHTML = `
          <span style="color:var(--text-3)">Đo hạt #${step+1}:</span>
          <b style="color:var(--amber)">Đo ra: ${randOutcome}</b>
        `;
      }

      const elB = document.getElementById(`elab-ns-b-${step}`);
      if (elB) {
        elB.innerHTML = `
          <span style="color:var(--text-3)">Bình thấy:</span>
          <b style="color:var(--cyan)">Nhận: ${randOutcome}</b>
        `;
      }

      step++;
    }, 450);
  };

  // ── Tab 3: Quantum Teleportation (Dịch Chuyển Lượng Tử) ────────────────
  const teleSteps = [
    {
      title: 'Bước 0: Có một "Viên Ngọc Bí Mật" |ψ⟩',
      desc: 'An đang giữ một trạng thái lượng tử bí mật (ví dụ viên ngọc phát sáng). Vật lý cấm nhìn trộm (sẽ làm hỏng ngọc) và cấm sao chép nhân bản.',
      btn: 'Chuẩn Bị Cặp Vướng Víu Liên Kết'
    },
    {
      title: 'Bước 1: Chia nhau 2 hạt Vướng Víu',
      desc: 'Nguồn lượng tử tạo ra 2 hạt liên kết thần kỳ (Bell Pair): An giữ Hạt 1, Bình giữ Hạt 2 ở Sao Hỏa.',
      btn: 'An Tiến Hành Đo Lượng Tử'
    },
    {
      title: 'Bước 2: Đo & Hủy bản gốc (No-Cloning)',
      desc: 'An cho Viên Ngọc bí mật tương tác với Hạt 1 rồi đo. Viên ngọc gốc bị vỡ vụn (hủy bản gốc), chỉ còn lại đúng 2 con số bí mật (ví dụ: "10").',
      btn: 'Gửi 2 Số Qua Tin Nhắn Điện Thoại'
    },
    {
      title: 'Bước 3: Nhắn tin 2 bit với tốc độ ánh sáng',
      desc: 'An nhắn tin qua sóng vô tuyến/cáp quang: "Bình ơi, mã số là 10 nhé!". Thông điệp này bay với tốc độ ánh sáng thông thường.',
      btn: 'Bình Nhận Mã & Biến Hình Hạt 2'
    },
    {
      title: 'Bước 4: Tái sinh Viên Ngọc ở Trạm Bình',
      desc: 'Bình nhận được mã "10", liền xoay Hạt 2 có sẵn theo đúng hướng dẫn. KỲ DIỆU THAY: Hạt 2 biến thành chính xác Viên Ngọc bí mật ban đầu!',
      btn: 'Hoàn Tất Dịch Chuyển'
    }
  ];

  let curTeleStep = 0;
  let teleBitsVal = '10';
  let canvasTele, ctxTele;
  let teleAnimAngle = 0;
  let teleAnimTimer = null;

  function initTeleport() {
    canvasTele = document.getElementById('canvas-elab-teleport');
    if (canvasTele) {
      ctxTele = canvasTele.getContext('2d');
    }
    renderTeleStepper();
    if (!teleAnimTimer) {
      teleAnimLoop();
    }
  }

  function teleAnimLoop() {
    teleAnimAngle += 0.04;
    window.renderTeleCanvas();
    requestAnimationFrame(teleAnimLoop);
  }

  window.renderTeleCanvas = function () {
    if (!canvasTele) {
      canvasTele = document.getElementById('canvas-elab-teleport');
      if (canvasTele) ctxTele = canvasTele.getContext('2d');
      else return;
    }
    const rect = canvasTele.parentElement.getBoundingClientRect();
    canvasTele.width = rect.width;
    canvasTele.height = 175;
    const w = canvasTele.width;
    const h = canvasTele.height;
    ctxTele.clearRect(0, 0, w, h);

    const ax = w * 0.22;
    const bx = w * 0.78;
    const my = h * 0.5;

    // Station bases
    ctxTele.save();
    ctxTele.fillStyle = 'rgba(94, 234, 212, 0.06)';
    ctxTele.strokeStyle = 'rgba(94, 234, 212, 0.4)';
    ctxTele.lineWidth = 1.5;
    ctxTele.beginPath();
    ctxTele.roundRect(ax - 55, my - 54, 110, 108, 12);
    ctxTele.fill();
    ctxTele.stroke();

    ctxTele.fillStyle = 'rgba(129, 140, 248, 0.06)';
    ctxTele.strokeStyle = 'rgba(129, 140, 248, 0.4)';
    ctxTele.beginPath();
    ctxTele.roundRect(bx - 55, my - 54, 110, 108, 12);
    ctxTele.fill();
    ctxTele.stroke();

    // Station Labels
    ctxTele.fillStyle = '#5eead4';
    ctxTele.font = 'bold 12px -apple-system, sans-serif';
    ctxTele.textAlign = 'center';
    ctxTele.fillText('Trạm An (Trái Đất)', ax, my - 62);
    ctxTele.fillStyle = '#818cf8';
    ctxTele.fillText('Trạm Bình (Sao Hỏa)', bx, my - 62);

    // 1. Entanglement link line
    ctxTele.beginPath();
    ctxTele.strokeStyle = curTeleStep >= 1 ? 'rgba(196, 162, 255, 0.7)' : 'rgba(255, 255, 255, 0.1)';
    ctxTele.lineWidth = curTeleStep >= 1 ? 2.2 : 1;
    if (curTeleStep >= 1) {
      ctxTele.setLineDash([5, 4]);
    }
    ctxTele.moveTo(ax + 55, my - 16);
    ctxTele.lineTo(bx - 55, my - 16);
    ctxTele.stroke();
    ctxTele.setLineDash([]);

    if (curTeleStep >= 1) {
      ctxTele.fillStyle = '#c4a2ff';
      ctxTele.font = '10px "JetBrains Mono", monospace';
      ctxTele.fillText('Dây liên kết vướng víu (Bell Link)', (ax + bx) / 2, my - 24);
    }

    // 2. Classical channel (Internet / Radio)
    ctxTele.beginPath();
    ctxTele.strokeStyle = curTeleStep >= 3 ? '#fbbf24' : 'rgba(255, 255, 255, 0.08)';
    ctxTele.lineWidth = curTeleStep >= 3 ? 2.5 : 1;
    ctxTele.moveTo(ax + 55, my + 22);
    ctxTele.lineTo(bx - 55, my + 22);
    ctxTele.stroke();

    if (curTeleStep >= 3) {
      const p = Math.min(1, Math.max(0, (teleAnimAngle % 2)));
      const envX = (ax + 55) + ((bx - 55) - (ax + 55)) * (curTeleStep === 3 ? 0.5 : 1);
      ctxTele.fillStyle = '#fbbf24';
      ctxTele.beginPath();
      ctxTele.arc(envX, my + 22, 6, 0, Math.PI * 2);
      ctxTele.fill();
      ctxTele.font = 'bold 11px "JetBrains Mono", monospace';
      ctxTele.fillText(`✉️ Tin nhắn: "${teleBitsVal}" (tốc độ ánh sáng c)`, (ax + bx) / 2, my + 40);
    }

    // Draw Particles in Stations
    // An's Secret Gem
    if (curTeleStep === 0) {
      drawGlowingGem(ctxTele, ax, my - 16, '#5eead4', 'Ngọc |ψ⟩', teleAnimAngle);
    } else if (curTeleStep === 1) {
      drawGlowingGem(ctxTele, ax - 25, my - 16, '#5eead4', 'Ngọc |ψ⟩', teleAnimAngle);
      drawGlowingGem(ctxTele, ax + 25, my - 16, '#c4a2ff', 'Hạt 1', teleAnimAngle);
    } else {
      // Destroyed / measured
      ctxTele.fillStyle = '#fb7185';
      ctxTele.font = 'bold 11px -apple-system, sans-serif';
      ctxTele.fillText('💥 Bản gốc bị hủy', ax, my - 16);
      ctxTele.fillStyle = '#fbbf24';
      ctxTele.font = 'bold 13px "JetBrains Mono", monospace';
      ctxTele.fillText(`Mã đo: [${teleBitsVal}]`, ax, my + 14);
    }

    // Binh's Entangled Particle (Step 1 to 3)
    if (curTeleStep >= 1 && curTeleStep < 4) {
      drawGlowingGem(ctxTele, bx, my - 16, '#c4a2ff', 'Hạt 2 (Chờ mã)', teleAnimAngle);
    } else if (curTeleStep === 4) {
      // Reconstructed Secret Gem at Binh's station!
      drawGlowingGem(ctxTele, bx, my - 16, '#5eead4', '✨ Ngọc Tái Sinh', teleAnimAngle);
    } else {
      ctxTele.fillStyle = '#6f7a92';
      ctxTele.font = '11px -apple-system, sans-serif';
      ctxTele.fillText('Chưa có hạt', bx, my - 12);
    }

    ctxTele.restore();
  };

  function drawGlowingGem(ctx, x, y, color, label, angle) {
    ctx.save();
    // Halo glow
    ctx.beginPath();
    ctx.arc(x, y, 16 + Math.sin(angle * 3) * 2, 0, Math.PI * 2);
    ctx.fillStyle = color === '#5eead4' ? 'rgba(94, 234, 212, 0.25)' : 'rgba(196, 162, 255, 0.25)';
    ctx.fill();

    // Core
    ctx.beginPath();
    ctx.arc(x, y, 9, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();

    // Label
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 10px -apple-system, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(label, x, y + 24);
    ctx.restore();
  }

  function renderTeleStepper() {
    const box = document.getElementById('elab-tele-stepper');
    if (!box) return;
    box.innerHTML = teleSteps.map((s, idx) => `
      <div id="elab-ts-${idx}" class="elab-step-item ${idx === 0 ? 'active' : ''}">
        <span style="font-size:0.68rem;opacity:0.7;display:block">BƯỚC ${idx}</span>
        ${s.title.split(':')[1] || s.title}
      </div>
    `).join('');
  }

  window.nextTeleStep = function () {
    if (curTeleStep >= teleSteps.length - 1) return;
    curTeleStep++;
    playTone(520 + curTeleStep * 75, 'sine', 0.1);

    if (curTeleStep === 2) {
      const outcomes = ['00', '01', '10', '11'];
      teleBitsVal = outcomes[Math.floor(Math.random() * outcomes.length)];
      const aQ = document.getElementById('elab-tele-an-q');
      const aB = document.getElementById('elab-tele-an-bits');
      if (aQ) aQ.innerHTML = '<span style="color:var(--rose);font-weight:bold">💥 Bị hủy (No-Cloning)</span>';
      if (aB) aB.innerText = `Mã: ${teleBitsVal}`;
    }

    if (curTeleStep === 3) {
      const chan = document.getElementById('elab-tele-chan-status');
      if (chan) chan.innerHTML = `<b style="color:var(--amber)">Đang gửi tin nhắn "${teleBitsVal}" qua điện thoại...</b>`;
    }

    if (curTeleStep === 4) {
      const bQ = document.getElementById('elab-tele-binh-q');
      const bS = document.getElementById('elab-tele-binh-status');
      if (bQ) bQ.innerHTML = '<b style="color:var(--cyan)">✨ Tái sinh đúng Viên Ngọc |ψ⟩!</b>';
      if (bS) bS.innerHTML = '<b style="color:var(--green)">✓ Thành công: Bình đã có viên ngọc y hệt bản gốc!</b>';
      const btnN = document.getElementById('btn-tele-next');
      if (btnN) btnN.style.display = 'none';
    }

    const tTitle = document.getElementById('elab-tele-title');
    const tDesc = document.getElementById('elab-tele-desc');
    const btnN = document.getElementById('btn-tele-next');
    if (tTitle) tTitle.innerText = teleSteps[curTeleStep].title;
    if (tDesc) tDesc.innerText = teleSteps[curTeleStep].desc;
    if (btnN && curTeleStep < teleSteps.length - 1) {
      btnN.innerText = teleSteps[curTeleStep].btn + ' →';
    }

    for (let i = 0; i < teleSteps.length; i++) {
      const el = document.getElementById(`elab-ts-${i}`);
      if (el) {
        if (i === curTeleStep) el.className = 'elab-step-item active';
        else if (i < curTeleStep) el.className = 'elab-step-item done';
        else el.className = 'elab-step-item';
      }
    }
  };

  window.resetTeleport = function () {
    curTeleStep = 0;
    teleBitsVal = '10';
    const aQ = document.getElementById('elab-tele-an-q');
    const aB = document.getElementById('elab-tele-an-bits');
    const bQ = document.getElementById('elab-tele-binh-q');
    const bS = document.getElementById('elab-tele-binh-status');
    const chan = document.getElementById('elab-tele-chan-status');
    const btnN = document.getElementById('btn-tele-next');

    if (aQ) aQ.innerText = 'Viên Ngọc Bí Mật |ψ⟩';
    if (aB) aB.innerText = '--';
    if (bQ) bQ.innerText = 'Chưa có hạt';
    if (bS) bS.innerText = 'Chờ tin nhắn 2 con số của An để biến hình...';
    if (chan) chan.innerText = 'Chờ gửi tin nhắn...';
    if (btnN) {
      btnN.style.display = 'inline-flex';
      btnN.innerText = teleSteps[0].btn + ' →';
    }

    const tTitle = document.getElementById('elab-tele-title');
    const tDesc = document.getElementById('elab-tele-desc');
    if (tTitle) tTitle.innerText = teleSteps[0].title;
    if (tDesc) tDesc.innerText = teleSteps[0].desc;

    renderTeleStepper();
    playTone(320, 'sine', 0.08);
  };

  // ── Tab 4: Superdense Coding ─────────────────────────────────────────────
  const denseDict = {
    '00': { gate: 'I (Không đổi)', desc: 'Giữ nguyên trạng thái Bell |Φ⁺⟩' },
    '01': { gate: 'Z (Đổi Pha)', desc: 'Đổi dấu pha tạo thành trạng thái |Φ⁻⟩' },
    '10': { gate: 'X (Đảo Bit)', desc: 'Đảo bit 0↔1 tạo thành trạng thái |Ψ⁺⟩' },
    '11': { gate: 'XZ (Cả 2 Cổng)', desc: 'Đảo bit và đổi pha tạo thành trạng thái |Ψ⁻⟩' }
  };
  let curDenseBits = '00';

  window.selectDenseBits = function (bits) {
    curDenseBits = bits;
    document.querySelectorAll('.dense-sel-btn').forEach(b => {
      if (b.innerText === bits) b.classList.add('active');
      else b.classList.remove('active');
    });

    const gName = document.getElementById('elab-dense-gate');
    const gDesc = document.getElementById('elab-dense-gate-desc');
    const dec = document.getElementById('elab-dense-decoded');
    const badge = document.getElementById('elab-dense-badge');
    const fly = document.getElementById('elab-dense-particle');
    const stat = document.getElementById('elab-dense-flight-stat');

    if (gName) gName.innerText = denseDict[bits].gate;
    if (gDesc) gDesc.innerText = denseDict[bits].desc;
    if (dec) dec.innerText = '??';
    if (badge) badge.classList.add('hidden');
    if (fly) fly.style.transform = 'translate(0px, -50%)';
    if (stat) stat.innerText = 'Sẵn sàng truyền 1 qubit';

    playTone(460, 'sine', 0.05);
  };

  window.sendDenseQubit = function () {
    const fly = document.getElementById('elab-dense-particle');
    const stat = document.getElementById('elab-dense-flight-stat');
    const dec = document.getElementById('elab-dense-decoded');
    const badge = document.getElementById('elab-dense-badge');
    const btn = document.getElementById('btn-dense-send');

    if (fly) fly.style.transform = 'translate(140px, -50%)';
    if (stat) stat.innerText = 'Qubit đang bay qua không gian...';
    if (btn) btn.disabled = true;
    playTone(600, 'triangle', 0.1);

    setTimeout(() => {
      if (stat) stat.innerText = 'Bình đã nhận được qubit!';
      if (dec) dec.innerText = curDenseBits;
      if (badge) badge.classList.remove('hidden');
      if (btn) btn.disabled = false;
      playTone(880, 'sine', 0.15);
    }, 900);
  };

  // ── Tab 5: Mini Quiz ─────────────────────────────────────────────────────
  const quizItems = [
    {
      id: 1,
      q: 'Tại sao KHÔNG THỂ dùng vướng víu lượng tử để gửi tin tức thì nhanh hơn ánh sáng?',
      opts: [
        { id: 'a', t: 'Vì khi đo hạt, kết quả luôn ngẫu nhiên 50/50, người gửi không thể tự ý ép hạt ra bit mong muốn.', c: true },
        { id: 'b', t: 'Vì photon vướng víu di chuyển chậm hơn ánh sáng trong môi trường cáp quang.', c: false },
        { id: 'c', t: 'Vì sóng lượng tử bị hấp thụ bởi khí quyển.', c: false }
      ],
      exp: 'Chính xác! Do tính ngẫu nhiên lượng tử bản thể, người nhận ở xa chỉ thấy một chuỗi số ngẫu nhiên 50/50 vô nghĩa nếu không có thông tin cổ điển đối chiếu.'
    },
    {
      id: 2,
      q: 'Để thực hiện Dịch chuyển lượng tử (Teleportation) 1 Qubit, bạn bắt buộc cần tài nguyên gì?',
      opts: [
        { id: 'a', t: 'Chỉ cần 1 cặp vướng víu lượng tử là đủ.', c: false },
        { id: 'b', t: '1 cặp vướng víu + 2 bit thông tin cổ điển (gửi qua internet/radio).', c: true },
        { id: 'c', t: 'Không cần gửi gì cả, hạt tự biến mất và xuất hiện lại.', c: false }
      ],
      exp: 'Chính xác! Công thức vàng: 1 Cặp Entanglement + 2 Bit Cổ Điển = Truyền 1 Trạng Thái Qubit.'
    },
    {
      id: 3,
      q: 'Khi thực hiện Teleportation, trạng thái qubit gốc ở phía người gửi (An) sẽ ra sao?',
      opts: [
        { id: 'a', t: 'Vẫn còn nguyên, ta vừa nhân bản được một qubit thứ hai giống hệt.', c: false },
        { id: 'b', t: 'Bị phá hủy hoàn toàn trong quá trình đo (Định lý Không-Sao-Chép No-Cloning).', c: true },
        { id: 'c', t: 'Tự động biến thành bit 0.', c: false }
      ],
      exp: 'Chính xác! Định lý Không-Sao-Chép (No-Cloning Theorem) cấm tuyệt đối việc nhân bản một trạng thái lượng tử chưa biết.'
    }
  ];

  let quizAnswers = {};

  function initQuiz() {
    const box = document.getElementById('elab-quiz-box');
    if (!box) return;
    box.innerHTML = quizItems.map((q, idx) => `
      <div class="elab-quiz-q">
        <div class="elab-quiz-title">Câu ${idx + 1}: ${q.q}</div>
        <div style="display:grid;gap:0.4rem">
          ${q.opts.map(o => `
            <button onclick="pickQuizOpt(${q.id}, '${o.id}')" id="elab-q-${q.id}-opt-${o.id}" class="elab-quiz-opt">
              <b style="color:var(--cyan);font-family:var(--mono);text-transform:uppercase">${o.id}.</b>
              <span>${o.t}</span>
            </button>
          `).join('')}
        </div>
        <div id="elab-quiz-exp-${q.id}" class="elab-quiz-exp" style="display:none">
          💡 <b>Giải thích:</b> ${q.exp}
        </div>
      </div>
    `).join('');
  }

  window.pickQuizOpt = function (qId, optId) {
    quizAnswers[qId] = optId;
    const q = quizItems.find(item => item.id === qId);
    q.opts.forEach(opt => {
      const btn = document.getElementById(`elab-q-${qId}-opt-${opt.id}`);
      if (btn) {
        if (opt.id === optId) btn.classList.add('selected');
        else btn.classList.remove('selected');
      }
    });
    playTone(480, 'sine', 0.05);
  };

  window.submitQuiz = function () {
    if (Object.keys(quizAnswers).length < quizItems.length) {
      alert('Vui lòng chọn câu trả lời cho cả 3 câu trước khi nộp bài!');
      return;
    }

    let score = 0;
    quizItems.forEach(q => {
      const selected = quizAnswers[q.id];
      const correctOpt = q.opts.find(o => o.c);
      const expBox = document.getElementById(`elab-quiz-exp-${q.id}`);
      if (expBox) expBox.style.display = 'block';

      q.opts.forEach(opt => {
        const btn = document.getElementById(`elab-q-${q.id}-opt-${opt.id}`);
        if (!btn) return;
        btn.classList.remove('selected');
        if (opt.c) {
          btn.className = 'elab-quiz-opt correct';
        } else if (opt.id === selected && !opt.c) {
          btn.className = 'elab-quiz-opt wrong';
        }
      });

      if (selected === correctOpt.id) score++;
    });

    const badge = document.getElementById('elab-quiz-score');
    if (badge) {
      badge.innerText = `Điểm: ${score} / ${quizItems.length}`;
      badge.classList.remove('hidden');
    }

    const btnSub = document.getElementById('btn-quiz-sub');
    const btnRes = document.getElementById('btn-quiz-res');
    if (btnSub) btnSub.classList.add('hidden');
    if (btnRes) btnRes.classList.remove('hidden');
    playTone(score === 3 ? 880 : 500, 'triangle', 0.2);
  };

  window.resetQuiz = function () {
    quizAnswers = {};
    initQuiz();
    const badge = document.getElementById('elab-quiz-score');
    const btnSub = document.getElementById('btn-quiz-sub');
    const btnRes = document.getElementById('btn-quiz-res');
    if (badge) badge.classList.add('hidden');
    if (btnSub) btnSub.classList.remove('hidden');
    if (btnRes) btnRes.classList.add('hidden');
    playTone(320, 'sine', 0.08);
  };

  // ── Auto Initialization ──────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', () => {
    initIntuition();
    renderNoSigGrid();
    initTeleport();
    initQuiz();
  });
})();
