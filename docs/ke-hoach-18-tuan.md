# Kế hoạch 18 tuần — bản theo dõi

Bản in ra được. Mỗi tuần có **một deliverable kiểm chứng được**, không phải "đã đọc
xong chương X". Nếu cuối tuần không có thứ chạy được thì tuần đó chưa xong — đừng đi
tiếp.

Cách dùng: mỗi tối Chủ nhật, tick những dòng đã xong và ghi số kata vào cột cuối.

---

## Phase 0 · Khởi động (2 giờ, không phải một tuần)

| ✓ | Việc | Kiểm chứng bằng |
|---|---|---|
| ☐ | Đọc hết `slides/phase0.html` | 24 slide, có nghịch cả 4 widget |
| ☐ | Môi trường chạy | `python -c "import qiskit; print(qiskit.__version__)"` → `2.5.1` |
| ☐ | `h_test.py` | ra ~50/50 |
| ☐ | `giao_thoa.py` | mạch B ra **đúng** 4096/4096 số `'0'` |
| ☐ | `bell_test.py` | chỉ có `'00'` và `'11'` |
| ☐ | Tài khoản IBM Quantum | đã đăng nhập được |
| ☐ | Nghịch Quirk ≥ 30 phút | — |
| ☐ | Kata Bậc 1–2 | **25/350** |

**Cửa ải:** giải thích được vì sao H·H ra 100% mà H một lần ra 50/50. Không giải
thích được thì đọc lại slide "Giao thoa xảy ra ở bước nào".

---

## Phase 1 · Tự viết simulator (tuần 1–2)

| Tuần | ✓ | Mốc | Kiểm chứng | Kata |
|---|---|---|---|---|
| 1 | ☐ | Mốc 1 — ma trận cổng | test mốc 1 xanh | |
| 1 | ☐ | Mốc 2 — ghép cặp biên độ ⭐ | test mốc 2 xanh, chạy được 15 qubit | |
| 1 | ☐ | Kata Bậc 3 | | **61** |
| 2 | ☐ | Mốc 3 — cổng 2 qubit | dựng được Bell state | |
| 2 | ☐ | Mốc 4 — đo lường | phân bố đúng, chuẩn hoá lại đúng | |
| 2 | ☐ | Mốc 5 — kiểm chứng chéo với Aer | **39/39 test xanh** | |
| 2 | ☐ | Kata Bậc 4 | | **92** |
| 2 | ☐ | Push repo `qsim-py` | README ghi rõ quy ước endian | |

**Cửa ải:** `pytest qsim/test_qsim.py -q` xanh hết, và bạn nói được vì sao ghép cặp
là `O(2ⁿ)` còn ma trận đầy đủ là `O(4ⁿ)`.

---

## Phase 2 · Bảy thuật toán (tuần 3–5)

Với **mỗi** thuật toán, làm đủ 3 bước: (1) chạy trên `qsim.py` của bạn, (2) chạy
bằng Qiskit, (3) viết 3 câu giải thích vì sao nó nhanh hơn cổ điển.

| Tuần | ✓ | Thuật toán | Kata |
|---|---|---|---|
| 3 | ☐ | Phase kickback (hiểu cơ chế trước, không phải thuật toán) | |
| 3 | ☐ | Teleportation | |
| 3 | ☐ | Superdense coding | **129** |
| 4 | ☐ | Deutsch–Jozsa | |
| 4 | ☐ | Bernstein–Vazirani | |
| 4 | ☐ | Simon | **188** |
| 5 | ☐ | Grover (thử 1, 2, 3 vòng — vẽ đồ thị xác suất) | |
| 5 | ☐ | QFT | **211** |
| 5 | ☐ | **Chạy trên `ibm_kingston` thật** + biểu đồ nhiễu | |

**Cửa ải:** có một biểu đồ so simulator lý tưởng với máy thật, và bạn giải thích được
mỗi nguồn lỗi đến từ đâu (readout / gate / decoherence).

