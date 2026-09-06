# ══════════════════════════════════════════════════════════════════════════════
# BÀI 338/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/3.1
#   Gợi ý:      python qk.py hint MagicSquareGame/3.1
#   Lời giải:   python qk.py solution MagicSquareGame/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1. Testing magic square strategies
# Goal:
#    Use your classical and quantum magic square strategies to
#    verify their probabilities of winning. This is an experimental/testing task.

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
    """Helper: Check win condition."""
    if not valid_alice_move(row) or not valid_bob_move(column):
        return False
    return row[column_index] == column[row_index]

def alice_classical(row_index: int) -> list[int]:
    """Helper: Alice's classical strategy."""
    strategies = [
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1]
    ]
    return strategies[row_index]

def bob_classical(column_index: int) -> list[int]:
    """Helper: Bob's classical strategy."""
    strategies = [
        [1, 1, -1],
        [1, -1, 1],
        [-1, -1, -1]
    ]
    return strategies[column_index]

def test_magic_square_strategies() -> dict:
    """
    Test both classical and quantum magic square strategies.

    Returns:
        Dictionary with test results and win rates
    """
    # Your code here - test the strategies
    pass
