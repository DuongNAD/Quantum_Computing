#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quantum Computing Zero → Hero · Bài Thực Hành Tương Tác Trong Terminal
Chạy bằng lệnh:
    py phase0/thuc_hanh_tuong_tac.py
    hoặc: python phase0/thuc_hanh_tuong_tac.py

Không yêu cầu cài Qiskit! Chạy 100% bằng thư viện chuẩn Python (hoặc numpy nếu có).
Hướng dẫn bạn tự tay thực hành:
    1. Trạng thái Qubit, Biên độ phức & Chuẩn hoá
    2. Cổng lượng tử 1-Qubit (X, Y, Z, H, S, T)
    3. Đo lường & Sụp đổ hàm sóng (Born rule)
    4. Vướng víu lượng tử 2-Qubit & Trạng thái Bell
    5. Mini-Quiz thử thách trực giác lượng tử
"""
import cmath
import math
import os
import random
import sys
import time

# Reconfigure stdout/stderr for Windows PowerShell & CMD UTF-8 support
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stdin, "reconfigure"):
    try:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# ANSI color codes
USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

def col(code, text):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text

CYAN = lambda s: col("36;1", s)
GREEN = lambda s: col("32;1", s)
YELLOW = lambda s: col("33;1", s)
MAGENTA = lambda s: col("35;1", s)
RED = lambda s: col("31;1", s)
BOLD = lambda s: col("1", s)
DIM = lambda s: col("2", s)

def safe_input(prompt=""):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)

def clear_screen():
    # Only clear if terminal
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")

def bar_chart(val, max_val=1.0, width=30):
    filled = int(round((val / max_val) * width)) if max_val > 0 else 0
    return "█" * filled + "░" * (width - filled)

def pause(prompt="\n[Bấm Enter để tiếp tục...]"):
    safe_input(DIM(prompt))

# ═══════════════════════════════════════════════════════════════════════════
# CHƯƠNG 1: BIÊN ĐỘ PHỨC & VECTOR TRẠNG THÁI
# ═══════════════════════════════════════════════════════════════════════════
def chapter_1_state():
    print(CYAN("\n" + "═" * 70))
    print(CYAN("  CHƯƠNG 1 · VECTOR TRẠNG THÁI & ĐIỀU KIỆN CHUẨN HÓA"))
    print(CYAN("═" * 70))
    print("""
Một qubit ở trạng thái tổng quát được biểu diễn bằng vector cột:
    |ψ⟩ = α|0⟩ + β|1⟩  = [ α ]
                         [ β ]
Trong đó α và β là hai SỐ PHỨC thỏa mãn điều kiện bảo toàn xác suất:
    |α|² + |β|² = 1
""")
    print("Hãy thử nhập một góc θ (độ) để tạo trạng thái:")
    print("    |ψ⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩")
    
    while True:
        try:
            val = safe_input(YELLOW("Nhập góc θ (0 đến 180 độ, ví dụ 0, 90, 180): ")).strip()
            if not val:
                deg = 90.0
            else:
                deg = float(val)
            break
        except ValueError:
            print(RED("Vui lòng nhập một số thực hợp lệ!"))

    rad = math.radians(deg)
    alpha = math.cos(rad / 2)
    beta = math.sin(rad / 2)
    p0 = alpha ** 2
    p1 = beta ** 2

    print(f"\n{BOLD('Kết quả tính toán với θ = ' + str(deg) + '°:')}")
    print(f"  Biên độ α = {alpha:.4f}  → Xác suất ra |0⟩: P(0) = |α|² = {p0*100:.1f}%")
    print(f"    |0⟩: {CYAN(bar_chart(p0))} {p0*100:.1f}%")
    print(f"  Biên độ β = {beta:.4f}  → Xác suất ra |1⟩: P(1) = |β|² = {p1*100:.1f}%")
    print(f"    |1⟩: {MAGENTA(bar_chart(p1))} {p1*100:.1f}%")
    print(f"  Tổng xác suất: {p0:.4f} + {p1:.4f} = {GREEN(f'{p0+p1:.4f}')} (Bảo toàn chuẩn 100%!)")

    if abs(deg - 90) < 1e-4:
        print(GREEN("\n⭐ Bạn vừa tạo trạng thái |+⟩ = (|0⟩ + |1⟩)/√2 — trạng thái chồng chập đều chuẩn mực!"))
    elif abs(deg) < 1e-4:
        print(GREEN("\n⭐ Trạng thái cơ sở tính toán |0⟩."))
    elif abs(deg - 180) < 1e-4:
        print(GREEN("\n⭐ Trạng thái cơ sở tính toán |1⟩."))

    pause()

# ═══════════════════════════════════════════════════════════════════════════
# CHƯƠNG 2: CỔNG LƯỢNG TỬ 1-QUBIT
# ═════════════════════════════════════════════════════════════════════════
def chapter_2_gates():
    print(CYAN("\n" + "═" * 70))
    print(CYAN("  CHƯƠNG 2 · TÁC ĐỘNG CỦA CÁC CỔNG LƯỢNG TỬ"))
    print(CYAN("═" * 70))
    print("""
