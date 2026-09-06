# Lỗi hay gặp & cách gỡ

Sắp theo **triệu chứng bạn nhìn thấy**, không theo nguyên nhân — vì lúc gặp lỗi bạn
chỉ có triệu chứng trong tay.

---

## A. Môi trường & cài đặt

### `command not found: python` sau khi mở terminal mới

Bạn chưa activate virtualenv. Mỗi cửa sổ terminal mới đều phải chạy lại:

```bash
source ~/quantum-env/bin/activate
```

Dấu hiệu đã đúng: đầu dòng prompt có `(quantum-env)`.

Đỡ phải gõ lại: thêm vào `~/.zshrc`

```bash
alias qenv="source ~/quantum-env/bin/activate"
```

### `ModuleNotFoundError: No module named 'qiskit'` dù đã cài

Gần như luôn là **cài vào một Python, chạy bằng Python khác**. Kiểm chứng:

```bash
which python
python -c "import sys; print(sys.executable)"
pip -V
```

Ba dòng này phải cùng trỏ vào `~/quantum-env`. Nếu `pip -V` trỏ chỗ khác, dùng
`python -m pip install ...` thay vì `pip install ...`.

### `pip` / `pytest` hỏng sau khi `mv` thư mục env

Virtualenv **nhúng đường dẫn tuyệt đối** vào `bin/*` và `pyvenv.cfg`. Di chuyển là
hỏng, không sửa vặt được. Tạo lại:

```bash
python3.11 -m venv ~/quantum-env
source ~/quantum-env/bin/activate
pip install -r requirements.txt
```

### `numpy.dtype size changed` hoặc lỗi ABI lạ khi import

Xung đột NumPy 1.x/2.x. Qiskit 2.5 bắt buộc NumPy ≥ 2.0:

```bash
pip install -U "numpy>=2.0" qiskit qiskit-aer
```

---

## B. API Qiskit đã đổi

### `ImportError: cannot import name 'execute' from 'qiskit'`

`execute()` đã bị xoá khỏi Qiskit 1.0. Đây là dấu hiệu bạn đang đọc tutorial cũ hơn
2024 — **đóng tab đó lại**, phần còn lại của nó cũng sẽ sai.

```python
# ❌ chết
from qiskit import execute
job = execute(qc, backend, shots=1024)

# ✅ dùng
from qiskit_aer.primitives import SamplerV2
counts = SamplerV2().run([qc], shots=1024).result()[0].data.meas.get_counts()
```

### `AttributeError: 'DataBin' object has no attribute 'meas'`

Tên trường trong `.data` là tên **classical register**. `measure_all()` tạo register
tên `meas`; nhưng nếu bạn tự khai báo `ClassicalRegister(1, "kq")` thì phải đọc
`.data.kq`.

```python
print(result[0].data.keys())     # xem có những trường nào
```

### `QiskitError: 'No counts for experiment'`

Mạch không có phép đo nào. Thêm `qc.measure_all()` — hoặc nếu bạn muốn xem state
vector thì dùng `Statevector(qc)` và **không** thêm measure.

### `Statevector` báo lỗi hoặc ra kết quả kỳ lạ

`Statevector(qc)` không chấp nhận mạch có `measure`. Tách làm hai mạch: một để xem
trạng thái, một để đo.

---

## C. Kết quả chạy được nhưng sai

### Kết quả ra `'01'` trong khi bạn kỳ vọng `'10'`

Endianness. Qiskit là **little-endian**: bit phải nhất là qubit 0.

```python
qc = QuantumCircuit(3)
qc.x(0)                    # đặt X lên qubit 0
qc.measure_all()
# → in ra '001', KHÔNG phải '100'
```

Bạn không sai vật lý, bạn sai quy ước. Bấm thử ở widget slide
`phase1.html` (slide "🔬 Endianness · nhìn tận mắt") 30 giây là nhớ mãi.

### Mạch Bell ra cả `'01'` và `'10'`

- Nếu chạy trên **simulator lý tưởng**: bạn đặt CNOT sai chiều, hoặc `measure_all()`
  đứng trước CNOT. Kiểm tra bằng `print(qc.draw("text"))`.
- Nếu chạy trên **máy thật**: đây là bình thường — đó chính là nhiễu, và cũng chính
  là thứ bạn được yêu cầu quan sát ở Phase 2.

### Simulator tự viết khớp Qiskit ở 1 qubit nhưng lệch ở nhiều qubit

Ba nghi phạm, theo thứ tự khả năng:

