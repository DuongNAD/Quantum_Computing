# Quy ước ký hiệu

Trang này để bạn đọc được công thức trong paper và trong slide mà không phải đoán.
Không chứng minh gì — chỉ giải thích **ký hiệu đó nghĩa là gì**.

---

## 1. Ký hiệu Dirac (bra–ket)

| Viết | Đọc là | Là cái gì |
|---|---|---|
| `\|ψ⟩` | "ket psi" | Vector cột. Trạng thái lượng tử. |
| `⟨ψ\|` | "bra psi" | Vector hàng, **liên hợp chuyển vị** của `\|ψ⟩`. |
| `⟨φ\|ψ⟩` | "bra-ket" / tích trong | Một **số phức**. Bằng 0 nghĩa là hai trạng thái trực giao. |
| `\|ψ⟩⟨φ\|` | tích ngoài | Một **ma trận**. `\|ψ⟩⟨ψ\|` là toán tử chiếu lên ψ. |
| `⟨ψ\|A\|ψ⟩` | giá trị kỳ vọng | Trung bình của phép đo A nếu lặp lại vô hạn lần. |
| `\|\|ψ⟩\|` hoặc `‖ψ‖` | chuẩn | `√⟨ψ\|ψ⟩`. Trạng thái hợp lệ luôn có chuẩn = 1. |

Vì sao dùng ký hiệu này thay vì vector thường: nó cho phép viết `⟨0|1⟩ = 0` gọn hơn
nhiều so với `[1,0]ᵀ · [0,1] = 0`, và nó tự nhắc bạn cái nào là hàng, cái nào là cột.

## 2. Cơ sở tính toán

```
|0⟩ = [1]      |1⟩ = [0]
      [0]            [1]
```

Trạng thái tổng quát của 1 qubit:

```
|ψ⟩ = α|0⟩ + β|1⟩ = [α]      với  |α|² + |β|² = 1
                     [β]
```

Với n qubit, cơ sở có `2ⁿ` phần tử, đánh nhãn bằng chuỗi bit:

```
|ψ⟩ = Σ  α_x |x⟩        x chạy từ 000…0 tới 111…1
```

## 3. Số phức — đúng phần cần dùng

| Ký hiệu | Nghĩa |
|---|---|
| `i` (vật lý: `j` trong Python) | `i² = −1` |
| `z = a + bi` | dạng đại số |
| `z̄` hoặc `z*` | liên hợp: `a − bi` |
| `\|z\|` | module: `√(a² + b²)` |
| `\|z\|²` | `z·z̄ = a² + b²` — **đây là cái cho ra xác suất** |
| `arg(z)` | pha (góc), tính bằng `atan2(b, a)` |
| `e^{iθ}` | `cos θ + i·sin θ` — số có module 1, pha θ |

Ba giá trị nên nhớ ngay: `e^{iπ} = −1`, `e^{iπ/2} = i`, `e^{2πi} = 1`.

Trong Python số ảo viết bằng `j` và **phải có số đứng trước**: `1j`, không phải `j`.

## 4. Ma trận

| Ký hiệu | Nghĩa |
|---|---|
| `Aᵀ` | chuyển vị |
| `Ā` hoặc `A*` | liên hợp từng phần tử |
| `A†` ("A dagger") | liên hợp chuyển vị = `Āᵀ` |
| `A⁻¹` | nghịch đảo |
| `I` | ma trận đơn vị |
| `tr(A)` | vết — tổng đường chéo |

Hai tính chất dùng liên tục:

- **Unitary**: `U†U = UU† = I`. Suy ra `U⁻¹ = U†` — nghịch đảo của mọi cổng chỉ là
  dagger của nó. Đây là lý do mọi mạch lượng tử đảo ngược được.
- **Hermite**: `A† = A`. Trị riêng luôn thực → dùng làm đại lượng đo được.

## 5. Tích tensor `⊗`

Ghép hai hệ độc lập thành một hệ lớn.

```
|0⟩ ⊗ |1⟩ = |01⟩
```

Với ma trận, đây là tích Kronecker:

```
A ⊗ B = [a₀₀·B   a₀₁·B]
        [a₁₀·B   a₁₁·B]
```

**Thứ tự là chỗ dễ sai nhất.** Theo quy ước Qiskit (little-endian), muốn áp `U` lên
qubit `t` trong hệ n qubit:

```python
full = np.kron(np.eye(2**(n-1-t)), np.kron(U, np.eye(2**t)))
```

Chú ý: `I` của các qubit **cao hơn** đứng **bên trái**. Viết ngược là mọi kết quả
nhiều qubit sẽ lệch.

Nhưng — như Phase 1 nói rất kỹ — **đừng dùng công thức này để chạy thật**. Nó tốn
`O(4ⁿ)`. Dùng ghép cặp biên độ.

## 6. Endianness — bảng đối chiếu

Qiskit đánh chỉ số sao cho `index = Σ bit_q · 2^q`, tức **qubit 0 là bit phải nhất**:

| Chỉ số | Nhị phân | q₂ | q₁ | q₀ | Qiskit in ra |
|---|---|---|---|---|---|
| 0 | 000 | 0 | 0 | 0 | `'000'` |
| 1 | 001 | 0 | 0 | **1** | `'001'` |
| 2 | 010 | 0 | **1** | 0 | `'010'` |
| 4 | 100 | **1** | 0 | 0 | `'100'` |

Một nghịch lý gây khó chịu: `qc.draw()` vẽ **q₀ ở dòng trên cùng**, còn chuỗi kết quả
lại có q₀ ở **phải nhất**. Cả hai đều đúng theo quy ước của mình; chỉ cần biết trước.

## 7. Ký hiệu hay gặp trong paper

| Ký hiệu | Nghĩa |
|---|---|
| `H^{⊗n}` | áp H lên **tất cả** n qubit |
| `U^{\|x⟩}` hoặc `U_f` | oracle của hàm f |
| `\|x⟩\|y ⊕ f(x)⟩` | oracle kiểu XOR (bit oracle) |
| `(−1)^{f(x)}\|x⟩` | oracle kiểu pha (phase oracle) |
| `ρ` | ma trận mật độ |
| `Tr_B(ρ)` | vết riêng phần — bỏ hệ B đi |
| `⊕` | XOR (cộng modulo 2) |
| `·` giữa hai chuỗi bit | tích trong modulo 2: `s·x = Σ sᵢxᵢ mod 2` |
| `Õ(f)` | độ phức tạp bỏ qua thừa số log |
| `\|Φ⁺⟩, \|Ψ⁻⟩ …` | các trạng thái Bell |

## 8. Cách đọc một mạch

```
q₀: ──H──■──────M──
         │
q₁: ─────⊕──────M──
```

- **Đọc từ trái sang phải** như dòng thời gian
- Mỗi dây ngang = một qubit, nhãn ở đầu dây
- Ô vuông có chữ = cổng 1 qubit
- Chấm đặc `■` = **control**; `⊕` = **target** của CNOT
- Đường dọc nối control với target
- `M` hoặc biểu tượng đồng hồ đo = phép đo
- Dây đôi (nếu có) = bit **cổ điển**, không phải qubit

Mạch trên: đặt q₀ vào chồng chập, vướng víu nó với q₁, rồi đo cả hai. Đây là mạch
Bell.

---

Xem tiếp: [`bang-tra-cong.md`](bang-tra-cong.md) · [`thuat-ngu.md`](thuat-ngu.md)
