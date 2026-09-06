# ══════════════════════════════════════════════════════════════════════════════
# BÀI 118/350  ·  Bậc 5 · Giao thức lượng tử
# SuperdenseCoding/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SuperdenseCoding/4
#   Gợi ý:      python qk.py hint SuperdenseCoding/4
#   Lời giải:   python qk.py solution SuperdenseCoding/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Superdense coding protocol end-to-end
# Put together the steps performed in tasks 1-3 to implement the full superdense coding protocol.
# Input: Two classical bits to be transmitted.
# Goal: Prepare an EPR pair, encode the two classical bits in the state of the pair
# by applying quantum gates to one member of the pair, and decode the two classical bits
# from the state of the pair. Return the result of decoding.

from qiskit import QuantumCircuit

def superdense_coding_protocol(bit1: bool, bit2: bool) -> tuple[bool, bool]:
    """
    Complete superdense coding protocol: encode and decode two classical bits.

    Args:
        bit1: First classical bit to transmit
        bit2: Second classical bit to transmit

    Returns:
        Tuple of decoded (bit1, bit2) - should match input
    """
    # Your code here
    pass
