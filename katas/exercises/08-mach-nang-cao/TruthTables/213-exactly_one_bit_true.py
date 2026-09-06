# ══════════════════════════════════════════════════════════════════════════════
# BÀI 213/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/2
#   Gợi ý:      python qk.py hint TruthTables/2
#   Lời giải:   python qk.py solution TruthTables/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. "Exactly 1 bit is true" function
# Goal: Describe a 3-input function f(x₃, x₂, x₁) represented by an integer
#       which is true if and only if exactly 1 bit out of x₁, x₂ or x₃ is true.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def exactly_one_bit_true() -> TruthTable:
    """
    Return a truth table for the function that is true iff exactly 1 bit is true.

    Returns:
        TruthTable representing the "exactly 1 bit true" function
    """
    # Your code here
    f = TruthTable(0, 3)  # Update this
    return f
