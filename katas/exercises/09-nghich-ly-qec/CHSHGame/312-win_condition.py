# ══════════════════════════════════════════════════════════════════════════════
# BÀI 312/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/1.1
#   Gợi ý:      python qk.py hint CHSHGame/1.1
#   Lời giải:   python qk.py solution CHSHGame/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Win condition
# Input:
#     1) Alice and Bob's starting bits (X and Y),
#     2) Alice and Bob's output bits (A and B).
# Output:
#     True if Alice and Bob won the CHSH game, that is, if X ∧ Y = A ⊕ B,
#     and false otherwise.
#
# The CHSH game: Alice gets bit X, Bob gets bit Y. They must return bits A and B
# such that X AND Y equals A XOR B, without communicating during the game.

def win_condition(x: bool, y: bool, a: bool, b: bool) -> bool:
    """
    Check if Alice and Bob won the CHSH game.

    Args:
        x: Alice's input bit
        y: Bob's input bit
        a: Alice's output bit
        b: Bob's output bit

    Returns:
        True if they won (X ∧ Y = A ⊕ B), False otherwise
    """
    # Your code here
    pass
