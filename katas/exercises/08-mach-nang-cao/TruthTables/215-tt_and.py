# ══════════════════════════════════════════════════════════════════════════════
# BÀI 215/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/4
#   Gợi ý:      python qk.py hint TruthTables/4
#   Lời giải:   python qk.py solution TruthTables/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Compute AND of two truth tables
# Goal: Compute a truth table that computes the conjunction (AND)
#       of two truth tables. Find a way to perform the computation
#       directly on the integer representations of the truth tables,
#       i.e., without accessing the bits individually.
#
# Hint: You can use bit-wise operations for this task.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def tt_and(tt1: TruthTable, tt2: TruthTable) -> TruthTable:
    """
    Compute the AND of two truth tables.

    Args:
        tt1: First truth table
        tt2: Second truth table

    Returns:
        Truth table representing tt1 AND tt2
    """
    assert tt1.num_vars == tt2.num_vars, "Number of variables for both truth tables must match"

    # Your code here
    pass
