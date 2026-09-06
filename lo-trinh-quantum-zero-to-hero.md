# Lộ trình Quantum Computing: Zero → Hero (hands-on first)

**Thiết kế riêng cho:** nền Rust systems + AI/ML, môi trường WSL + conda
**Ngày lập:** 08/08/2026 · **Nhịp giả định:** 6–8h/tuần · **Tổng:** ~18 tuần đến mức "làm được việc"

---

## 0. Ba quyết định đã chốt sẵn (đừng phân vân lại)

| Câu hỏi | Quyết định | Lý do |
|---|---|---|
| Framework chính? | **Qiskit 2.5** (bản mới nhất, 14/07/2026) | Hệ sinh thái lớn nhất, có phần cứng thật miễn phí, core đang được viết lại bằng Rust → hợp nền của bạn |
| Framework phụ? | **PennyLane** — chỉ khi vào Phase 4 nhánh QML | Autodiff tốt nhất cho quantum ML. Không học song song từ đầu |
| Bỏ qua cái gì? | **Cirq, Q#, Braket** | Học 3 framework cùng lúc = học cú pháp, không học khái niệm. Chuyển framework sau này mất đúng 1 buổi |
| Python version? | **3.12** | PennyLane hiện yêu cầu ≥ 3.11 — con số 3.10 trong tài liệu cũ sẽ chặn bạn ở Phase 4 |
| Điểm khác biệt của bạn? | **Tự viết simulator bằng Rust** (Phase 3) | 99% người học quantum chỉ biết gọi API. Bạn có lợi thế viết được cái nằm dưới API |

---

## 1. Đính chính tài liệu "Cẩm nang Thực hành" bạn đang có

Ba chỗ trong tài liệu đó sẽ làm bạn mất thời gian nếu làm theo nguyên văn:

**a) "Qiskit QuantumKatas" — không phải khóa học bài tập.**
Tài liệu mô tả nó như một bộ Jupyter Notebook có sẵn hàm trống để bạn điền và chạy unit test. Thực tế: đây là **benchmark đánh giá LLM**, công bố tháng 5/2026 (Juan Cruz-Benito & Ismael Faro, arXiv:2605.27210), phát hành dưới dạng **dataset trên HuggingFace** (`cbjuan/qiskit-quantumkatas`) — 350 task, 26 nhóm, mỗi task có prompt + lời giải chuẩn + test kiểm chứng bằng mô phỏng cổ điển.

→ Bạn **vẫn dùng được** nó làm ngân hàng bài tập (Phase 2), nhưng phải tự dựng khung notebook. Bản katas "điền vào chỗ trống" thật sự là bản Q# gốc của Microsoft. Còn thứ đúng nghĩa "khóa học tương tác trên trình duyệt, không cần cài gì" là **PennyLane Codebook**.

**b) Python 3.10** — xem bảng trên. Dùng 3.12.

**c) `pip install qiskit` trần** sẽ thiếu công cụ vẽ mạch. Xem lệnh đúng ở Phase 0.

Phần còn lại của tài liệu (Miniconda, VS Code + extension Python/Jupyter, Quirk, IBM Quantum Composer) là chuẩn — giữ nguyên.

---

## 2. Nguyên tắc vận hành lộ trình

1. **Lý thuyết just-in-time.** Không đọc chương nào trước khi có một dòng code bị sai vì thiếu chương đó.
2. **Mỗi phase có đúng 1 deliverable chạy được.** Không có deliverable = chưa xong phase, dù đã xem hết video.
3. **Simulator trước, phần cứng sau.** Phần cứng thật chỉ dùng ở đúng 2 thời điểm trong toàn bộ lộ trình.
4. **Push mọi thứ lên GitHub.** Đây là lộ trình học *và* là 2–3 dòng CV.

---

## PHASE 0 — Môi trường (1 buổi, ~2h)

### Cài đặt

```bash
# WSL — Miniconda nếu chưa có
conda create -n quantum python=3.12 -y
conda activate quantum

# Qiskit 2.5 + extras visualization (kéo theo pylatexenc, matplotlib, seaborn)
pip install "qiskit[visualization]==2.5.*" qiskit-aer qiskit-ibm-runtime
pip install jupyterlab
```

