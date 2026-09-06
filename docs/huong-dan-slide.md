# Hướng dẫn tự viết slide

Bộ deck này **không dùng framework nào** — không reveal.js, không CDN, không build
step. Chỉ có ba file trong `slides/assets/`:

| File | Việc |
|---|---|
| `theme.css` | toàn bộ design system |
| `deck.js` | điều hướng, fragment, quiz, tìm kiếm, checklist, tô màu code |
| `qlab.js` | simulator lượng tử bằng JS + widget mạch tương tác |

Muốn thêm một deck mới: copy khung dưới đây, viết nội dung, mở bằng trình duyệt.
Không cần cài gì.

---

## 1. Khung file tối thiểu

```html
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tên deck · Quantum Zero→Hero</title>
<link rel="stylesheet" href="assets/theme.css">
</head>
<body data-deck="ten-deck">
<div class="deck">

  <div class="slide" data-part="Chương 1" data-title="Tiêu đề trong mục lục">
    <div class="wrap">
      <h2><span class="k">01</span> Tiêu đề hiện trên slide</h2>
      <p>Nội dung.</p>
    </div>
  </div>

</div>
<script src="assets/qlab.js"></script>
<script src="assets/deck.js"></script>
</body>
</html>
```

Quy tắc:

- `body[data-deck]` quyết định khoá lưu tiến độ trong `localStorage`. **Phải khác
  nhau giữa các deck**, nếu không hai deck sẽ ghi đè tiến độ của nhau.
- `.slide[data-title]` là chữ hiện trong mục lục (phím `O`) và trong kết quả tìm
  kiếm (phím `/`).
- `.slide[data-part]` gom nhóm slide trong mục lục. Chỉ cần đặt ở **slide đầu tiên**
  của mỗi nhóm.
- `.wrap` giới hạn 1080px; `.wrap.wide` giới hạn 1280px — dùng khi có widget hoặc
  bảng rộng.
- `qlab.js` phải nạp **trước** `deck.js`.

## 2. Bố cục

```html
<div class="grid">…</div>      <!-- auto-fit, tối thiểu 230px -->
<div class="grid-2">…</div>    <!-- auto-fit, tối thiểu 300px -->
<div class="grid-3">…</div>    <!-- auto-fit, tối thiểu 190px -->
<div class="row">…</div>       <!-- flex ngang, tự xuống dòng -->
```

Thẻ có màu ngữ nghĩa:

```html
<div class="card">…</div>          <!-- trung tính -->
<div class="card good">…</div>     <!-- xanh lá: cách đúng -->
<div class="card warn">…</div>     <!-- vàng: cảnh báo -->
<div class="card bad">…</div>      <!-- đỏ: cách sai / hiểu lầm -->
<div class="card info">…</div>     <!-- xanh dương: giải thích thêm -->
<div class="card pad-lg">…</div>   <!-- padding rộng hơn -->
```

Dòng thời gian dọc:

```html
<div class="steps-v">
  <div class="sv"><span class="dot">1</span><div class="body">
    <b>Tiêu đề bước</b><span class="tiny">Mô tả</span>
  </div></div>
</div>
```

## 3. Chữ & ký hiệu

```html
<p class="lead">Câu mở đầu, chữ to hơn</p>
<p class="sub">Câu phụ, chữ xám</p>
<p class="tiny">Ghi chú nhỏ</p>
<em class="q">nhấn mạnh màu tím</em>
<span class="ket">|ψ⟩</span>                        <!-- ket, font mono, màu cyan -->
<span class="frac"><span class="num">1</span><span class="den">√2</span></span>
<div class="note"><b>Nói thẳng:</b> …</div>          <!-- khối viền tím bên trái -->
```

Chip nhãn:

```html
<span class="chip">trung tính</span>
<span class="chip cyan">·</span>  <span class="chip violet">·</span>
<span class="chip amber">·</span> <span class="chip green">·</span>
<span class="chip rose">·</span>
```

## 4. Khối code

```html
<div class="code-head"><div class="dots"><i></i><i></i><i></i></div><span>ten_file.py</span></div>
<pre class="code" data-lang="python">import numpy as np</pre>
```

`data-lang` nhận `python` (mặc định), `bash`, `rust`, `text`. Nút **copy** được gắn
tự động vào `.code-head`. Tô màu do `deck.js` làm, không cần thư viện ngoài.

