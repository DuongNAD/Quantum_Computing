# ══════════════════════════════════════════════════════════════════════════════
# BÀI 330/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/1.3
#   Gợi ý:      python qk.py hint MagicSquareGame/1.3
#   Lời giải:   python qk.py solution MagicSquareGame/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Alice and Bob's classical strategy
# In this task you have to implement two functions, one for Alice's classical strategy and one for Bob's.
# The classical strategy should win about 89% of the time.
#
# Alice's input: The index of Alice's row (0, 1, or 2).
# Alice's output: The signs Alice should place in her row (as a list of 3 integers).
#                 +1 indicates plus sign, -1 - minus sign.
#
# Bob's input: The index of Bob's column (0, 1, or 2).
# Bob's output: The signs Bob should place in his column (as a list of 3 integers).
#               +1 indicates plus sign, -1 - minus sign.

def alice_classical(row_index: int) -> list[int]:
    """
    Alice's classical strategy for the magic square game.

    Args:
        row_index: The index of Alice's assigned row (0, 1, or 2)

    Returns:
        List of 3 integers (+1 or -1) representing Alice's row
    """
    # Your code here
    pass

def bob_classical(column_index: int) -> list[int]:
    """
    Bob's classical strategy for the magic square game.

    Args:
        column_index: The index of Bob's assigned column (0, 1, or 2)

    Returns:
        List of 3 integers (+1 or -1) representing Bob's column
    """
    # Your code here
    pass
