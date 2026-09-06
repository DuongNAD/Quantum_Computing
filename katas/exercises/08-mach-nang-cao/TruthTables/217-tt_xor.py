# ══════════════════════════════════════════════════════════════════════════════
# BÀI 217/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/6
#   Gợi ý:      python qk.py hint TruthTables/6
#   Lời giải:   python qk.py solution TruthTables/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Compute XOR of two truth tables
# Goal: Compute a truth table that computes the exclusive-OR (XOR)
#       of two truth tables.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def tt_xor(tt1: TruthTable, tt2: TruthTable) -> TruthTable:
    """
    Compute the XOR of two truth tables.

    Args:
        tt1: First truth table
        tt2: Second truth table

    Returns:
        Truth table representing tt1 XOR tt2
    """
    assert tt1.num_vars == tt2.num_vars, "Number of variables for both truth tables must match"

    # Your code here
    pass