**Lưu ý phiên bản:** Qiskit từ v2.5 yêu cầu **NumPy ≥ 2.0** và **SciPy ≥ 1.14**. Nếu bạn tái dùng một env cũ có NumPy 1.x, nó sẽ gãy — tạo env mới sạch như trên.

**VS Code + WSL:** cài extension **WSL**, **Python**, **Jupyter**. Mở folder bằng `code .` từ trong WSL, chọn interpreter là env `quantum`. Đừng chạy `jupyter notebook` rồi copy URL sang browser Windows — VS Code Remote-WSL xử lý sạch hơn.

### Test môi trường (đây là Bell state, code Qiskit 2.x đúng chuẩn hiện tại)

```python
# bell_test.py
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

sampler = SamplerV2()
result = sampler.run([qc], shots=4096).result()
counts = result[0].data.meas.get_counts()
print(counts)          # kỳ vọng ~50% '00', ~50% '11', gần như không có '01'/'10'
print(qc.draw("text"))
```

> **API đã đổi:** Qiskit ≥ 1.0 bỏ `execute()` và `backend.run()` kiểu cũ. Mọi tutorial trên mạng dùng `from qiskit import execute` là code **trước 2024** — bỏ qua. Chuẩn hiện tại là **primitives**: `SamplerV2` (lấy phân bố bit) và `EstimatorV2` (lấy kỳ vọng của observable).

### Đăng ký IBM Quantum (làm luôn, chưa dùng vội)

Tạo tài khoản tại IBM Quantum Platform. **Open Plan** hiện cho:
- **10 phút runtime QPU thật / mỗi 28 ngày** (rolling window), miễn phí, không cần thẻ
- Từ 16/03/2026: mở quyền truy cập **`ibm_kingston`** (Heron r2, 156 qubit) cho toàn bộ user Open Plan
- Nếu tích lũy đủ 20 phút sử dụng trong 12 tháng → opt-in được gói khuyến mãi **180 phút cho 12 tháng tiếp theo**

10 phút nghe ít nhưng thực tế mỗi circuit nhỏ chỉ tốn vài chục mili-giây QPU time. Cái tốn thời gian là **hàng đợi**, không phải quota.

### Chơi 30 phút, không code

- **Quirk** (`algassert.com/quirk`) — kéo thả cổng, thấy biên độ và pha đổi realtime. Đây là công cụ trực quan tốt nhất từng có cho phần này.
- **IBM Quantum Composer** — bố cục giống mạch thật hơn.

**✅ Deliverable Phase 0:** `bell_test.py` chạy ra ~50/50, screenshot mạch.

---

## PHASE 1 — Tự viết simulator bằng NumPy (Tuần 1–2)

> Đây là phần thay thế cho "đọc chương 2 Nielsen & Chuang". Bạn sẽ học đại số tuyến tính lượng tử **vì code không chạy nếu bạn hiểu sai**, không phải vì sách bảo thế.

### Bạn xây gì

Một file `qsim.py` (~120 dòng) mô phỏng state-vector:

```
Ngày 1–2   Biểu diễn state = np.array 2^n phần tử complex128. Chuẩn hóa. Đo (Born rule).
Ngày 3–4   Cổng 1 qubit: I, X, Y, Z, H, S, T, Rx/Ry/Rz. Áp dụng bằng np.kron.
Ngày 5–6   Cổng 2 qubit: CNOT, CZ, SWAP. Đây là chỗ bạn thật sự hiểu entanglement.
Ngày 7–8   Đo lấy mẫu (sampling) + đo có sụp đổ trạng thái (collapse).
Ngày 9–10  Kiểm chứng chéo: mọi mạch bạn viết phải khớp qiskit_aer trong sai số 1e-10.
```

### Bốn khái niệm lý thuyết duy nhất cần nạp (mỗi cái ~20 phút)

1. **Số phức + biên độ/pha** — xác suất là `|amplitude|²`, và pha là thứ tạo ra giao thoa
2. **Tích tensor (Kronecker)** — vì sao n qubit cần 2^n số phức
3. **Ma trận unitary** — vì sao mọi cổng lượng tử đều đảo ngược được
4. **Born rule** — đo là gì, và vì sao đo thì mất thông tin

