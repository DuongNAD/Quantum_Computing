# Từ điển thuật ngữ lượng tử · Việt ⇄ Anh

Mục tiêu của trang này: khi bạn đọc paper, đọc docs Qiskit, hoặc nghe người ta nói
chuyện, bạn **không phải dừng lại tra cứu**. Mỗi mục có ba phần: tên tiếng Anh
(dùng cái này khi search), cách nói bằng tiếng Việt, và **một câu giải thích không
dùng toán**.

Sắp xếp theo thứ tự bạn gặp trong lộ trình, không phải theo alphabet — vì tra theo
alphabet thì bạn đã biết mình tìm gì rồi.

---

## Phase 0 · Khái niệm nền

| Tiếng Anh | Tiếng Việt | Nói ngắn gọn là |
|---|---|---|
| **qubit** | qubit (không dịch) | Đơn vị thông tin lượng tử. Mô tả bằng 2 số phức, không phải 1 bit. |
| **amplitude** | biên độ | Hai số phức α, β. **Không** phải xác suất — bình phương độ lớn của nó mới là. |
| **probability amplitude** | biên độ xác suất | Cách gọi đầy đủ của "amplitude". Cái tên nhắc bạn: nó liên quan xác suất nhưng không phải xác suất. |
| **Born rule** | quy tắc Born | `P(kết quả k) = |amplitude_k|²`. Cây cầu duy nhất nối toán lượng tử với cái bạn quan sát được. |
| **superposition** | chồng chập | Nhiều biên độ khác 0 cùng lúc. **Không** phải "vừa là 0 vừa là 1". |
| **interference** | giao thoa | Các biên độ cộng lại **có dấu** → nhánh triệt tiêu, nhánh cộng dồn. Đây mới là nguồn sức mạnh, không phải "song song". |
| **constructive / destructive** | tăng cường / triệt tiêu | Hai nhánh cùng dấu thì cộng dồn; ngược dấu thì giết nhau. |
| **phase** | pha | Hướng của số phức trên mặt phẳng phức. Vô hình khi đo, quyết định khi giao thoa. |
| **global phase** | pha toàn cục | Nhân **cả** trạng thái với `e^{iθ}`. Không quan sát được bằng bất kỳ phép đo nào → bỏ qua được. |
| **relative phase** | pha tương đối | Pha **lệch nhau giữa các nhánh**. Cái này thì có ý nghĩa vật lý thật. |
| **measurement** | phép đo | Lấy ra một chuỗi bit cổ điển. Ngẫu nhiên theo Born rule, và **phá huỷ** trạng thái. |
| **collapse** | sập trạng thái | Sau khi đo, trạng thái nhảy về đúng cái bạn vừa đo được. Không đảo ngược được. |
| **gate** | cổng | Một ma trận unitary tác động lên trạng thái. Luôn đảo ngược được. |
| **unitary** | unitary (đơn nhất) | Ma trận thoả `U†U = I` — giữ nguyên tổng xác suất. Mọi tiến hoá lượng tử (trừ phép đo) đều unitary. |
| **circuit** | mạch | Dãy cổng, đọc **từ trái sang phải** như dòng thời gian. |
| **shots** | shots (số lần chạy) | Chạy lại toàn bộ mạch bao nhiêu lần để lấy thống kê. Một lần đo thì chẳng biết được gì. |
| **entanglement** | vướng víu / rối lượng tử | Trạng thái nhiều qubit **không tách được** thành từng qubit riêng lẻ. |
| **Bell state** | trạng thái Bell | Bốn trạng thái vướng víu tối đa của 2 qubit: `|Φ⁺⟩ |Φ⁻⟩ |Ψ⁺⟩ |Ψ⁻⟩`. |
| **Bloch sphere** | quả cầu Bloch | Bản đồ mọi trạng thái 1 qubit. Cực bắc `|0⟩`, cực nam `|1⟩`, xích đạo là các chồng chập 50/50. |
| **no-cloning theorem** | định lý không sao chép | Không có cổng nào copy được một qubit chưa biết. Đây là lý do QKD an toàn và QEC khó. |
| **no-communication theorem** | định lý không truyền tin | Vướng víu **không** cho phép truyền tin nhanh hơn ánh sáng. Tương quan ≠ truyền tin. |

## Phase 1 · Toán & simulator

