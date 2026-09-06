# ══════════════════════════════════════════════════════════════════════════════
# BÀI 216/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/5
#   Gợi ý:      python qk.py hint TruthTables/5
#   Lời giải:   python qk.py solution TruthTables/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Compute OR of two truth tables
# Goal: Compute a truth table that computes the disjunction (OR)
#       of two truth tables.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def tt_or(tt1: TruthTable, tt2: TruthTable) -> TruthTable:
    """
    Compute the OR of two truth tables.

    Args:
        tt1: First truth table
        tt2: Second truth table

    Returns:
        Truth table representing tt1 OR tt2
    """
    assert tt1.num_vars == tt2.num_vars, "Number of variables for both truth tables must match"

    # Your code here
    pass