Mỗi cổng lượng tử 1-qubit là một MA TRẬN 2×2 UNITARY (U†·U = I).
Cổng tác động lên vector bằng phép nhân ma trận với vector:
    |ψ'⟩ = U · |ψ⟩
""")
    GATES = {
        "X": ("Pauli-X (NOT lượng tử)", [[0, 1], [1, 0]], "Lật chỗ α và β: biến |0⟩ ↔ |1⟩"),
        "Z": ("Pauli-Z (Lật pha)", [[1, 0], [0, -1]], "Giữ nguyên |0⟩, đổi dấu |1⟩ thành −|1⟩"),
        "H": ("Hadamard (Tạo chồng chập)", [[1/math.sqrt(2), 1/math.sqrt(2)], [1/math.sqrt(2), -1/math.sqrt(2)]], "Biến |0⟩ → |+⟩ và |1⟩ → |−⟩"),
        "S": ("Cổng Phase S (Quay 90°)", [[1, 0], [0, 1j]], "Thêm pha e^(iπ/2) = i vào nhánh |1⟩"),
        "T": ("Cổng π/8 T (Quay 45°)", [[1, 0], [0, cmath.exp(1j * math.pi / 4)]], "Thêm pha e^(iπ/4) vào nhánh |1⟩")
    }

    # Bắt đầu với |0>
    state = [1.0 + 0j, 0.0 + 0j]
    history = ["|0⟩"]

    while True:
        print(f"\nTrạng thái hiện tại: {BOLD(f'[{state[0].real:.3f}+{state[0].imag:.3f}i, {state[1].real:.3f}+{state[1].imag:.3f}i]ᵀ')}")
        p0 = abs(state[0]) ** 2
        p1 = abs(state[1]) ** 2
        print(f"  P(0) = {p0*100:.1f}%  |  P(1) = {p1*100:.1f}%")
        print(f"  Lịch sử cổng đã áp: {CYAN(' → '.join(history))}")

        print("\nChọn cổng muốn áp lên qubit:")
        for k, (name, _, desc) in GATES.items():
            print(f"  [{BOLD(k)}] {name} — {DIM(desc)}")
        print("  [R] Đặt lại về |0⟩")
        print("  [XONG] Kết thúc chương 2")

        choice = safe_input(YELLOW("\nLựa chọn của bạn (X, Z, H, S, T, R, XONG): ")).strip().upper()
        if choice == "XONG" or choice == "Q":
            break
        elif choice == "R":
            state = [1.0 + 0j, 0.0 + 0j]
            history = ["|0⟩"]
            print(GREEN("✓ Đã đặt lại trạng thái về |0⟩"))
        elif choice in GATES:
            name, mat, _ = GATES[choice]
            a, b = state[0], state[1]
            new_a = mat[0][0] * a + mat[0][1] * b
            new_b = mat[1][0] * a + mat[1][1] * b
            state = [new_a, new_b]
            history.append(choice)
            print(GREEN(f"✓ Đã áp cổng {choice} ({name})"))
            if len(history) >= 3 and history[-1] == "H" and history[-2] == "H":
                print(YELLOW("  💡 Chú ý: H theo sau H triệt tiêu hoàn toàn giao thoa (H·H = I)!"))
        else:
            print(RED("Lựa chọn không hợp lệ!"))

    pause()

# ═════════════════════════════════════════════════════════════════════════
# CHƯƠNG 3: MÔ PHỎNG ĐO LƯỜNG & SỤP ĐỔ HÀM SÓNG
# ═════════════════════════════════════════════════════════════════════════
def chapter_3_measurement():
    print(CYAN("\n" + "═" * 70))
    print(CYAN("  CHƯƠNG 3 · MÔ PHỎNG ĐO LƯỜNG & SỤP ĐỔ HÀM SÓNG (BORN RULE)"))
    print(CYAN("═" * 70))
    print("""
