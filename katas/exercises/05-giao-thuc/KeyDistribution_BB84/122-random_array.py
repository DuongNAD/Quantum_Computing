# ══════════════════════════════════════════════════════════════════════════════
# BÀI 122/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/2.1
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/2.1
#   Lời giải:   python qk.py solution KeyDistribution_BB84/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Generate random array
# You need a way of generating random boolean values for both Alice and Bob to use
# in the BB84 protocol. Alice needs random choices for which basis to prepare in
# and what bit value to send. Bob needs random bit values to decide what basis
# to measure each qubit in.
# Input: An integer N.
# Output: A bool list of length N, where each element is chosen at random.
#
# Note: This will be used by both Alice and Bob to choose either the sequence
#       of bits to send or the sequence of bases (False indicates |0⟩/|1⟩ basis,
#       and True indicates |+⟩/|-⟩ basis) to use when encoding/measuring the bits.

import random
from typing import List

def random_array(n: int) -> List[bool]:
    """
    Generate a random array of boolean values.

    Args:
        n: Length of the array to generate

    Returns:
        List of n random boolean values
    """
    # Your code here
    pass
