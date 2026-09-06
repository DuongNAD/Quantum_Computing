# ══════════════════════════════════════════════════════════════════════════════
# BÀI 320/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# GHZGame/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GHZGame/1.1
#   Gợi ý:      python qk.py hint GHZGame/1.1
#   Lời giải:   python qk.py solution GHZGame/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Win condition
# Input:
#     1) Alice, Bob and Charlie's input bits (r, s and t), stored as a list of length 3,
#     2) Alice, Bob and Charlie's output bits (a, b and c), stored as a list of length 3.
# The input bits will have zero or two bits set to True.
# Output:
#     True if Alice, Bob and Charlie won the GHZ game, that is, if r ∨ s ∨ t = a ⊕ b ⊕ c,
#     and False otherwise.
#
# The GHZ game: Three players get bits with 0 or 2 bits set to True.
# They must return bits such that (r OR s OR t) equals (a XOR b XOR c).

def win_condition(rst: list[bool], abc: list[bool]) -> bool:
    """
    Check if players won the GHZ game.

    Args:
        rst: Input bits [r, s, t] for Alice, Bob, Charlie
        abc: Output bits [a, b, c] from Alice, Bob, Charlie

    Returns:
        True if they won (r ∨ s ∨ t = a ⊕ b ⊕ c), False otherwise
    """
    # Your code here
    pass
