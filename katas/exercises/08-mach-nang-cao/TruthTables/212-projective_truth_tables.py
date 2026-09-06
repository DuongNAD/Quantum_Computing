# ══════════════════════════════════════════════════════════════════════════════
# BÀI 212/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/1
#   Gợi ý:      python qk.py hint TruthTables/1
#   Lời giải:   python qk.py solution TruthTables/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Projective functions (elementary variables)
# Goal: Describe the three projective functions x₁, x₂, x₃ represented by integers.
#       Each of them is a 3-input function, i.e., f(x₃, x₂, x₁) : {0, 1}³ → {0, 1}.
#
# We use the following convention:
# x₁ is the least significant input.
# x₃ is the most significant input.
#
# Example: The function x₁ (least significant input) is given as an example.
#          The function is true for assignments 001, 011, 101, and 111,
#          since for all these assignments their least significant bit x₁ = 1.
#          This gives truth table 0b10101010.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def projective_truth_tables() -> tuple[TruthTable, TruthTable, TruthTable]:
    """
    Return the three projective functions x₁, x₂, x₃.

    Returns:
        Tuple of (x1, x2, x3) truth tables
    """
    x1 = TruthTable(0b10101010, 3)  # Given example
    # Your code here - compute x2 and x3
    x2 = TruthTable(0, 0)  # Update this
    x3 = TruthTable(0, 0)  # Update this

    return (x1, x2, x3)
