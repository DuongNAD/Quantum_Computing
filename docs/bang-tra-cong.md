# Bảng tra cổng lượng tử

Một trang, in ra dán cạnh màn hình. Mọi ma trận đều viết theo quy ước
**Qiskit / little-endian**: qubit 0 là bit phải nhất.

---

## 1. Cổng 1 qubit

| Cổng | Ma trận | Làm gì | Qiskit |
|---|---|---|---|
| **I** | `[[1,0],[0,1]]` | không làm gì | `qc.id(q)` |
| **X** | `[[0,1],[1,0]]` | lật bit — đổi chỗ α, β | `qc.x(q)` |
| **Y** | `[[0,-i],[i,0]]` | lật bit **và** lật pha | `qc.y(q)` |
| **Z** | `[[1,0],[0,-1]]` | đổi dấu `|1⟩`; xác suất **không đổi** | `qc.z(q)` |
| **H** | `[[1,1],[1,-1]]/√2` | tạo/gỡ chồng chập đều | `qc.h(q)` |
| **S** | `[[1,0],[0,i]]` | pha 90° cho `|1⟩` | `qc.s(q)` |
| **S†** | `[[1,0],[0,-i]]` | nghịch đảo của S | `qc.sdg(q)` |
| **T** | `[[1,0],[0,e^{iπ/4}]]` | pha 45° cho `|1⟩` | `qc.t(q)` |
| **T†** | `[[1,0],[0,e^{-iπ/4}]]` | nghịch đảo của T | `qc.tdg(q)` |
| **P(λ)** | `[[1,0],[0,e^{iλ}]]` | pha tuỳ ý cho `|1⟩` | `qc.p(λ, q)` |
| **Rx(θ)** | `[[cos(θ/2), -i·sin(θ/2)], [-i·sin(θ/2), cos(θ/2)]]` | quay θ quanh trục x | `qc.rx(θ, q)` |
| **Ry(θ)** | `[[cos(θ/2), -sin(θ/2)], [sin(θ/2), cos(θ/2)]]` | quay θ quanh trục y — **ma trận thực** | `qc.ry(θ, q)` |
| **Rz(θ)** | `[[e^{-iθ/2}, 0], [0, e^{iθ/2}]]` | quay θ quanh trục z | `qc.rz(θ, q)` |

> **Bẫy Rz.** Nhiều tài liệu viết `Rz(θ) = diag(1, e^{iθ})`. Bản đó lệch một
> **pha toàn cục** so với Qiskit. Trạng thái riêng lẻ thì không sao, nhưng khi Rz
> nằm dưới một cổng có điều khiển thì pha đó thành pha **tương đối** và kết quả sai.
> Luôn dùng dạng đối xứng `diag(e^{-iθ/2}, e^{+iθ/2})`.

## 2. Cổng nhiều qubit

| Cổng | Làm gì | Qiskit |
|---|---|---|
| **CX / CNOT** | lật target khi control = 1 | `qc.cx(c, t)` |
| **CZ** | đổi dấu chỉ khi **cả hai** = 1 (đối xứng!) | `qc.cz(a, b)` |
| **CP(λ)** | pha λ khi cả hai = 1 | `qc.cp(λ, a, b)` |
| **SWAP** | tráo hai qubit | `qc.swap(a, b)` |
| **CCX / Toffoli** | lật target khi **cả hai** control = 1 | `qc.ccx(c1, c2, t)` |
| **CSWAP / Fredkin** | tráo hai qubit khi control = 1 | `qc.cswap(c, a, b)` |

CNOT trên cơ sở tính toán, với q0 = control, q1 = target (thứ tự chỉ số `|q1 q0⟩`):

```
|00⟩ → |00⟩      |01⟩ → |11⟩      |10⟩ → |10⟩      |11⟩ → |01⟩
```

## 3. Đẳng thức phải thuộc

Đây là những quan hệ mà test của bạn sẽ kiểm tra, và cũng là những gì bạn dùng để
rút gọn mạch bằng tay.

```
H·H  = I           X·X = Y·Y = Z·Z = I
S·S  = Z           T·T = S
H·X·H = Z          H·Z·H = X          H·Y·H = −Y
X·Y  = iZ          Y·Z = iX           Z·X = iY
Rx(π) = −i·X       Ry(π) = −i·Y       Rz(π) = −i·Z
CNOT·CNOT = I      SWAP = CX(a,b)·CX(b,a)·CX(a,b)
```