Nguồn: khóa **"Basics of Quantum Information"** của John Watrous trên IBM Quantum Learning (miễn phí, chặt chẽ, có notebook). Chỉ đọc đúng mục đang cần.

### Bẫy lớn nhất của phase này

Endianness. Qiskit đánh số qubit **little-endian** (qubit 0 là bit **phải nhất** trong chuỗi bitstring). Nếu simulator của bạn ra `'10'` còn Qiskit ra `'01'`, bạn không sai vật lý — bạn sai quy ước. Chốt quy ước từ dòng code đầu tiên và ghi vào docstring.

**✅ Deliverable Phase 1:** repo `qsim-py` + một file test khẳng định simulator của bạn khớp `qiskit-aer` trên ≥ 10 mạch ngẫu nhiên.

---

## PHASE 2 — Thuật toán kinh điển trên Qiskit (Tuần 3–5)

Giờ mới dùng framework — và bạn sẽ dùng nó với con mắt của người biết bên trong nó có gì.

### 2a. PennyLane Codebook (tuần 3, ~6h)

`pennylane.ai/codebook` — chạy hoàn toàn trên trình duyệt, không cài gì, có chấm bài tự động. Làm module **I (Introduction)** đến **F (Fourier)**. Đây là thứ tài liệu cũ *tưởng* là QuantumKatas.

Bổ sung: `pennylane.ai/challenges` — dạng competitive programming, chấm điểm, có certificate. Rất hợp gu nếu bạn thích thử thách lập trình.

### 2b. Cài lại từng thuật toán bằng Qiskit (tuần 4–5)

Với **mỗi** thuật toán, làm đủ 3 bước — đây mới là chỗ đọng lại kiến thức:

1. Cài đặt trên `qsim.py` của chính bạn
2. Cài đặt lại bằng Qiskit
3. Viết 5 dòng trả lời: *thuật toán này khai thác giao thoa/vướng víu ở đúng chỗ nào?*

| Thuật toán | Ý tưởng bạn phải bắt được | Độ khó |
|---|---|---|
| Quantum teleportation | Entanglement + classical channel, **không** truyền nhanh hơn ánh sáng | ★★ |
| Superdense coding | Mặt đối ngẫu của teleportation | ★★ |
| Deutsch–Jozsa | Truy vấn oracle 1 lần thay vì 2^(n-1) — nhưng bài toán này vô dụng thực tế | ★★ |
| Bernstein–Vazirani | Rõ ràng hơn D–J, dễ debug hơn | ★★ |
| Simon's | Tiền thân trực tiếp của Shor. Có hậu xử lý cổ điển (giải hệ GF(2)) | ★★★ |
| Grover (2–3 qubit) | Amplitude amplification. Vẽ được diffusion operator trên Bloch | ★★★ |
| QFT | Nền của Shor và phase estimation | ★★★★ |

Ngân hàng bài tập bổ sung: dataset `cbjuan/qiskit-quantumkatas` trên HuggingFace — mỗi task có lời giải chuẩn + test tự động, bạn tự bọc thành notebook.

### 2c. Lần chạy phần cứng thật đầu tiên (cuối tuần 5) — thời khắc quan trọng nhất lộ trình

Chạy **Bell state** và **Grover 3 qubit** trên `ibm_kingston`, rồi đặt kết quả cạnh kết quả simulator.

```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

service = QiskitRuntimeService()          # đã lưu token trước đó
backend = service.least_busy(operational=True, simulator=False)

pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
isa_qc = pm.run(qc)                       # bắt buộc: transpile về ISA của máy thật

sampler = SamplerV2(mode=backend)
result = sampler.run([isa_qc], shots=4096).result()
```

> Chuỗi `channel=` khi lưu token đã đổi vài lần trong 2025–2026 (`ibm_quantum` → `ibm_cloud` → `ibm_quantum_platform`). Copy chính xác từ trang docs tại thời điểm bạn đăng ký, đừng copy từ blog post cũ. Ngoài ra từ Qiskit v2.5, "Qiskit Runtime Service" được IBM đổi tên thành **IBM Quantum Compute Service** — API không đổi, chỉ tên đổi.

