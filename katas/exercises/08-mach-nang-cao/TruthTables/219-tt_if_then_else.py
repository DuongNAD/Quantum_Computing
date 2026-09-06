# ══════════════════════════════════════════════════════════════════════════════
# BÀI 219/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/8
#   Gợi ý:      python qk.py hint TruthTables/8
#   Lời giải:   python qk.py solution TruthTables/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Build if-then-else truth table
# Goal: Compute the truth table of the if-then-else function ttCond ? ttThen : ttElse
#       (if ttCond then ttThen else ttElse) by making use of the truth table operations
#       defined in the previous tasks.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def tt_and(tt1: TruthTable, tt2: TruthTable) -> TruthTable:
    """Helper: Compute AND of two truth tables."""
    assert tt1.num_vars == tt2.num_vars
    return TruthTable(tt1.bits & tt2.bits, tt1.num_vars)

def tt_or(tt1: TruthTable, tt2: TruthTable) -> TruthTable:
    """Helper: Compute OR of two truth tables."""
    assert tt1.num_vars == tt2.num_vars
    return TruthTable(tt1.bits | tt2.bits, tt1.num_vars)

def tt_not(tt: TruthTable) -> TruthTable:
    """Helper: Compute NOT of a truth table."""
    mask = (1 << (1 << tt.num_vars)) - 1
    return TruthTable(tt.bits ^ mask, tt.num_vars)

def tt_if_then_else(tt_cond: TruthTable, tt_then: TruthTable, tt_else: TruthTable) -> TruthTable:
    """
    Compute the if-then-else function: ttCond ? ttThen : ttElse

    Args:
        tt_cond: Condition truth table
        tt_then: Truth table to return when condition is true
        tt_else: Truth table to return when condition is false

    Returns:
        Truth table representing if-then-else operation
    """
    assert tt_cond.num_vars == tt_then.num_vars == tt_else.num_vars, "All truth tables must have same number of variables"

    # Your code here - use tt_and, tt_or, tt_not operations
    pass