`H·X·H = Z` là đẳng thức đáng nhớ nhất: nó nói rằng **lật bit trong hệ quy chiếu X
chính là lật pha trong hệ quy chiếu Z**. Toàn bộ trò "giấu đáp án vào pha rồi dùng H
để lộ ra" nằm trong dòng đó.

Ba dòng `Rx(π) = −i·X` là chỗ hầu hết người tự viết simulator trượt test: quay 180°
**không** bằng đúng cổng Pauli, nó lệch một pha toàn cục `−i`.

## 4. Sáu trạng thái mốc

| Ký hiệu | Vector | Là gì | Dựng bằng |
|---|---|---|---|
| `|0⟩` | `[1, 0]` | cực bắc Bloch | (mặc định) |
| `|1⟩` | `[0, 1]` | cực nam | `X` |
| `|+⟩` | `[1, 1]/√2` | +x | `H` |
| `|−⟩` | `[1, -1]/√2` | −x | `X, H` |
| `|+i⟩` | `[1, i]/√2` | +y | `H, S` |
| `|−i⟩` | `[1, -i]/√2` | −y | `H, S†` |

Bốn trạng thái Bell:

| Tên | Vector | Mạch |
|---|---|---|
| `|Φ⁺⟩` | `(|00⟩ + |11⟩)/√2` | `H(0), CX(0,1)` |
| `|Φ⁻⟩` | `(|00⟩ − |11⟩)/√2` | `H(0), CX(0,1), Z(0)` |
| `|Ψ⁺⟩` | `(|01⟩ + |10⟩)/√2` | `H(0), CX(0,1), X(1)` |
| `|Ψ⁻⟩` | `(|01⟩ − |10⟩)/√2` | `H(0), CX(0,1), X(1), Z(0)` |

## 5. Đổi hệ quy chiếu đo

Qiskit chỉ đo được trên cơ sở Z. Muốn đo trên cơ sở khác thì **quay trước rồi đo**:

| Muốn đo theo | Làm gì trước khi `measure` |
|---|---|
| Z (mặc định) | không cần gì |
| X | `qc.h(q)` |
| Y | `qc.sdg(q); qc.h(q)` |

Đây chính là câu trả lời cho "làm sao phân biệt `|+⟩` và `|−⟩`": đo theo cơ sở X.

## 6. Qiskit 2.x — API còn dùng được

Rất nhiều tutorial trên mạng dùng API đã bị xoá. Bảng đối chiếu:

| Đã chết ❌ | Dùng thay ✅ |
|---|---|
| `from qiskit import execute` | `SamplerV2` / `EstimatorV2` |
| `Aer.get_backend('qasm_simulator')` | `from qiskit_aer.primitives import SamplerV2` |
| `backend.run(qc)` rồi `result.get_counts()` | `sampler.run([qc]).result()[0].data.meas.get_counts()` |
| `qiskit.IBMQ` | `qiskit_ibm_runtime.QiskitRuntimeService` |
| `qc.u3(...)` | `qc.u(...)` |

Khuôn mẫu chạy local, copy dùng luôn:

```python
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

counts = SamplerV2().run([qc], shots=4096).result()[0].data.meas.get_counts()
print(counts)          # {'00': ~2048, '11': ~2048}
```

Xem state vector (chỉ simulator mới cho phép):

```python
from qiskit.quantum_info import Statevector
print(Statevector(QuantumCircuit(2)).data)     # không có measure_all() trong mạch!
```

## 7. Bảng chi phí — dùng để ước lượng trước khi code

| n qubit | số biên độ | RAM (complex128) |
|---|---|---|
| 10 | 1 024 | 16 KB |
| 20 | 1 048 576 | 16 MB |
| 24 | 16.7 triệu | 268 MB |
| 28 | 268 triệu | 4.3 GB |
| 30 | 1.07 tỉ | 17 GB |
| 40 | — | 17 TB |

Quy tắc nhẩm: **+10 qubit = ×1024 bộ nhớ**. Trần thực tế của một laptop 16 GB là
khoảng 26–28 qubit, và chỉ đạt được nếu bạn làm việc **tại chỗ** (in-place), không
cấp phát bản sao mỗi cổng.

---

Xem thêm: [`thuat-ngu.md`](thuat-ngu.md) · [`ky-hieu-toan.md`](ky-hieu-toan.md) · [`faq-loi-hay-gap.md`](faq-loi-hay-gap.md)
