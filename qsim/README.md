# qsim — simulator state-vector tự viết

Deliverable của **Phase 1**. Bạn điền các TODO trong `qsim.py` cho tới khi 39 test xanh.

```bash
source ~/quantum-env/bin/activate
cd qsim
pytest test_qsim.py -x -q      # -x = dừng ở lỗi đầu tiên
```

## 5 mốc

| Mốc | Ngày | Nội dung | Test |
|---|---|---|---|
| 1 | 1–2 | Ma trận cổng 1 qubit + khởi tạo state | `test_moc1_*` |
| 2 | 3–4 | `apply_1q()` bằng ghép cặp biên độ — **khó nhất** | `test_moc2_*` |
| 3 | 5–6 | CNOT, CZ, SWAP | `test_moc3_*` |
| 4 | 7–8 | Xác suất, lấy mẫu, đo có sụp đổ | `test_moc4_*` |
| 5 | 9–10 | Kiểm chứng chéo với `qiskit-aer` | `test_khop_qiskit_*` |

## Đọc độ lệch ở mốc 5 để đoán bệnh

| Độ lệch | Nguyên nhân |
|---|---|
| `~1e-16` | Đúng rồi — sai số dấu phẩy động |
| `~1e-1` trở lên | Sai quy ước endian, hoặc nhầm control/target |
| Chỉ lệch dấu/pha | `rz` viết dạng `diag(1, e^{iθ})` — đổi sang dạng đối xứng |
| Đúng 1 qubit, sai từ 2 qubit | CNOT đổi hai lần mỗi cặp (thiếu điều kiện bit t = 0) |

Bản làm đúng đạt sai số lớn nhất `3.7e-16` qua 200 mạch ngẫu nhiên tới 5 qubit.
