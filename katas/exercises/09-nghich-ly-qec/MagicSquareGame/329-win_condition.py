# ══════════════════════════════════════════════════════════════════════════════
# BÀI 329/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/1.2
#   Gợi ý:      python qk.py hint MagicSquareGame/1.2
#   Lời giải:   python qk.py solution MagicSquareGame/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Win condition
# Inputs:
#     1) The row and column indices Alice and Bob were assigned. Each index will be between 0 and 2, inclusive.
#     2) Alice and Bob's moves, represented as Int arrays of length 3.
# Output:
#     True if Alice and Bob won the game (that is, if both their moves are valid and
#     they chose the same sign in the cell on the intersection of Alice's row and Bob's column),
#     and false otherwise.

def valid_alice_move(cells: list[int]) -> bool:
    """Helper: Validate Alice's move."""
    for cell in cells:
        if cell != 1 and cell != -1:
            return False
    minus_count = sum(1 for cell in cells if cell == -1)
    return minus_count % 2 == 0

def valid_bob_move(cells: list[int]) -> bool:
    """Helper: Validate Bob's move."""
    for cell in cells:
        if cell != 1 and cell != -1:
            return False
    minus_count = sum(1 for cell in cells if cell == -1)
    return minus_count % 2 == 1

def win_condition(row_index: int, column_index: int, row: list[int], column: list[int]) -> bool:
    """
    Check if Alice and Bob won the magic square game.

    Args:
        row_index: Alice's assigned row index (0-2)
        column_index: Bob's assigned column index (0-2)
        row: Alice's move (3 integers)
        column: Bob's move (3 integers)

    Returns:
        True if both moves are valid and they agree on the intersection cell
    """
    # Your code here
    pass