Theo quy tắc Born: Khi đo một qubit ở trạng thái α|0⟩ + β|1⟩:
  - Bạn nhận được bit '0' với xác suất P(0) = |α|²
  - Bạn nhận được bit '1' với xác suất P(1) = |β|²
VÀ TRẠNG THÁI SẬP VỀ NHÁNH VỪA ĐO ĐƯỢC!
""")
    # Tạo trạng thái bất đối xứng
    # e.g., cos(pi/6)|0> + sin(pi/6)|1> => P(0) = 75%, P(1) = 25%
    rad = math.pi / 3 # theta = 60 deg -> theta/2 = 30 deg -> cos=sqrt(3)/2 ~ 0.866 (P0=0.75)
    alpha = math.cos(rad / 2)
    beta = math.sin(rad / 2)
    p0_true = alpha ** 2
    p1_true = beta ** 2

    print(f"Trạng thái chuẩn bị: |ψ⟩ = {alpha:.3f}|0⟩ + {beta:.3f}|1⟩")
    print(f"Xác suất lý thuyết: P(0) = {p0_true*100:.1f}%, P(1) = {p1_true*100:.1f}%\n")

    shots_str = safe_input(YELLOW("Bạn muốn bắn bao nhiêu lần đo (shots, ví dụ 10, 100, 1024, 10000): ")).strip()
    try:
        shots = int(shots_str) if shots_str else 1024
        if shots <= 0:
            print(YELLOW("Số shots phải ≥ 1! Tự động đặt về mặc định 1024."))
            shots = 1024
    except ValueError:
        shots = 1024

    print(f"\n{CYAN('Đang mô phỏng ' + str(shots) + ' lần đo...')}")
    count0 = 0
    count1 = 0
    for _ in range(shots):
        if random.random() < p0_true:
            count0 += 1
        else:
            count1 += 1

    ratio0 = count0 / shots
    ratio1 = count1 / shots

    print(f"\nKết quả sau {BOLD(str(shots))} lần đo:")
    print(f"  |0⟩: {count0:6d} lần ({ratio0*100:.2f}%) {CYAN(bar_chart(ratio0))}")
    print(f"  |1⟩: {count1:6d} lần ({ratio1*100:.2f}%) {MAGENTA(bar_chart(ratio1))}")
    print(f"  Sai số so với lý thuyết (|P_thực - P_lý_thuyết|): {abs(ratio0 - p0_true)*100:.3f}%")
    print(DIM("  (Khi số shots tăng lên, kết quả đo thực tế hội tụ về phân bố lý thuyết theo Luật Số Lớn!)"))

    print(BOLD("\nBây giờ thử Đo Duy Nhất 1 Lần để thấy Sụp Đổ Hàm Sóng:"))
    measured = 0 if random.random() < p0_true else 1
    print(f"  Kết quả đo được: {GREEN(f'|{measured}⟩')}")
    print(f"  Sau phép đo, trạng thái sụp đổ hoàn toàn về: {BOLD(f'|{measured}⟩')}")
    print(f"  Nếu bạn đo tiếp lần thứ 2: Chắc chắn {GREEN('100.0%')} ra lại kết quả |{measured}⟩!")

    pause()

# ═════════════════════════════════════════════════════════════════════════
# CHƯƠNG 4: VƯỚNG VÍU LƯỢNG TỬ & BELL STATE
# ═════════════════════════════════════════════════════════════════════════
def chapter_4_bell():
    print(CYAN("\n" + "═" * 70))
    print(CYAN("  CHƯƠNG 4 · VƯỚNG VÍU LƯỢNG TỬ & CẶP BELL |Φ⁺⟩"))
    print(CYAN("═" * 70))
    print("""
