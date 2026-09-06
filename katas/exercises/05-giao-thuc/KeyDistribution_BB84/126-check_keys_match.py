# ══════════════════════════════════════════════════════════════════════════════
# BÀI 126/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/2.5
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/2.5
#   Lời giải:   python qk.py solution KeyDistribution_BB84/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5. Check if error rate was low enough
# Eavesdroppers can introduce more errors into the transmission. Alice and Bob
# need to check that there weren't more errors than expected from their channel
# characterization. They compare their keys and calculate the error rate.
#
# Inputs:
#      1) "key_alice" and "key_bob": bool lists of equal length N describing
#         the versions of the shared key obtained by Alice and Bob, respectively,
#      2) "error_rate": an integer between 0 and 50 - the percentage of bits
#         that are allowed to not match based on channel characterization.
# Output: True if the percentage of errors is less than or equal to the error rate,
#         and False otherwise.
#
# This check helps detect eavesdropping attempts in the BB84 protocol.

from typing import List

def check_keys_match(key_alice: List[bool], key_bob: List[bool], error_rate: int) -> bool:
    """
    Check if the error rate between Alice's and Bob's keys is acceptable.

    Args:
        key_alice: Alice's version of the shared key
        key_bob: Bob's version of the shared key
        error_rate: Maximum allowed error rate as percentage (0-50)

    Returns:
        True if error rate is within acceptable limits, False otherwise
    """
    # Your code here
    pass
