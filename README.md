# Quantum Computing · Zero → Hero

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-2.5%2B-6929C4.svg?logo=qiskit&logoColor=white)](https://qiskit.org/)
[![Exercises](https://img.shields.io/badge/Katas-350%2F350%20Verified-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/qsim%20tests-39%20Passing-success.svg)]()

Bộ tài liệu tự học điện toán lượng tử theo hướng **thực hành trước, lý thuyết khi bí**.
Toàn bộ chạy offline, không cần mạng sau khi đã cài xong.

```
├── slides/          5 deck bài giảng có mạch lượng tử bấm được (mở bằng trình duyệt)
├── docs/            6 trang tra cứu: thuật ngữ, bảng cổng, ký hiệu, FAQ, kế hoạch
├── katas/           350 bài tập chấm tự động, xếp theo 9 bậc
├── qsim/            khung code Phase 1 — bạn tự viết simulator, có 39 test
└── lo-trinh-quantum-zero-to-hero.md    lộ trình đầy đủ dạng văn bản
```

## Bắt đầu

```bash
source ~/quantum-env/bin/activate
open slides/index.html
```

Rồi đi theo đúng thứ tự này:

| Bước | Việc | Thời gian |
|---|---|---|
| 1 | Đọc deck `slides/phase0.html` (24 slide, 4 bàn thí nghiệm bấm được) | ~45 phút |
| 2 | Bật hệ thống kata: `cd katas && python qk.py` | 5 phút |
| 3 | Làm Bậc 1–2 (25 bài) song song với deck Phase 0 | ~3 giờ |
| 4 | Sang `slides/phase1.html` + `qsim/` | 2 tuần |

## Hệ thống luyện tập (`katas/`)

350 bài lấy từ [`qiskit-community/Qiskit-QuantumKatas`](https://github.com/qiskit-community/Qiskit-QuantumKatas)
(Apache-2.0) — bộ này gốc là **dataset benchmark đánh giá LLM**, không phải khoá học.
Ở đây nó đã được:

- sắp xếp lại thành **9 bậc theo thứ tự sư phạm** (bộ gốc không có thứ tự)
- bọc thành file bài tập riêng lẻ có TODO
- gắn runner chấm tự động kiểu `rustlings`
- **kiểm chứng 350/350 chạy đúng** trên Qiskit 2.5.1 + Aer 0.17.2 + Python 3.11.8

```bash
cd katas
python qk.py                  # bảng tiến độ + bài kế tiếp
python qk.py next             # đọc đề đầy đủ
python qk.py run              # chấm bài đang làm
python qk.py watch            # tự chấm mỗi khi lưu file  ← khuyên dùng
python qk.py hint <id>        # gợi ý 3 mức tăng dần
python qk.py solution <id>    # lời giải chuẩn
python qk.py list --bac 2     # liệt kê một bậc
python qk.py reset <id>       # làm lại từ đầu
```

`<id>` viết được nhiều kiểu: `BasicGates/1.1`, `1.1`, `state_flip`, hoặc số thứ tự `42`.

### 9 bậc

| Bậc | Nội dung | Bài | Phase |
|---|---|---|---|
| 1 | Toán nền — số phức & vector | 4 | P1 |
| 2 | Qubit đầu tiên — cổng 1 qubit | 21 | P0–1 |
| 3 | Nhiều qubit & vướng víu | 36 | P1 |
| 4 | Đo lường | 31 | P1 |
| 5 | Giao thức lượng tử | 37 | P2 |
| 6 | Oracle & thuật toán kinh điển | 59 | P2 |
| 7 | QFT & Phase Estimation | 23 | P2 |
| 8 | Mạch nâng cao & ứng dụng | 100 | P3 |
| 9 | Nghịch lý lượng tử & sửa lỗi | 39 | P4 |

## Simulator tự viết (`qsim/`)

Deliverable của Phase 1. `qsim/qsim.py` là khung có TODO; `qsim/test_qsim.py` có 39 test
xếp theo 5 mốc, mốc cuối so trực tiếp với `qiskit-aer` trên mạch ngẫu nhiên.

```bash
cd qsim
pytest test_qsim.py -x -q     # -x = dừng ở lỗi đầu tiên
```

Test đầu sẽ báo `X vẫn còn None — điền ma trận đi`. Đó là việc kế tiếp của bạn.

## Tài liệu tra cứu (`docs/`)

Sáu trang, không trang nào cần đọc từ đầu tới cuối — mở khi bí rồi đóng lại.

| Trang | Mở khi nào |
|---|---|
| [`docs/thuat-ngu.md`](docs/thuat-ngu.md) | Gặp một từ tiếng Anh không chắc nghĩa (90+ mục) |
| [`docs/bang-tra-cong.md`](docs/bang-tra-cong.md) | Cần ma trận cổng, đẳng thức, hoặc khuôn mẫu API Qiskit 2.x |
| [`docs/ky-hieu-toan.md`](docs/ky-hieu-toan.md) | Không đọc được công thức: bra-ket, `⊗`, `†`, endianness |
| [`docs/faq-loi-hay-gap.md`](docs/faq-loi-hay-gap.md) | Code không chạy, hoặc ra kết quả lạ — sắp theo **triệu chứng** |
| [`docs/ke-hoach-18-tuan.md`](docs/ke-hoach-18-tuan.md) | Bản theo dõi từng tuần, có "cửa ải" cho mỗi phase |
| [`docs/huong-dan-slide.md`](docs/huong-dan-slide.md) | Muốn sửa slide hoặc viết deck mới |

## Slides

Mở `slides/index.html` bằng trình duyệt bất kỳ. Không cần build, không cần mạng,
không phụ thuộc CDN nào.

### Mạch lượng tử bấm được ngay trong slide

Mỗi deck có vài **bàn thí nghiệm** chạy simulator state-vector viết bằng JavaScript
thuần (`slides/assets/qlab.js`). Bấm cổng vào mạch, xem biên độ phức, đĩa pha, quả
cầu Bloch, và histogram thay đổi tức thì — kèm nút tua **"xem trạng thái sau bước k"**
để mổ xẻ giao thoa từng bước, và khối hiện **mã Qiskit tương ứng** với mạch đang có.

| Deck | Bàn thí nghiệm |
|---|---|
| Phase 0 | 1 qubit tự do · giao thoa H·H từng bước · quả cầu Bloch · Bell state & vướng víu |
| Phase 1 | endianness trên 3 qubit · ghép cặp biên độ |
| Phase 2 | phase kickback (so hai mạch) · Grover 2 qubit chạy đủ vòng |
| Phase 4–5 | mã sửa lỗi bit-flip — tự tạo lỗi rồi tự thấy syndrome |

### Điều hướng

| Phím | Việc |
|---|---|
| `→` `Space` `J` | ý tiếp theo, hết ý thì sang slide sau |
| `Shift + →` | bỏ qua, sang thẳng slide sau |
| `←` `K` | lùi lại |
| `1`–`9` | nhảy tới slide |
| `O` | mục lục (chia chương, có dấu ✓ slide đã hiểu) |
| `/` | tìm trong deck — **không cần gõ dấu tiếng Việt** |
| `D` | đánh dấu slide "đã hiểu" |
| `N` | hiện/ẩn ghi chú của người dạy |
| `F` | toàn màn hình |
| `P` | in ra PDF (tự bung mọi phần đang ẩn) |
| `?` | bảng phím tắt |

Vị trí đang học, checklist đã tick và slide đã đánh dấu được nhớ riêng cho từng deck
(lưu trong `localStorage`, không gửi đi đâu).

### Muốn trang chủ hiện tiến độ kata thật

Trang chủ đọc `slides/assets/progress.json`, nhưng `fetch()` bị chặn khi mở bằng
`file://`. Cách bật:

```bash
python katas/qk.py progress          # xuất tiến độ
cd slides && python -m http.server 8000
```

Rồi mở <http://localhost:8000>.

## Môi trường

Đã cài sẵn ở `~/quantum-env` (Python 3.11.8):

| Gói | Bản |
|---|---|
| qiskit | 2.5.1 |
| qiskit-aer | 0.17.2 |
| qiskit-ibm-runtime | 0.48.0 |
| numpy | 2.4.6 |
| scipy | 1.17.1 |
| matplotlib | 3.11.1 |
| pytest | 9.1.1 |
| jupyterlab | 4.6.2 |

Tiện tay thì thêm alias vào `~/.zshrc`:

```bash
alias qenv="source ~/quantum-env/bin/activate"
```

> **Lưu ý khi di chuyển env:** virtualenv nhúng đường dẫn tuyệt đối vào `bin/*` và
> `pyvenv.cfg`. `mv` thẳng sẽ làm hỏng `pip`, `jupyter`, `pytest`. Muốn đổi chỗ thì
> tạo lại env mới rồi cài lại từ `requirements.txt`.

---

## 👤 Tác Giả & Đóng Góp

- **Dương Nguyễn** — [@DuongNAD](https://github.com/DuongNAD)
- Tham khảo bài tập: [Qiskit Quantum Katas](https://github.com/qiskit-community/Qiskit-QuantumKatas) (Apache-2.0)