Trạng thái Bell |Φ⁺⟩ = (|00⟩ + |11⟩) / √2
Được tạo bằng 2 bước đơn giản:
    1. Áp cổng H lên Qubit 0 (tạo chồng chập)
    2. Áp cổng CNOT từ Qubit 0 sang Qubit 1 (vướng víu)
""")
    print("Mô phỏng đo cặp vướng víu giữa An (Trái Đất) và Bình (Sao Hỏa):")
    print("Mỗi lần bấm [Enter], một cặp hạt Bell được gửi đi và đo:")

    for round_no in range(1, 4):
        safe_input(YELLOW(f"\n[Bấm Enter để bắn Cặp Bell #{round_no}...]"))
        outcome = 0 if random.random() < 0.5 else 1
        print(f"  🪐 An đo Qubit 0 trên Trái Đất: {CYAN(f'Kết quả sụp đổ ngẫu nhiên ra |{outcome}⟩')}")
        time.sleep(0.3)
        print(f"  🚀 Bình đo Qubit 1 trên Sao Hỏa: {GREEN(f'TỨC THÌ sụp đổ ra chính xác |{outcome}⟩')}")
        print(f"     → Tương quan 100%! Không bao giờ xuất hiện cặp |01⟩ hay |10⟩.")

    print("""