Trong `<pre>` phải escape `<`, `>`, `&` thành `&lt;` `&gt;` `&amp;`.

## 5. Khối bài tập & phần hé lộ

```html
<div class="ex">
  <div class="ex-head">
    <span class="ex-tag">Thực hành 0.2</span>
    <span class="ex-title">Tên bài</span>
    <span class="chip">5 phút</span>
  </div>
  <div class="ex-body">
    <p>Đề bài.</p>
  </div>
  <details class="reveal"><summary>Gợi ý / đáp án</summary>
    <div class="reveal-in"><p>Nội dung ẩn.</p></div>
  </details>
</div>
```

## 6. Quiz

```html
<div class="quiz">
  <span class="q-tag">Quiz 1</span>
  <p class="q-text">Câu hỏi?</p>
  <div class="opts">
    <button class="opt" data-why="Vì sao đáp án này sai.">Đáp án sai</button>
    <button class="opt" data-ok="1" data-why="Vì sao đáp án này đúng.">Đáp án đúng</button>
  </div>
  <div class="why">Giải thích chung, hiện sau khi trả lời.</div>
</div>
```

- `data-ok="1"` đánh dấu đáp án đúng (đúng **một** nút).
- `data-why` (tuỳ chọn) là giải thích riêng cho đáp án người học vừa chọn — hiệu quả
  hơn nhiều so với chỉ có một đoạn giải thích chung.
- Nhãn A/B/C/D và nút **"Làm lại câu này"** được thêm tự động.
- Tổng điểm của cả deck hiện trên thanh dưới.

## 7. Fragment — hé lộ từng ý

Thêm `class="frag"` vào bất kỳ phần tử nào. Phím `→` sẽ hiện lần lượt từng cái, hết
mới sang slide sau. `Shift + →` bỏ qua.

```html
<div class="card frag">Hiện ở lần bấm → thứ nhất</div>
<div class="card frag">Hiện ở lần thứ hai</div>
<div class="card frag ghost">Biến thể: mờ sẵn thay vì ẩn hẳn (giữ layout ổn định)</div>
```

Dùng khi bạn muốn người học **đoán trước khi thấy đáp án**. Đừng dùng cho mọi thứ —
slide toàn fragment thì mệt hơn là hữu ích.

## 8. Checklist nhớ được

```html
<div class="row" style="justify-content:space-between">
  <h3>Việc cần làm</h3>
  <span data-check-count="#p0-check">0/3</span>
</div>
<ul class="check" id="p0-check">
  <li><b>Việc 1</b> — mô tả</li>
  <li><b>Việc 2</b> — mô tả</li>
  <li><b>Việc 3</b> — mô tả</li>
</ul>
```

Trạng thái tick lưu trong `localStorage` theo từng deck. `data-check-count` trỏ tới
`id` của danh sách và tự cập nhật `2/3`.

## 9. Ghi chú của người dạy

```html
<div class="notes">Chỉ hiện khi bấm phím N. Dùng để ghi ý đồ sư phạm, thời lượng,
câu hỏi nên đặt cho lớp.</div>
```

Khi in PDF thì phần này **được in ra**.

## 10. Mạch vẽ tĩnh

Khi chỉ cần một hình minh hoạ, không cần tương tác:

```html
<div class="circ">
  <div class="wire">
    <span class="lbl">q₀</span><span class="ln"></span>
    <span class="g">H</span><span class="ln"></span>
    <span class="ctrl vlink"><b></b></span><span class="ln"></span>
    <span class="m">📊</span>
  </div>
  <div class="wire">
    <span class="lbl">q₁</span><span class="ln"></span>
    <span class="targ"><b>⊕</b></span><span class="ln"></span>
  </div>
</div>
```

`.circ.sm` là biến thể nhỏ, để nhét vào trong thẻ hẹp.
`.g.v` cho ô cổng màu tím.

## 11. Thanh dữ liệu

```html
<div class="bars">
  <div class="b"><span class="k">|0⟩</span>
    <span class="track"><span class="fill" data-w="51"></span></span>
    <span class="v">2086</span></div>
  <div class="b mute">…</div>     <!-- xám, dùng cho giá trị 0 -->
</div>
```

`data-w` là phần trăm chiều rộng; thanh chạy animation mỗi khi slide hiện ra.

## 12. QLab — mạch tương tác

Đây là thứ mạnh nhất trong bộ công cụ: một simulator state-vector thật, chạy trong
trình duyệt, không cần mạng.

