# ══════════════════════════════════════════════════════════════════════════════
# BÀI 332/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.2
#   Gợi ý:      python qk.py hint MagicSquareGame/2.2
#   Lời giải:   python qk.py solution MagicSquareGame/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Magic square observables
# Input:  A row and column indices corresponding to a cell in a magic square.
# Output: A tuple that represents the given cell of a magic square.
#         The first element of the tuple is an int denoting the sign of the observable (+1 for plus, -1 for minus),
#         the second - a list of 2 Pauli observables.
# The square should satisfy the following properties:
#  1) The observables in each row and column mutually commute,
#  2) The product of observables in each row is I,
#  3) The product of observables in each column is -I.
#
# Note: We'll use a standard magic square from Mermin-Peres game literature.

from enum import Enum

class Pauli(Enum):
    I = "I"
    X = "X"
    Y = "Y"
    Z = "Z"

def get_magic_observables(row_index: int, column_index: int) -> tuple[int, list[Pauli]]:
    """
    Get the magic square observable for the given cell.

    Args:
        row_index: Row index (0, 1, or 2)
        column_index: Column index (0, 1, or 2)

    Returns:
        Tuple of (sign, [pauli1, pauli2]) for the cell
    """
    # Your code here
    pass
