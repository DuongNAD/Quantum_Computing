# ══════════════════════════════════════════════════════════════════════════════
# BÀI 214/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/3
#   Gợi ý:      python qk.py hint TruthTables/3
#   Lời giải:   python qk.py solution TruthTables/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. "Exactly 2 bits are true" function
# Goal: Describe a 3-input function f(x₃, x₂, x₁) represented by an integer
#       which is true if and only if exactly 2 bits out of x₁, x₂ or x₃ are true.

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def exactly_two_bits_true() -> TruthTable:
    """
    Return a truth table for the function that is true iff exactly 2 bits are true.

    Returns:
        TruthTable representing the "exactly 2 bits true" function
    """
    # Your code here
    f = TruthTable(0, 3)  # Update this
    return f
