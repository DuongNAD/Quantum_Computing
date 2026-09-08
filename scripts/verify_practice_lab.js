/**
 * Automated Verification Script for Quantum Zero→Hero Practice Lab
 * 
 * Verifies:
 *  1. All 12 Challenge solutions solve the challenge with Fidelity >= 99.9%
 *  2. Empty circuits are rejected immediately (False-Pass prevention for Ch 7 & all)
 *  3. Edge-case / False-Pass prevention validators for Ch 7, 8, 9, 10, 11, 12
 *  4. Tab switching across all 6 modules
 *  5. HTML file links and references consistency
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log("==================================================================");
console.log("  Quantum Zero→Hero · Practice Lab Automated Verification Suite   ");
console.log("==================================================================\n");

// ── 1. Create Browser / DOM Mock Environment ───────────────────────────────
const elements = new Map();

function createMockElement(id, tagName = 'div') {
  const el = {
    id,
    tagName: tagName.toUpperCase(),
    className: '',
    style: {},
    innerText: '',
    innerHTML: '',
    children: [],
    dataset: {},
    classList: {
      _classes: new Set(),
      add: (c) => el.classList._classes.add(c),
      remove: (c) => el.classList._classes.delete(c),
      contains: (c) => el.classList._classes.has(c),
      toggle: (c, force) => {
        if (force === undefined) {
          if (el.classList.contains(c)) el.classList.remove(c);
          else el.classList.add(c);
        } else if (force) {
          el.classList.add(c);
        } else {
          el.classList.remove(c);
        }
      }
    },
    addEventListener: () => {},
    removeEventListener: () => {},
    appendChild: (child) => el.children.push(child),
    getAttribute: (attr) => el[attr] || null,
    setAttribute: (attr, val) => { el[attr] = val; },
    querySelectorAll: (sel) => {
      const res = [];
      for (const e of elements.values()) {
        if (sel.startsWith('.') && e.className && e.className.includes(sel.slice(1))) res.push(e);
        if (sel.startsWith('#') && e.id === sel.slice(1)) res.push(e);
      }
      return res;
    },
    querySelector: (sel) => el.querySelectorAll(sel)[0] || null,
    getContext: () => ({
      clearRect: () => {},
      beginPath: () => {},
      arc: () => {},
      fill: () => {},
      stroke: () => {},
      moveTo: () => {},
      lineTo: () => {},
      fillText: () => {},
      setLineDash: () => {},
      measureText: () => ({ width: 10 })
    })
  };
  elements.set(id, el);
  return el;
}

// Pre-create standard UI elements used by practice_lab.js
createMockElement('ch-sidebar-list');
createMockElement('ch-completed-count');
createMockElement('ch-cur-title');
createMockElement('ch-cur-desc');
createMockElement('ch-cur-target');
createMockElement('ch-hint-box');
createMockElement('ch-result-status');
createMockElement('ch-fidelity-meter');
createMockElement('ch-fidelity-val');
createMockElement('ch-qlab-mount');
createMockElement('canvas-bloch-interactive');
createMockElement('pairwise-lab-mount');
createMockElement('canvas-grover-2d');
createMockElement('qec-lab-mount');
createMockElement('chsh-game-mount');
createMockElement('ram-slider');

// Tab bar container
const pracTabsEl = createMockElement('prac-tabs-bar', 'div');
pracTabsEl.className = 'prac-tabs';

// Tab buttons & panes
['challenges', 'bloch', 'pairwise', 'grover', 'qec', 'chsh'].forEach(t => {
  createMockElement(`tab-btn-${t}`);
  createMockElement(`tab-pane-${t}`);
});

const mockLocalStorage = {
  data: {},
  getItem: (k) => mockLocalStorage.data[k] || null,
  setItem: (k, v) => { mockLocalStorage.data[k] = String(v); },
  removeItem: (k) => { delete mockLocalStorage.data[k]; },
  clear: () => { mockLocalStorage.data = {}; }
};

const domWindow = {
  localStorage: mockLocalStorage,
  addEventListener: () => {},
  removeEventListener: () => {},
  location: { hash: '' },
  AudioContext: function () {
    return {
      state: 'running',
      currentTime: 0,
      createOscillator: () => ({
        type: 'sine',
        frequency: { value: 440 },
        connect: () => {},
        start: () => {},
        stop: () => {}
      }),
      createGain: () => ({
        gain: { setValueAtTime: () => {}, exponentialRampToValueAtTime: () => {} },
        connect: () => {}
      }),
      destination: {}
    };
  },
  Math: Math,
  Float64Array: Float64Array,
  Int32Array: Int32Array,
  parseInt: parseInt,
  parseFloat: parseFloat,
  setTimeout: (fn) => setTimeout(fn, 0)
};

const domDocument = {
  getElementById: (id) => elements.get(id) || null,
  querySelectorAll: (sel) => {
    const res = [];
    for (const e of elements.values()) {
      if (sel.startsWith('.') && e.className && e.className.includes(sel.slice(1))) res.push(e);
      if (sel.startsWith('#') && e.id === sel.slice(1)) res.push(e);
    }
    return res;
  },
  querySelector: (sel) => domDocument.querySelectorAll(sel)[0] || null,
  createElement: (tag, cls) => {
    const el = createMockElement('temp-' + Math.random(), tag);
    if (cls) el.className = cls;
    return el;
  },
  addEventListener: () => {}
};

domWindow.document = domDocument;
domWindow.window = domWindow;

const context = vm.createContext(domWindow);

// Load qlab.js & practice_lab.js
const qlabCode = fs.readFileSync(path.join(__dirname, '../slides/assets/qlab.js'), 'utf8');
const practiceCode = fs.readFileSync(path.join(__dirname, '../slides/assets/practice_lab.js'), 'utf8');

vm.runInContext(qlabCode, context);
vm.runInContext(practiceCode, context);

const QLab = domWindow.QLab;
const QP = domWindow.QuantumPractice;
const CHALLENGES = QP.CHALLENGES;

let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  if (condition) {
    passedTests++;
    console.log(`  ✓ ${message}`);
  } else {
    failedTests++;
    console.error(`  ✗ FAIL: ${message}`);
  }
}

// ── Test Suite 1: Challenge Structure & Solution Verification ───────────────
console.log("\n[1] Kiểm Tra 12 Mini-Katas và Lời Giải Mẫu:");
assert(CHALLENGES.length === 12, "Có đúng 12 thử thách trong danh sách CHALLENGES");

CHALLENGES.forEach((ch, idx) => {
  assert(ch.id === idx + 1, `Bài ${ch.id}: id khớp với chỉ số (${ch.id})`);
  assert(typeof ch.expected === 'function', `Bài ${ch.id}: expected() là function tạo trạng thái đích`);
  assert(typeof ch.solution === 'string' && ch.solution.length > 0, `Bài ${ch.id}: có chuỗi solution`);

  // Parse solution gates
  const solGates = QLab.parseGates(ch.solution);
  const solStrs = solGates.map(QP.gateToString);

  // Validate solution with custom validator if present
  if (typeof ch.validate === 'function') {
    // 1-argument invocation as required by specification
    const vRes1 = ch.validate(solGates);
    const isValid1 = typeof vRes1 === 'boolean' ? vRes1 : (vRes1 && vRes1.valid !== false);
    assert(isValid1, `Bài ${ch.id}: Lời giải mẫu chạy validate(gates) 1 tham số thành công`);

    const vRes = ch.validate(solGates, solStrs);
    const isValid = typeof vRes === 'boolean' ? vRes : (vRes && vRes.valid !== false);
    assert(isValid, `Bài ${ch.id}: Lời giải mẫu (${ch.solution}) vượt qua hàm validate()`);
  }

  // Simulate solution
  const state = QLab.Sim.run(ch.qubits, solGates);
  const target = ch.expected();
  const fidelity = QP.computeFidelity(state, target);
  assert(fidelity >= 0.999, `Bài ${ch.id} (${ch.title}): Lời giải mẫu đạt Fidelity = ${(fidelity * 100).toFixed(2)}% (>= 99.9%)`);
});

// ── Test Suite 2: Empty Circuit Rejection (False-Pass Prevention) ───────────
console.log("\n[2] Kiểm Tra Chống Gian Lận / Mạch Trống (False-Pass Prevention):");

// Mock setup for qlab widget inside verifyChallenge
function testVerifyChallengeWithGates(chIndex, gatesString) {
  domWindow.selectChallenge(chIndex);
  const qlabEl = elements.get('ch-qlab-instance') || createMockElement('ch-qlab-instance');
  qlabEl.setAttribute('data-current-gates', gatesString);
  qlabEl._qlab = {
    gates: QLab.parseGates(gatesString),
    n: CHALLENGES[chIndex].qubits
  };
  
  domWindow.verifyChallenge();
  
  const statusEl = elements.get('ch-result-status');
  const meterEl = elements.get('ch-fidelity-meter');
  const isFail = statusEl && statusEl.className.includes('fail');
  const isSuccess = statusEl && statusEl.className.includes('success');
  const meterPct = meterEl ? meterEl.style.width : '0%';
  
  return { isFail, isSuccess, meterPct, body: statusEl ? statusEl.innerHTML : '' };
}

// Challenge 7: H*H = I. Target is |0>, Initial is |0>.
// Empty circuit MUST FAIL with "MẠCH ĐANG TRỐNG"
const ch7EmptyRes = testVerifyChallengeWithGates(6, "");
assert(ch7EmptyRes.isFail, "Bài 7: Mạch trống bị từ chối (isFail = true)");
assert(!ch7EmptyRes.isSuccess, "Bài 7: Mạch trống KHÔNG được thông qua (isSuccess = false)");
assert(ch7EmptyRes.body.includes("MẠCH ĐANG TRỐNG"), "Bài 7: Mạch trống hiện thông báo rõ ràng 'MẠCH ĐANG TRỐNG'");
assert(ch7EmptyRes.meterPct === "0%", "Bài 7: Mạch trống đo điểm meter = 0%");

// Check all other challenges reject empty circuits
for (let i = 0; i < 12; i++) {
  const emptyRes = testVerifyChallengeWithGates(i, "");
  assert(emptyRes.isFail && !emptyRes.isSuccess, `Bài ${i + 1}: Mạch trống bị từ chối hoàn toàn`);
}

// ── Test Suite 3: Specific Validation Rules ────────────────────────────────
console.log("\n[3] Kiểm Tra Các Bộ Lọc Cấu Trúc Mạch (Custom Validators):");

// Challenge 6: Phase Kickback requires CX0-1 and H0 superposition/readout
const ch6CheatDirect = testVerifyChallengeWithGates(5, "X0, X1, H1");
assert(ch6CheatDirect.isFail, "Bài 6: Gian lận lật bit trực tiếp không dùng CNOT bị từ chối");
assert(ch6CheatDirect.body.includes("Phase Kickback hoàn chỉnh"), "Bài 6: Báo lỗi phải thiết lập mạch Phase Kickback hoàn chỉnh");

const ch6MissingH = testVerifyChallengeWithGates(5, "X0, CX0-1");
assert(ch6MissingH.isFail, "Bài 6: Thiếu Hadamard H0 tạo và đọc pha bị từ chối");

const ch6Correct = testVerifyChallengeWithGates(5, "H0, X1, H1, CX0-1, H0");
assert(ch6Correct.isSuccess, "Bài 6: Áp đúng H0, X1, H1, CX0-1, H0 đạt 100% và VƯỢT QUA");

// Challenge 7: Requires at least 2 Hadamard gates
const ch7SingleH = testVerifyChallengeWithGates(6, "H0");
assert(ch7SingleH.isFail, "Bài 7: Áp 1 cổng H0 bị từ chối");
assert(ch7SingleH.body.includes("yêu cầu áp dụng ít nhất 2 cổng Hadamard"), "Bài 7: Thông báo yêu cầu ít nhất 2 cổng H0");

const ch7WrongGates = testVerifyChallengeWithGates(6, "Z0, Z0");
assert(ch7WrongGates.isFail, "Bài 7: Áp Z0, Z0 (dù trạng thái về |0>) bị từ chối vì không dùng Hadamard");

const ch7Correct = testVerifyChallengeWithGates(6, "H0, H0");
assert(ch7Correct.isSuccess, "Bài 7: Áp đúng H0, H0 đạt 100% và VƯỢT QUA");

// Challenge 8: Must keep X0 and add 3 CNOTs
const ch8DeletedPreset = testVerifyChallengeWithGates(7, "X1");
assert(ch8DeletedPreset.isFail, "Bài 8: Xóa X0 và đặt X1 bị từ chối");
assert(ch8DeletedPreset.body.includes("giữ nguyên cổng khởi tạo X0"), "Bài 8: Báo lỗi phải giữ nguyên X0 khi xóa X0");

const ch8PresetAlone = testVerifyChallengeWithGates(7, "X0");
assert(ch8PresetAlone.isFail, "Bài 8: Chỉ có X0 mà chưa thêm 3 CNOT bị từ chối");
assert(ch8PresetAlone.body.includes("thêm đúng 3 cổng CNOT đan xen"), "Bài 8: Báo lỗi chính xác yêu cầu thêm 3 CNOT sau X0 (không báo sai xóa X0)");

const ch8WrongCnot = testVerifyChallengeWithGates(7, "X0, CX0-1, CX0-1");
assert(ch8WrongCnot.isFail, "Bài 8: Sai chuỗi 3 CNOT bị từ chối");

const ch8Correct = testVerifyChallengeWithGates(7, "X0, CX0-1, CX1-0, CX0-1");
assert(ch8Correct.isSuccess, "Bài 8: Áp đúng X0, CX0-1, CX1-0, CX0-1 đạt 100% và VƯỢT QUA");

// Challenge 9: Bernstein-Vazirani Oracle & Superposition
const ch9Cheat = testVerifyChallengeWithGates(8, "X0, X1, X2, H2");
assert(ch9Cheat.isFail, "Bài 9: Gian lận lật bit trực tiếp mà không dùng Oracle bị từ chối");

const ch9Correct = testVerifyChallengeWithGates(8, "H0, H1, X2, H2, CX0-2, CX1-2, H0, H1");
assert(ch9Correct.isSuccess, "Bài 9: Áp đúng thuật toán BV đạt 100% và VƯỢT QUA");

// Challenge 10: Grover Search 2-Qubit
const ch10Cheat = testVerifyChallengeWithGates(9, "X0, X1");
assert(ch10Cheat.isFail, "Bài 10: Gian lận dùng X0, X1 mà không dùng Grover (CZ + Diffuser) bị từ chối");

const ch10CheatCancel = testVerifyChallengeWithGates(9, "CZ0-1, H0, H0, X0, X1");
assert(ch10CheatCancel.isFail, "Bài 10: Gian lận triệt tiêu CZ và H rồi lật bit bằng X0, X1 bị từ chối");

const ch10CheatEndsWithX = testVerifyChallengeWithGates(9, "H0, H1, CZ0-1, H0, H1, CZ0-1, X0, X1");
assert(ch10CheatEndsWithX.isFail, "Bài 10: Gian lận kết thúc bằng X0, X1 thay vì bộ khuếch đại Grover bị từ chối");

const ch10Correct = testVerifyChallengeWithGates(9, "H0, H1, CZ0-1, H0, H1, X0, X1, CZ0-1, X0, X1, H0, H1");
assert(ch10Correct.isSuccess, "Bài 10: Áp đúng thuật toán Grover đạt 100% và VƯỢT QUA");

// Challenge 11: GHZ 3-Qubit (linear & star topology)
const ch11Linear = testVerifyChallengeWithGates(10, "H0, CX0-1, CX1-2");
assert(ch11Linear.isSuccess, "Bài 11: Dạng chuỗi tuyến tính (H0, CX0-1, CX1-2) đạt 100% và VƯỢT QUA");

const ch11Star = testVerifyChallengeWithGates(10, "H0, CX0-1, CX0-2");
assert(ch11Star.isSuccess, "Bài 11: Dạng hình sao (H0, CX0-1, CX0-2) đạt 100% và VƯỢT QUA");

// Challenge 12: QEC Bit-Flip Correction
const ch12DeletedError = testVerifyChallengeWithGates(11, "H0, CX0-1, CX0-2");
assert(ch12DeletedError.isFail, "Bài 12: Xóa cổng lỗi X1 khỏi mạch ban đầu bị từ chối");
assert(ch12DeletedError.body.includes("giữ nguyên mạch mã hóa và mô phỏng lỗi"), "Bài 12: Báo lỗi phải giữ nguyên mạch mã hóa ban đầu");

const ch12NoCorrection = testVerifyChallengeWithGates(11, "H0, CX0-1, CX0-2, X1");
assert(ch12NoCorrection.isFail, "Bài 12: Giữ nguyên mạch lỗi mà chưa thêm cổng sửa lỗi X1 bị từ chối");

const ch12Correct = testVerifyChallengeWithGates(11, "H0, CX0-1, CX0-2, X1, X1");
assert(ch12Correct.isSuccess, "Bài 12: Giữ nguyên mạch lỗi và thêm cổng sửa lỗi X1 đạt 100% và VƯỢT QUA");

// ── Test Suite 4: Tab Switching Across 6 Modules ───────────────────────────
console.log("\n[4] Kiểm Tra Chuyển Tab Giữa 6 Phân Hệ Tương Tác:");
const tabs = ['challenges', 'bloch', 'pairwise', 'grover', 'qec', 'chsh'];
tabs.forEach(t => {
  domWindow.switchPracticeTab(t);
  const btn = elements.get(`tab-btn-${t}`);
  const pane = elements.get(`tab-pane-${t}`);
  assert(btn && btn.classList.contains('active'), `Tab ${t}: Nút tab có class active`);
  assert(pane && pane.classList.contains('active'), `Tab ${t}: Khung pane có class active`);
});

// ── Test Suite 5: Cross-Slide Link Consistency ─────────────────────────────
console.log("\n[5] Kiểm Tra Tính Nhất Quán Của Liên Kết Giữa Các Slide:");

const slidesDir = path.join(__dirname, '../slides');
const slideFiles = ['phase0.html', 'phase1.html', 'phase2.html', 'phase3.html', 'phase4_5.html', 'index.html'];

slideFiles.forEach(file => {
  const content = fs.readFileSync(path.join(slidesDir, file), 'utf8');
  const hasLink = content.includes('practice.html');
  assert(hasLink, `${file}: Có liên kết dẫn tới practice.html`);
});

// Verify practice.html links back to all phases
const practiceHtml = fs.readFileSync(path.join(slidesDir, 'practice.html'), 'utf8');
['index.html', 'phase0.html', 'phase1.html', 'phase2.html', 'phase3.html', 'phase4_5.html'].forEach(f => {
  assert(practiceHtml.includes(f), `practice.html: Có liên kết ngược về ${f}`);
});

// Check slide specific deep links
const phase0Html = fs.readFileSync(path.join(slidesDir, 'phase0.html'), 'utf8');
assert(phase0Html.includes('practice.html#bloch'), "phase0.html: Slide 06 liên kết tới Quả cầu Bloch 3D (#bloch)");
assert(phase0Html.includes('practice.html#ch-1'), "phase0.html: Slide 08 liên kết tới Mini-Kata 1 (#ch-1)");
assert(phase0Html.includes('practice.html#ch-7'), "phase0.html: Slide 11 liên kết tới Mini-Kata 7 H·H=I (#ch-7)");
assert(phase0Html.includes('practice.html#ch-3'), "phase0.html: Slide 17 liên kết tới Mini-Kata 3–5 Bell (#ch-3)");
assert(phase0Html.includes('practice.html#challenges'), "phase0.html: Slide 21 liên kết tới #challenges");
assert(phase0Html.includes('assets/practice_lab.js'), "phase0.html: Đã nhúng script practice_lab.js");

const phase1Html = fs.readFileSync(path.join(slidesDir, 'phase1.html'), 'utf8');
assert(phase1Html.includes('practice.html#pairwise'), "phase1.html: Liên kết trực tiếp tới #pairwise");

const phase2Html = fs.readFileSync(path.join(slidesDir, 'phase2.html'), 'utf8');
assert(phase2Html.includes('practice.html#grover'), "phase2.html: Liên kết trực tiếp tới #grover");

const phase3Html = fs.readFileSync(path.join(slidesDir, 'phase3.html'), 'utf8');
assert(phase3Html.includes('practice.html#pairwise'), "phase3.html: Liên kết trực tiếp tới #pairwise");

const phase4Html = fs.readFileSync(path.join(slidesDir, 'phase4_5.html'), 'utf8');
assert(phase4Html.includes('practice.html#qec'), "phase4_5.html: Liên kết trực tiếp tới #qec");
assert(phase4Html.includes('practice.html#chsh'), "phase4_5.html: Liên kết trực tiếp tới #chsh");

// ── Test Suite 6: URL Hash Navigation & Deep Linking ───────────────────────
console.log("\n[6] Kiểm Tra Điều Hướng URL Hash & Deep Links:");

let lastHistoryUrl = "";
domWindow.history = {
  replaceState: (state, title, url) => {
    lastHistoryUrl = url;
    domWindow.location.hash = url;
  }
};

// Test hash navigation to Challenge 7
domWindow.location.hash = "#ch-7";
domWindow.handleHashNav();
const titleEl = elements.get("ch-cur-title");
assert(titleEl && titleEl.innerText.includes("Bài 7"), "Hash #ch-7: Tự động kích hoạt đúng Bài 7 (Giao Thoa Triệt Tiêu)");

// Test hash navigation to Grover tab
domWindow.location.hash = "#grover";
domWindow.handleHashNav();
const groverBtn = elements.get("tab-btn-grover");
const groverPane = elements.get("tab-pane-grover");
assert(groverBtn && groverBtn.classList.contains("active"), "Hash #grover: Tự động kích hoạt đúng tab Grover");
assert(groverPane && groverPane.classList.contains("active"), "Hash #grover: Khung pane grover hiển thị active");

// Test selecting Challenge 3 updates URL hash
domWindow.selectChallenge(2);
assert(lastHistoryUrl === "#ch-3", "selectChallenge(2): Tự động đồng bộ URL hash thành #ch-3");

// Test switching tab to bloch updates URL hash
domWindow.switchPracticeTab("bloch");
assert(lastHistoryUrl === "#bloch", "switchPracticeTab('bloch'): Tự động đồng bộ URL hash thành #bloch");

// ── Summary ────────────────────────────────────────────────────────────────
console.log("\n==================================================================");
console.log(`  KẾT QUẢ KIỂM THỬ: ${passedTests} passed, ${failedTests} failed`);
console.log("==================================================================");

if (failedTests > 0) {
  process.exit(1);
} else {
  console.log("🎉 TẤT CẢ TEST CASES ĐÃ CHUYỂN XANH HOÀN HẢO!\n");
  process.exit(0);
}