1. **Thứ tự tensor.** Phải là `kron(U_{n-1}, …, U_1, U_0)` — ngược với thứ tự đọc.
2. **Ghi đè trong vòng lặp ghép cặp.** Phải đọc `a, b` ra biến tạm **trước** khi ghi:

   ```python
   a, b = state[i], state[j]        # đọc trước
   state[i] = U[0,0]*a + U[0,1]*b
   state[j] = U[1,0]*a + U[1,1]*b
   ```

   Nếu bạn ghi `state[i]` rồi mới tính `state[j]` từ `state[i]`, bạn đang dùng giá
   trị đã bị hỏng. Đây là bug #1 của mốc 2.
3. **Rz sai dạng.** Xem [`bang-tra-cong.md`](bang-tra-cong.md) mục "Bẫy Rz".

### Kết quả khớp về xác suất nhưng lệch dấu / lệch pha

Rất có thể chỉ là **pha toàn cục** — không phải lỗi. Kiểm tra đúng cách: so
`|⟨φ|ψ⟩|` (giá trị tuyệt đối của tích trong) chứ đừng so từng phần tử.

```python
import numpy as np
assert abs(abs(np.vdot(mine, theirs)) - 1) < 1e-9
```

Nhưng nếu pha lệch **giữa các nhánh** (pha tương đối) thì đó là lỗi thật.

### Grover chạy đúng với 1 vòng nhưng sai với nhiều vòng

Đúng như dự kiến, không phải bug. Số vòng tối ưu là `≈ (π/4)·√N`. Grover là một
**phép quay** — quay quá thì đi qua đích và xác suất tụt xuống. Với N = 4 thì đúng
1 vòng; N = 16 thì 3 vòng.

### Đo giữa mạch xong thì "phép màu" biến mất

Đúng như vật lý. Phép đo phá huỷ pha, nên không còn gì để giao thoa nữa. Nếu bạn cần
kết quả đo mà không muốn phá trạng thái, bạn cần **ancilla** — đo qubit phụ chứ
không đo qubit dữ liệu (đây chính là ý tưởng của QEC).

---

## D. Hiệu năng

### Máy treo / hết RAM khi tăng số qubit

Bạn đang dựng ma trận đầy đủ `2ⁿ×2ⁿ`. Với 15 qubit đó là 17 GB. Chuyển sang ghép
cặp — xem Phase 1 mốc 2.

### Simulator chậm hơn hẳn `qiskit-aer`

Bình thường. Aer có SIMD, có nhiều năm tối ưu, có backend chuyên biệt. Việc của bạn
không phải thắng Aer mà là **hiểu vì sao thua**, rồi viết điều đó ra. Ba chỗ nên
kiểm tra trước:

- Có đang cấp phát mảng mới mỗi cổng không? (nên làm tại chỗ)
- Python thuần trong vòng lặp thay vì vector hoá bằng NumPy slice?
- Ở Rust: có đang đo bản **debug** không? Debug chậm hơn release 10–50×.

### `python qk.py watch` ăn CPU

Giảm tần suất poll hoặc dùng `python qk.py run` thủ công. Nếu đang mở nhiều watch
cùng lúc, tắt bớt.

---

## E. Slide & tài liệu

### Trang chủ không hiện tiến độ kata thật

`fetch()` bị chặn khi mở bằng `file://`. Phải qua HTTP:

```bash
python katas/qk.py progress
cd slides && python -m http.server 8000
```

Rồi mở <http://localhost:8000>.

### Widget mạch trong slide không hiện gì

Mở Console của trình duyệt (F12). Thường là:

- Thiếu `<script src="assets/qlab.js"></script>` trong file HTML đó
- Sai cú pháp `data-gates` — đúng dạng là `H0, CX0-1, RZ1:0.5` (xem
  [`huong-dan-slide.md`](huong-dan-slide.md))

### Bấm `→` mà slide không chuyển

Slide đó có **fragment** — mũi tên đang hé lộ từng ý một. Góc dưới phải có chấm tiến
độ (ví dụ `2/4`). Bấm `Shift + →` để bỏ qua và sang thẳng slide sau.

### Mất tiến độ / checklist sau khi đổi trình duyệt

Tiến độ lưu trong `localStorage` — riêng cho từng trình duyệt và từng máy, và bị xoá
khi bạn dùng chế độ ẩn danh. Đây là chủ ý: không có server, không gửi dữ liệu đi đâu.

---

## Khi không tìm thấy lỗi của bạn ở đây

1. Đọc **dòng cuối cùng** của traceback trước, không đọc từ đầu.
2. Rút gọn về mạch nhỏ nhất còn tái hiện được lỗi (thường 1–2 qubit).
3. So với `Statevector` của Qiskit ở **từng bước**, không chỉ ở cuối.
4. Nếu là kata: `python qk.py hint <id>` trước khi `solution`.