Bạn sẽ thấy `'01'` và `'10'` xuất hiện với tỉ lệ vài phần trăm. Đó là **noise**. Khoảnh khắc bạn thật sự hiểu vì sao cả ngành đang đổ tiền vào error correction chứ không phải vào thuật toán mới.

**✅ Deliverable Phase 2:** repo `quantum-algorithms` — 7 notebook, mỗi cái có bản của bạn + bản Qiskit + ghi chú. Cộng 1 notebook so sánh simulator vs `ibm_kingston` kèm biểu đồ.

---

## PHASE 3 — Simulator bằng Rust (Tuần 6–9) ⭐ Đây là lợi thế của bạn

Phase này không ai bắt bạn làm. Nó là thứ tách bạn khỏi vài nghìn người khác cũng "học Qiskit trên Coursera".

**Bối cảnh khiến nó đáng giá gấp đôi:** core data model của Qiskit đang được viết lại bằng **Rust**. Bản v2.3 (01/2026) hoàn tất việc chuyển `ControlFlowOp` sang Rust — mảnh cuối cùng. v2.4 và v2.5 mở rộng **C API** để viết transpiler pass bằng C/Rust rồi nạp vào Qiskit dưới dạng compiled Python extension. Nghĩa là: một người viết Rust tốt hiện đang là loại contributor mà dự án quantum lớn nhất thế giới đang thiếu.

### Kiến trúc gợi ý

```rust
// Vec<Complex64> độ dài 2^n. Không dùng ndarray cho state vector — thừa.
// Crates: num-complex, rayon, criterion (bench), pyo3 + maturin (binding Python)
```

### Chìa khóa thuật toán — đừng bao giờ dựng ma trận 2^n × 2^n

Áp một cổng 1-qubit lên qubit `t` **không** cần nhân ma trận đầy đủ. Chỉ cần duyệt các **cặp biên độ** có chỉ số khác nhau đúng ở bit `t`:

```rust
// cho mỗi i mà bit t của i bằng 0:
//   (state[i], state[i | (1<<t)]) = (a*state[i] + b*state[i|(1<<t)],
//                                    c*state[i] + d*state[i|(1<<t)])
```

Độ phức tạp rơi từ O(4^n) xuống **O(2^n) mỗi cổng**. Đây chính là design principle của **Spinoza** (`github.com/QuState/spinoza`, arXiv:2303.01493) — đọc source của nó *sau khi* bạn tự nghĩ ra, không phải trước.

### Mốc tiến độ

| Tuần | Mục tiêu | Kiểm chứng |
|---|---|---|
| 6 | Naive: dựng ma trận đầy đủ, chạy được 12 qubit | Khớp `qsim.py` |
| 7 | Pairwise indexing (ở trên) — lên 22–24 qubit | Khớp `qiskit-aer` |
| 8 | `rayon` song song hóa vòng lặp cặp — lên 26–28 qubit | Benchmark bằng `criterion` |
| 9 | Binding Python bằng `pyo3` + `maturin`, benchmark head-to-head với `qiskit-aer` | Biểu đồ, viết README |

### Hệ sinh thái Rust quantum để tham chiếu (đọc, đừng copy)

- **`spinoza`** — QuState/spinoza, state-vector thuần Rust, nhanh, kèm paper
- **`roqoqo` / `qoqo`** — HQS Quantum Simulations, toolkit đầy đủ, có backend QuEST
- **`RustQIP`** — Renmusxd/RustQIP, tận dụng borrow checker để enforce no-cloning theorem (rất thú vị về mặt thiết kế)
- **`qasmsim`** — interpreter OpenQASM bằng Rust
- **Qiskit source** — `github.com/Qiskit/qiskit`, thư mục `crates/`. Đọc để biết production code trông thế nào
- Index tổng hợp: `arewequantumyet.github.io`

**✅ Deliverable Phase 3:** repo Rust public + README có biểu đồ benchmark + một bài viết ngắn ("Tôi viết quantum simulator bằng Rust, nó nhanh hơn/chậm hơn Aer bao nhiêu và vì sao"). Đây là thứ recruiter thật sự click vào.

---

## PHASE 4 — Chọn đúng 1 nhánh chuyên sâu (Tuần 10–14)

Đừng học cả ba. Chọn một, làm sâu.

