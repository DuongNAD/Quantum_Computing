# ══════════════════════════════════════════════════════════════════════════════
# BÀI 220/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/9
#   Gợi ý:      python qk.py hint TruthTables/9
#   Lời giải:   python qk.py solution TruthTables/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. Find all true input assignments in a truth table
# Goal: Return an array that contains all input assignments in a truth table
#       that have a true truth value. These input assignments are called minterms.
#       The order of assignments in the return does not matter.
#
# Example: The truth table of 2-input OR is 0b1110, i.e., its minterms are [1, 2, 3].

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def all_minterms(tt: TruthTable) -> list[int]:
    """
    Find all input assignments that make the truth table true.

    Args:
        tt: Input truth table

    Returns:
        List of integers representing the true assignments (minterms)
    """
    # Your code here
    pass