```html
<div class="qlab"
     data-n="2"
     data-gates="H0, CX0-1"
     data-title="Mạch Bell"
     data-goal="Thử xoá CNOT xem còn vướng víu không."
     data-shots="1024"
     data-hide="bloch"
     data-lock="0"></div>
```

| Thuộc tính | Ý nghĩa |
|---|---|
| `data-n` | số qubit, 1–4 |
| `data-gates` | mạch nạp sẵn, ngăn bởi dấu phẩy |
| `data-title` | tiêu đề trên đầu widget |
| `data-goal` | dòng gợi ý màu vàng — **nên luôn có**, nói rõ cần thử gì |
| `data-shots` | số lần đo khi bấm nút ▶ (mặc định 1024) |
| `data-hide` | ẩn panel: `bloch`, `hist`, `amp`, `circ` — ngăn bởi dấu phẩy |
| `data-lock` | `"1"` = chỉ xem, giấu bảng cổng |

Cú pháp `data-gates`:

| Viết | Nghĩa |
|---|---|
| `H0` | H lên qubit 0 |
| `X1` | X lên qubit 1 |
| `CX0-1` | CNOT, control q0, target q1 |
| `CZ0-1` | CZ giữa q0 và q1 |
| `SWAP0-1` | tráo q0 và q1 |
| `RZ1:0.5` | Rz góc `0.5·π` lên q1 (đơn vị là **bội của π**) |
| `M0` | đo giữa mạch trên q0 (phá huỷ pha) |

Ví dụ đầy đủ: `data-gates="H0, H1, CZ0-1, H0, H1, X0, X1, CZ0-1, X0, X1, H0, H1"`
— đây là Grover một vòng trên 2 qubit.

Widget tự làm những việc sau, không cần bạn viết gì thêm:

- vẽ mạch (bấm vào cổng để xoá)
- bảng biên độ + đĩa pha + thanh xác suất
- quả cầu Bloch (khi `n = 1`)
- histogram khi bấm ▶
- nút tua **"xem trạng thái sau bước k"**
- một dòng **đọc hiểu bằng tiếng Việt** (chồng chập? vướng víu? có pha lệch?)
- khối `<details>` hiện **mã Qiskit tương ứng** với mạch đang có

### Dùng QLab ngoài slide

`qlab.js` cũng xuất API để dùng trong Console hoặc trong trang khác:

```js
const S = QLab.Sim;
const st = S.run(2, QLab.parseGates("H0, CX0-1"));
S.probs(st);       // Float64Array [0.5, 0, 0, 0.5]
S.bloch(st);       // chỉ có nghĩa khi n = 1
S.entangled2(st);  // true
S.sample(st, 1000);
```

## 13. Phím tắt (do `deck.js` cung cấp)

| Phím | Việc |
|---|---|
| `→` `Space` `J` | ý tiếp theo, rồi slide tiếp |
| `Shift + →` | bỏ qua fragment, sang thẳng slide sau |
| `←` `K` | lùi lại |
| `1`–`9` | nhảy tới slide |
| `O` | mục lục (có chia chương, có dấu ✓) |
| `/` | tìm trong deck — **không cần gõ dấu tiếng Việt** |
| `D` | đánh dấu slide "đã hiểu" |
| `N` | hiện/ẩn ghi chú |
| `F` | toàn màn hình |
| `P` | in PDF (tự bung mọi fragment và `<details>`) |
| `?` | bảng phím tắt |

## 14. Quy ước nội dung

Vài quy ước làm cho các deck đọc như một bộ, không phải như nhiều người viết rời:

- **Tiêu đề slide là một câu khẳng định**, không phải một danh từ. "Cổng lượng tử là
  phép quay, không phải if/else" tốt hơn "Cổng lượng tử".
- **Mỗi slide đúng một ý.** Nếu phải cuộn nhiều thì tách slide.
- **Nói thẳng chỗ dễ sai**, đặt trong `.card warn` hoặc `.card bad`. Người học nhớ
  cảnh báo lâu hơn nhớ định nghĩa.
- **Có widget thì luôn có `data-goal`.** Widget không có nhiệm vụ cụ thể thì người
  học chỉ nhìn rồi đi tiếp.
- **Kết mỗi deck bằng checklist tick được** + 2–3 câu tự kiểm tra trả lời không nhìn
  slide.
