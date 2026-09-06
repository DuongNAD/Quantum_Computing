# ══════════════════════════════════════════════════════════════════════════════
# BÀI 218/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/7
#   Gợi ý:      python qk.py hint TruthTables/7
#   Lời giải:   python qk.py solution TruthTables/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Compute NOT of a truth table
# Goal: Compute a truth table that computes negation of a truth table.
#
# Hint: Be careful not to set bits in the integer that are out-of-range
#       in the truth table.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def tt_not(tt: TruthTable) -> TruthTable:
    """
    Compute the NOT of a truth table.

    Args:
        tt: Input truth table

    Returns:
        Truth table representing NOT tt
    """
    # Your code here
    pass