| Tiếng Anh | Tiếng Việt | Nói ngắn gọn là |
|---|---|---|
| **state vector** | vector trạng thái | Mảng `2ⁿ` số phức mô tả đầy đủ n qubit. Đây là thứ simulator của bạn lưu. |
| **ket / bra** | ket / bra | `|ψ⟩` = vector cột. `⟨ψ|` = vector hàng liên hợp chuyển vị. `⟨φ|ψ⟩` = tích trong (một số). |
| **tensor product / Kronecker** | tích tensor / tích Kronecker | Cách ghép hệ: 2 qubit độc lập → vector 4 chiều. Ký hiệu `⊗`, trong NumPy là `np.kron`. |
| **normalization** | chuẩn hoá | Ép `Σ|αᵢ|² = 1`. Bắt buộc sau mỗi phép đo trong simulator. |
| **conjugate transpose (dagger)** | liên hợp chuyển vị | `U†` — chuyển vị rồi lấy liên hợp phức. Nghịch đảo của mọi cổng chính là `U†`. |
| **Hermitian** | Hermite | `A† = A`. Các đại lượng đo được (observable) đều là ma trận Hermite. |
| **eigenvalue / eigenvector** | trị riêng / vector riêng | `A|v⟩ = λ|v⟩`. Kết quả đo luôn là một trị riêng. |
| **little-endian** | little-endian | Quy ước Qiskit: **qubit 0 là bit phải nhất** của chuỗi. `'100'` nghĩa là q₂=1. |
| **pairwise indexing** | ghép cặp biên độ | Thuật toán áp cổng mà không dựng ma trận `2ⁿ×2ⁿ`. `O(2ⁿ)` thay vì `O(4ⁿ)`. |
| **in-place** | tại chỗ | Sửa mảng trạng thái trực tiếp, không cấp phát bản sao. Quan trọng khi n lớn. |
| **density matrix** | ma trận mật độ | `ρ = |ψ⟩⟨ψ|`. Cần khi hệ có nhiễu hoặc khi xét một phần của hệ vướng víu. |
| **partial trace** | vết riêng phần | "Vứt bỏ" các qubit khác để xem một qubit trông thế nào. Kết quả thường là trạng thái hỗn hợp. |
| **mixed state** | trạng thái hỗn hợp | Không phải chồng chập — là **không biết chắc** trạng thái nào. Phải mô tả bằng ρ, không dùng ket được. |
| **fidelity** | độ trung thực | Đo hai trạng thái giống nhau bao nhiêu, từ 0 đến 1. Thước đo chính khi so simulator với Aer. |

## Phase 2 · Thuật toán

| Tiếng Anh | Tiếng Việt | Nói ngắn gọn là |
|---|---|---|
| **oracle** | oracle (hộp đen) | Một cổng đóng gói hàm `f(x)` bạn muốn hỏi. Đếm số lần gọi oracle = đo độ phức tạp. |
| **query complexity** | độ phức tạp truy vấn | Cần hỏi oracle bao nhiêu lần. Đây là thước đo mà hầu hết "tăng tốc lượng tử" nói tới. |
| **phase kickback** | phase kickback | Đặt target ở `|−⟩` thì CNOT không đổi target mà "đá" một dấu `(−1)^x` ngược lên control. Cơ chế trung tâm của 5/7 thuật toán. |
| **phase oracle** | oracle pha | Oracle ghi đáp án vào **pha** thay vì vào bit: `|x⟩ → (−1)^{f(x)}|x⟩`. |
| **amplitude amplification** | khuếch đại biên độ | Ý tưởng tổng quát của Grover: lật dấu đáp án đúng rồi lật quanh trung bình. |
| **diffuser / diffusion operator** | toán tử khuếch tán | Nửa sau của một vòng Grover: "lật quanh giá trị trung bình". |
| **teleportation** | dịch chuyển lượng tử | Chuyển **trạng thái** một qubit sang qubit khác, dùng 1 cặp Bell + 2 bit cổ điển. Không chuyển vật chất, không nhanh hơn ánh sáng. |
| **superdense coding** | mã hoá siêu đặc | Đối ngẫu của teleportation: gửi 2 bit cổ điển bằng 1 qubit (đã chia sẵn cặp Bell). |
| **QFT** | biến đổi Fourier lượng tử | Phiên bản lượng tử của DFT. `O(n²)` cổng thay vì `O(n·2ⁿ)`. Nền của Shor. |
| **phase estimation (QPE)** | ước lượng pha | Tìm trị riêng của một unitary. Ứng dụng lớn nhất của QFT⁻¹. |
| **transpile** | biên dịch mạch | Dịch mạch của bạn sang tập cổng mà phần cứng thật hỗ trợ, kèm ánh xạ qubit. Bắt buộc trước khi chạy máy thật. |
| **basis gates** | tập cổng cơ sở | Danh sách cổng mà một con chip thật chạy được (ví dụ `rz, sx, x, ecr`). Mọi thứ khác phải phân rã ra. |
| **circuit depth** | độ sâu mạch | Số lớp cổng chạy nối tiếp. Sâu hơn = nhiều thời gian để nhiễu tích tụ hơn. |