💡 BÀI HỌC VÀNG:
Mặc dù Bình luôn thấy kết quả trùng khớp với An ngay lập tức,
Bình KHÔNG THỂ biết An muốn gửi thông điệp gì, vì bản thân kết quả của An
hoàn toàn ngẫu nhiên 50/50! Do đó, vướng víu KHÔNG truyền tin nhanh hơn ánh sáng
(Định lý No-Communication).
""")
    pause()

# ═════════════════════════════════════════════════════════════════════════
# CHƯƠNG 5: MINI-QUIZ KIỂM TRA HIỂU BIẾT
# ═════════════════════════════════════════════════════════════════════════
def chapter_5_quiz():
    print(CYAN("\n" + "═" * 70))
    print(CYAN("  CHƯƠNG 5 · THỬ THÁCH MINI-QUIZ (3 CÂU)"))
    print(CYAN("═" * 70))

    QUESTIONS = [
        {
            "q": "Cổng nào sau đây có tính chất H·H = I (áp 2 lần liên tiếp trở về trạng thái cũ)?",
            "opts": ["A. Chỉ riêng cổng X", "B. Chỉ riêng cổng H", "C. Cả cổng X, Y, Z và H đều là self-inverse (U² = I)", "D. Không có cổng nào"],
            "ans": "C",
            "exp": "Chính xác! Các cổng Pauli (X, Y, Z) và Hadamard (H) đều là ma trận Hermite và Unitary, do đó bình phương của chúng luôn bằng ma trận đơn vị I!"
        },
        {
            "q": "Nếu áp cổng H lên |0⟩ được |+⟩, thì áp cổng H lên |1⟩ sẽ được trạng thái nào?",
            "opts": ["A. |0⟩", "B. |+⟩", "C. |−⟩ = (|0⟩ − |1⟩)/√2", "D. Không xác định được"],
            "ans": "C",
            "exp": "Chính xác! H|1⟩ = (|0⟩ − |1⟩)/√2 = |−⟩ mang pha âm ở nhánh |1⟩."
        },
        {
            "q": "Để thực hiện Dịch Chuyển Lượng Tử (Quantum Teleportation) 1 qubit, cần tài nguyên gì?",
            "opts": ["A. Chỉ cần 1 cặp vướng víu Bell", "B. 1 cặp vướng víu Bell + 2 bit thông tin cổ điển", "C. 100 qubit phụ", "D. Dây cáp quang tốc độ cao"],
            "ans": "B",
            "exp": "Chính xác! Công thức vàng: 1 Cặp Entanglement + 2 Bit Cổ Điển = Truyền 1 Trạng Thái Qubit không thể nhân bản!"
        }
    ]

    score = 0
    for idx, item in enumerate(QUESTIONS, 1):
        print(f"\n{BOLD(f'Câu {idx}:')} {item['q']}")
        for opt in item["opts"]:
            print(f"  {opt}")
        while True:
            ans = safe_input(YELLOW("Đáp án của bạn (A/B/C/D): ")).strip().upper()
            if ans in ["A", "B", "C", "D"]:
                break
            print(RED("Vui lòng chỉ nhập A, B, C hoặc D!"))

        if ans == item["ans"]:
            print(GREEN(f"✓ CHÍNH XÁC! {item['exp']}"))
            score += 1
        else:
            print(RED(f"✗ Chưa đúng! Đáp án đúng là {item['ans']}. {item['exp']}"))

    print(CYAN("\n" + "═" * 50))
    print(f"Tổng kết điểm Quiz: {BOLD(f'{score} / {len(QUESTIONS)} câu')}")
    if score == len(QUESTIONS):
        print(GREEN("🏆 Xuất sắc! Bạn đã nắm rất vững các trực giác cốt lõi của điện toán lượng tử!"))
    else:
        print(YELLOW("Hãy mở slide Phase 0 và Phase 1 để ôn lại các khái niệm còn bỡ ngỡ nhé!"))
    print(CYAN("═" * 50))
    pause()

# ═════════════════════════════════════════════════════════════════════════
# MENU CHÍNH
# ═════════════════════════════════════════════════════════════════════════
def main():
    while True:
        clear_screen()
        print(CYAN("╔════════════════════════════════════════════════════════════════════╗"))
        print(CYAN("║       QUANTUM COMPUTING ZERO → HERO · WORKSHOP THỰC HÀNH           ║"))
        print(CYAN("║       Học Bằng Thực Hành Trực Tiếp · Chạy 100% Trong Terminal      ║"))
        print(CYAN("╚════════════════════════════════════════════════════════════════════╝"))
        print(f"""
Chọn một bài thực hành để bắt đầu:
  [{BOLD('1')}] Chương 1: Vector trạng thái & Điều kiện chuẩn hoá (|α|² + |β|² = 1)
  [{BOLD('2')}] Chương 2: Thử nghiệm tác động các cổng 1-qubit (X, Y, Z, H, S, T)
  [{BOLD('3')}] Chương 3: Mô phỏng đo lường & Sụp đổ hàm sóng (Born Rule)
  [{BOLD('4')}] Chương 4: Vướng víu lượng tử & Trạng thái Bell |Φ⁺⟩
  [{BOLD('5')}] Chương 5: Mini-Quiz thử thách trực giác lượng tử
  [{BOLD('A')}] Chạy toàn bộ lần lượt từ Chương 1 đến 5
  [{BOLD('Q')}] Thoát
""")
        choice = safe_input(YELLOW("Lựa chọn của bạn (1-5, A, Q): ")).strip().upper()
        if choice == "1":
            chapter_1_state()
        elif choice == "2":
            chapter_2_gates()
        elif choice == "3":
            chapter_3_measurement()
        elif choice == "4":
            chapter_4_bell()
        elif choice == "5":
            chapter_5_quiz()
        elif choice == "A":
            chapter_1_state()
            chapter_2_gates()
            chapter_3_measurement()
            chapter_4_bell()
            chapter_5_quiz()
        elif choice == "Q":
            print(GREEN("\nChúc bạn học tập hiệu quả trên con đường Quantum Computing Zero → Hero! Tạm biệt!\n"))
            break

if __name__ == "__main__":
    main()