### Nhánh A — Quantum Error Correction ⭐ khuyến nghị cho bạn

**Vì sao hợp bạn:** QEC là bài toán **hệ thống + thuật toán đồ thị + hiệu năng**, không phải bài toán vật lý. Decoder là minimum-weight perfect matching. Simulator là code hiệu năng cao. Đây đúng là Anima Engine nhưng đổi domain. Và đây là nơi 80% nỗ lực kỹ thuật thật của ngành đang đổ vào.

- Công cụ: **`stim`** (`pip install stim`) — Clifford simulator của Craig Gidney, nhanh kinh khủng, chạy được hàng triệu shot của surface code
- **`pymatching`** — decoder MWPM, ghép trực tiếp với stim
- Lộ trình: repetition code (3 qubit) → phase-flip code → Shor 9-qubit → surface code distance 3 → 5 → tự viết decoder
- Dự án cuối: **viết lại decoder bằng Rust**, benchmark với pymatching. Ghép thẳng vào Phase 3.

### Nhánh B — Quantum Machine Learning

**Vì sao cân nhắc:** khớp trực tiếp với hồ sơ AI/ML bạn đang xây và các dự án NLP/AI hiện có.

- Công cụ: **PennyLane** (`pip install pennylane`), demos tại `pennylane.ai/qml`
- Nội dung: variational circuits, parameter-shift rule, data encoding, VQE, QAOA, quantum kernels
- **Nói thẳng một điều:** tính đến 2026, QML **chưa** chứng minh được lợi thế thực tế so với ML cổ điển trên bài toán thật. Vấn đề barren plateau (gradient tiêu biến theo hàm mũ khi số qubit tăng) vẫn chưa có lời giải chung, và nhiều kết quả "quantum advantage" ban đầu đã bị các thuật toán cổ điển đuổi kịp. Học nhánh này để hiểu và để nghiên cứu thì tốt; đừng học vì tin nó sắp thay thế PyTorch.

### Nhánh C — Quantum Simulation (hóa/vật lý)

Đây là ứng dụng có khả năng mang lại giá trị thật sớm nhất. Nhưng cần nền hóa lượng tử/vật lý chất rắn — với bạn thì đây là nhánh tốn công nhất trên mỗi đơn vị kiến thức thu được. Bỏ qua trừ khi bạn thực sự thích.

**✅ Deliverable Phase 4:** 1 dự án thật trong nhánh đã chọn, có README, có số liệu.

---

## PHASE 5 — "Hero": từ người học sang người đóng góp (Tháng 4 trở đi)

Ở điểm này "hero" không còn là học thêm khóa nào. Nó là 4 việc:

**1. Làm QGSS 2026 tự học.**
Qiskit Global Summer School 2026 vừa chạy 13–24/07/2026. Bạn đã lỡ đăng ký, nhưng lab bài tập public tại `github.com/qiskit-community/qgss-2026` và lecture được ghi hình. Làm hết lab — đây là nội dung cấp cao nhất còn miễn phí.

**2. Đóng góp open source.** Ưu tiên theo đúng lợi thế:
- Qiskit — issue gắn nhãn `good first issue`, đặc biệt phần Rust core trong `crates/`
- PennyLane — nhận đóng góp demo
- **unitaryHACK** — sự kiện hackathon open source quantum, chạy vào tháng 6 hằng năm (2026: 3–17/06). Có bounty tiền thật cho PR được merge. Đặt lịch nhắc cho tháng 5/2027.

**3. Thi đấu.** IBM Quantum Challenge, các hackathon quantum khu vực. Bạn đã có kinh nghiệm lead team ở VAIC và DENSO — mảng này bạn biết cách chơi rồi.

**4. Đọc paper có chọn lọc.** Mỗi tuần 1 paper trên arXiv `quant-ph`, và **cài lại phần chính bằng code**. Không cài lại = không đọc.

---

## Tài nguyên — danh sách rút gọn

**Học có chấm bài (ưu tiên cao nhất)**
- PennyLane Codebook — `pennylane.ai/codebook`
- PennyLane Challenges — `pennylane.ai/challenges`
- IBM Quantum Learning (khóa của John Watrous) — `quantum.cloud.ibm.com/learning`
- QGSS 2026 labs — `github.com/qiskit-community/qgss-2026`