## Phase 3–4 · Hiệu năng, nhiễu, sửa lỗi

| Tiếng Anh | Tiếng Việt | Nói ngắn gọn là |
|---|---|---|
| **decoherence** | mất kết hợp | Qubit "quên" pha do tương tác với môi trường. Kẻ thù số một của máy thật. |
| **T1 / T2** | thời gian T1 / T2 | T1: thời gian `|1⟩` rơi về `|0⟩`. T2: thời gian pha bị mờ đi. Đọc số này trước khi thiết kế mạch cho máy thật. |
| **readout error** | lỗi đọc | Đo ra 1 trong khi thực tế là 0 (và ngược lại). Thường là nguồn lỗi lớn nhất, và cũng dễ hiệu chỉnh nhất. |
| **gate fidelity** | độ chính xác cổng | Cổng 2 qubit thường sai ~0.3–1%; cổng 1 qubit tốt hơn ~10×. Đây là lý do nên đếm số cổng 2 qubit. |
| **NISQ** | NISQ | "Noisy Intermediate-Scale Quantum" — thời kỳ hiện tại: đủ qubit để thú vị, quá nhiễu để tin cậy. |
| **QEC** | sửa lỗi lượng tử | Dùng nhiều qubit vật lý để tạo một qubit logic ít lỗi hơn. |
| **logical / physical qubit** | qubit logic / vật lý | Surface code hiện cần **hàng nghìn** qubit vật lý cho 1 qubit logic. |
| **syndrome** | syndrome (dấu hiệu lỗi) | Kết quả đo ancilla, cho biết **có lỗi ở đâu** mà không tiết lộ dữ liệu. |
| **stabilizer** | stabilizer | Nhóm toán tử giữ nguyên trạng thái mã hoá. Ngôn ngữ chuẩn để mô tả mọi mã QEC. |
| **surface code** | mã bề mặt | Mã QEC được đặt cược nhiều nhất hiện nay: lưới 2D, chỉ cần tương tác hàng xóm gần. |
| **threshold** | ngưỡng | Nếu lỗi vật lý thấp hơn ngưỡng này thì thêm qubit sẽ giảm lỗi; cao hơn thì thêm qubit làm tệ hơn. |
| **VQE / QAOA** | VQE / QAOA | Thuật toán lai lượng tử–cổ điển cho hoá học và tối ưu. Chạy được trên NISQ. |
| **barren plateau** | cao nguyên cằn | Gradient tắt dần theo hàm mũ khi mạch tham số sâu — vấn đề trung tâm của QML. |
| **ansatz** | ansatz | Dạng mạch tham số bạn chọn trước trong VQE/QML. Chọn sai ansatz thì tối ưu kiểu gì cũng không ra. |

---

## Ba cặp từ hay bị dùng lẫn

**Chồng chập ≠ vướng víu.** Một qubit có thể chồng chập. Chỉ **từ hai qubit trở lên**
mới nói tới vướng víu. `H|0⟩` là chồng chập không vướng víu; `(|00⟩+|11⟩)/√2` là cả hai.

**Ngẫu nhiên ≠ chồng chập.** Đồng xu đang quay là ngẫu nhiên cổ điển — nó *thật sự*
đã là sấp hoặc ngửa, bạn chỉ chưa biết. Chồng chập thì khác: chưa có kết quả nào tồn
tại, và đó là lý do hai nhánh giao thoa được. Thí nghiệm H·H ở Phase 0 chứng minh
điều này.

**Pha toàn cục ≠ pha tương đối.** `|1⟩` và `−|1⟩` là **cùng một trạng thái vật lý**.
Nhưng `(|0⟩+|1⟩)/√2` và `(|0⟩−|1⟩)/√2` là **hai trạng thái khác nhau**. Khác biệt:
cái sau có pha *lệch giữa các nhánh*.

---

## Cách tra nhanh khi đọc paper

- Không hiểu một ký hiệu → xem [`ky-hieu-toan.md`](ky-hieu-toan.md)
- Không nhớ ma trận một cổng → xem [`bang-tra-cong.md`](bang-tra-cong.md)
- Code chạy sai/không chạy → xem [`faq-loi-hay-gap.md`](faq-loi-hay-gap.md)