---

## Phase 3 · Simulator bằng Rust (tuần 6–9) ⭐

| Tuần | ✓ | Mốc | Kiểm chứng |
|---|---|---|---|
| 6 | ☐ | Cấu trúc dữ liệu + cổng 1 qubit | khớp `qsim.py` trên mạch ngẫu nhiên |
| 7 | ☐ | Cổng có điều khiển + đo | dựng được GHZ 20 qubit |
| 8 | ☐ | Song song hoá bằng `rayon` | có số speedup đo bằng `criterion` |
| 9 | ☐ | Binding Python qua `pyo3` + `maturin` | `pip install` rồi `import` chạy được |
| 9 | ☐ | Kata Bậc 8 | **311** |
| 9 | ☐ | README có biểu đồ benchmark 4 cột | naive / pair / rayon / aer |
| 9 | ☐ | Bài viết ngắn | trung thực kể cả khi chậm hơn Aer |

**Cửa ải:** simulator chạy được ≥ 26 qubit trên máy bạn, và bạn có bốn con số:
trần qubit, thời gian 1 cổng H trên 24 qubit, hệ số speedup của rayon, tỉ lệ so Aer.

---

## Phase 4 · Chuyên sâu (tuần 10–14) — chọn **một** nhánh

| ✓ | Nhánh | Deliverable |
|---|---|---|
| ☐ | **A · QEC** (khuyến nghị) | decoder cho bit-flip code hoặc surface code nhỏ, viết bằng Rust |
| ☐ | **B · QML** | một mô hình biến phân chạy được + phân tích barren plateau |
| ☐ | **C · Simulation** | mô phỏng một hệ vật lý/hoá học nhỏ bằng VQE |

| ✓ | Việc chung | |
|---|---|---|
| ☐ | Kata Bậc 9 | **350/350** |
| ☐ | Dự án chuyên sâu có README + kết quả số | |

**Cửa ải:** một repo mà người lạ đọc README trong 2 phút là hiểu bạn làm gì, tại sao,
và kết quả ra sao.

---

## Phase 5 · Hero (tuần 15+, liên tục)

| ✓ | Việc |
|---|---|
| ☐ | Học QGSS labs (Qiskit Global Summer School) |
| ☐ | PR đầu tiên vào một repo lượng tử open source |
| ☐ | Đọc và tóm tắt được 5 paper trong nhánh của bạn |
| ☐ | Tham gia một sự kiện (unitaryHACK / QHack / IBM Challenge) |

---

## Bốn quy tắc quyết định bạn có đi hết không

1. **Lý thuyết just-in-time.** Không đọc chương nào trước khi có một dòng code sai
   vì thiếu chương đó.
2. **Mỗi phase đúng một deliverable chạy được.** Không deliverable = chưa xong phase,
   dù đã hiểu hết slide.
3. **Simulator trước, phần cứng sau.** Quota QPU dùng để *quan sát nhiễu*, không
   phải để chạy thí nghiệm.
4. **Đều đặn hơn dồn dập.** 1 giờ mỗi ngày ăn đứt 7 giờ Chủ nhật.

## Khi bị chững lại

| Triệu chứng | Việc nên làm |
|---|---|
| Đọc mãi mà không thấy hiểu | Dừng đọc. Mở widget trong slide và bấm cho tới khi thấy điều mình đang đọc. |
| Kata khó quá, nản | Lùi một bậc. Bậc 6 mà bí thì Bậc 3–4 chưa chắc. |
| Code chạy nhưng không hiểu vì sao đúng | Đó là nợ kỹ thuật. Xoá đi viết lại từ đầu, đừng đi tiếp. |
| Mất động lực tuần 3 | Đây là chỗ hầu hết bỏ cuộc. Giảm mục tiêu xuống 20 phút/ngày, nhưng **đừng nghỉ hẳn một tuần**. |
| Không biết mình đang ở đâu | `python katas/qk.py` — bảng tiến độ trả lời ngay. |
