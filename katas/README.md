# 350 Quantum Katas · chấm tự động

Bộ bài gốc: [`qiskit-community/Qiskit-QuantumKatas`](https://github.com/qiskit-community/Qiskit-QuantumKatas) (Apache-2.0),
bản chuyển từ Microsoft QuantumKatas (Q#) sang Qiskit.

**Cần biết:** bộ gốc là *dataset benchmark đánh giá LLM* (`dataset/qiskit_quantumkatas.jsonl`),
không phải khoá học có notebook. Thư mục này bọc nó lại thành hệ thống luyện tập:
sắp xếp theo thứ tự học, sinh file bài tập, và chấm tự động.

Đã kiểm chứng **350/350 bài chạy đúng** với Qiskit 2.5.1 / Aer 0.17.2 / Python 3.11.8.

## Dùng

```bash
python qk.py                  # bảng tiến độ + bài kế tiếp
python qk.py gen              # sinh lại file thiếu (không ghi đè bài đã làm)
python qk.py next             # đọc đề đầy đủ
python qk.py run [ID]         # chấm
python qk.py run --bac 3      # chấm cả một bậc
python qk.py watch            # tự chấm khi lưu file
python qk.py hint ID          # gợi ý 3 mức
python qk.py solution ID      # lời giải chuẩn
python qk.py reset ID         # về stub gốc
python qk.py progress         # xuất JSON cho slides
```

## Cấu trúc

```
data/qiskit_quantumkatas.jsonl   bộ đề gốc (đề + lời giải + test)
curriculum.py                    thứ tự 9 bậc
qk.py                            runner
exercises/<bậc>/<chủ đề>/NNN-<tên hàm>.py    ← bạn viết code ở đây
.state.json                      tiến độ (an toàn khi xoá, chỉ mất tiến độ)
```

Lời giải **không** nằm trên đĩa — chỉ hiện khi bạn gọi `hint`/`solution`.

## Quy tắc tự đặt

Vật lộn ít nhất 10 phút rồi mới mở `hint`. Chỗ khó chịu đó chính là chỗ kiến thức bám lại.
Khi dùng `solution`, đọc hiểu rồi **tự gõ lại** — đừng copy-paste.
