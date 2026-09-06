# Tài liệu tra cứu

Năm trang. Không trang nào cần đọc từ đầu đến cuối — chúng là **tài liệu tra cứu**,
mở ra khi bí rồi đóng lại.

| Trang | Mở khi nào |
|---|---|
| [`thuat-ngu.md`](thuat-ngu.md) | Gặp một từ tiếng Anh không chắc nghĩa. 90+ mục, xếp theo thứ tự bạn gặp trong lộ trình. |
| [`bang-tra-cong.md`](bang-tra-cong.md) | Cần ma trận của một cổng, một đẳng thức, hoặc khuôn mẫu API Qiskit 2.x. **In ra dán cạnh màn hình.** |
| [`ky-hieu-toan.md`](ky-hieu-toan.md) | Không đọc được một công thức: bra-ket, `⊗`, `†`, endianness, cách đọc sơ đồ mạch. |
| [`faq-loi-hay-gap.md`](faq-loi-hay-gap.md) | Code không chạy, hoặc chạy mà ra kết quả lạ. Sắp theo **triệu chứng**, không theo nguyên nhân. |
| [`ke-hoach-18-tuan.md`](ke-hoach-18-tuan.md) | Đầu tuần và cuối tuần. Bản theo dõi có cửa ải cho từng phase. |
| [`huong-dan-slide.md`](huong-dan-slide.md) | Muốn sửa slide hoặc viết deck mới. Tra cứu đầy đủ mọi component. |

## Ba câu trả lời nhanh nhất

**"Kết quả ra `'01'` mà tôi kỳ vọng `'10'`."**
Endianness — Qiskit là little-endian, qubit 0 nằm ở **bit phải nhất**.
→ [`faq-loi-hay-gap.md` mục C](faq-loi-hay-gap.md)

**"`from qiskit import execute` báo lỗi."**
API đó đã bị xoá từ Qiskit 1.0. Tutorial bạn đang đọc đã chết.
→ [`bang-tra-cong.md` mục 6](bang-tra-cong.md)

**"Simulator của tôi khớp Qiskit ở 1 qubit nhưng lệch ở nhiều qubit."**
Ba nghi phạm: thứ tự tensor, ghi đè trong vòng lặp ghép cặp, dạng của `Rz`.
→ [`faq-loi-hay-gap.md` mục C](faq-loi-hay-gap.md)