**Trực quan**
- Quirk — `algassert.com/quirk`
- IBM Quantum Composer

**Nếu bạn muốn đúng 1 nguồn "lý thuyết"**
- **Quantum Computing for the Very Curious** — `quantum.country` (Michael Nielsen & Andy Matuschak). Đây là essay tích hợp **spaced repetition** ngay trong bài đọc — liên quan trực tiếp đến giao thức ghi nhớ bạn đang tự thiết kế. Đọc cái này thay vì mở Nielsen & Chuang chương 2.
- *Quantum Computation and Quantum Information* (Nielsen & Chuang) — chỉ dùng làm **từ điển tra cứu**. Đọc tuần tự là cách bỏ cuộc phổ biến nhất.

**Rust**
- spinoza · roqoqo/qoqo · RustQIP · qasmsim · Qiskit `crates/` · arewequantumyet.github.io

**QEC**
- `stim` — `github.com/quantumlib/Stim` · `pymatching`

---

## Sáu cái bẫy sẽ làm bạn bỏ cuộc

1. **Bắt đầu bằng đại số tuyến tính.** Đây là lý do #1 người ta bỏ. Code trước, toán khi bí.
2. **Copy code từ tutorial trước 2024.** Nếu có `from qiskit import execute` → code đã chết từ Qiskit 1.0. Luôn đối chiếu với docs chính thức.
3. **Học 3 framework song song.** Qiskit trước. PennyLane chỉ khi tới Phase 4B.
4. **Đốt quota QPU vào việc simulator làm được.** 10 phút/28 ngày để *quan sát noise*, không phải để chạy thí nghiệm.
5. **Tin hype.** "Quantum sẽ phá RSA năm sau" — không. Máy hiện tại vài trăm qubit vật lý, noisy; Shor cho RSA-2048 cần hàng triệu qubit vật lý với error correction. Biết điều này giúp bạn nói chuyện có trọng lượng trong phỏng vấn.
6. **Học một mình im lặng.** Discord của Qiskit và forum PennyLane trả lời rất nhanh.

---

## Nói thẳng về mặt nghề nghiệp

Quantum computing năm 2026 vẫn là ngành **tiền-thương-mại**. Số vị trí quantum engineer toàn cầu rất nhỏ và phần lớn yêu cầu PhD vật lý hoặc CS. Lộ trình này **không** phải con đường ngắn tới việc làm.

Nhưng nó có giá trị thật theo hai hướng khác, và cả hai đều hợp với hồ sơ bạn đang xây:

- **Làm bạn khác biệt trong tuyển dụng Data & AI.** Một simulator lượng tử viết bằng Rust có benchmark tử tế là bằng chứng năng lực kỹ thuật mạnh hơn nhiều so với thêm một chứng chỉ. Nhà tuyển dụng không cần bạn biết quantum — họ cần bằng chứng bạn học được thứ khó và ship được sản phẩm.
- **Đặt cược sớm, chi phí thấp.** Nếu ngành này cất cánh trong 5–10 năm, bạn đã ở trong. Nếu không, bạn vẫn giữ lại kỹ năng Rust hiệu năng cao, tính toán số học, và tư duy thuật toán — những thứ có giá trị bất kể quantum đi về đâu.

Học vì tò mò và vì thích những bài toán khó. Đó là lý do bền nhất, và nghe qua các dự án bạn đã làm thì đó cũng đúng là lý do của bạn.

---

## Checklist tổng

- [ ] **P0** (2h) — env chạy, Bell state 50/50, tài khoản IBM Quantum
- [ ] **P1** (2 tuần) — `qsim-py` khớp qiskit-aer trên 10 mạch ngẫu nhiên
- [ ] **P2** (3 tuần) — 7 thuật toán × 2 bản + 1 lần chạy `ibm_kingston` có biểu đồ noise
- [ ] **P3** (4 tuần) — simulator Rust ≥ 26 qubit, có benchmark, có bài viết
- [ ] **P4** (5 tuần) — 1 dự án chuyên sâu (khuyến nghị: QEC decoder bằng Rust)
- [ ] **P5** (liên tục) — QGSS labs, PR đầu tiên vào Qiskit, unitaryHACK 2027
