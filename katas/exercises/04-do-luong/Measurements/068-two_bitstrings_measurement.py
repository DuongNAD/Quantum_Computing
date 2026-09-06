# ══════════════════════════════════════════════════════════════════════════════
# BÀI 068/350  ·  Bậc 4 · Đo lường
# Measurements/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Measurements/1.7
#   Gợi ý:      python qk.py hint Measurements/1.7
#   Lời giải:   python qk.py solution Measurements/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. Distinguish two basis states given by bit strings
# Inputs:
#      1) N qubits (stored in an array) which are guaranteed to be
#         in one of the two basis states described by the given bit strings.
#      2) two bit string represented as Bool[]s.
# Output: 0 if the qubits were in the basis state described by the first bit string,
#         1 if they were in the basis state described by the second bit string.
# Bit values false and true correspond to |0⟩ and |1⟩ states.
# The state of the qubits at the end of the operation does not matter.
# You are guaranteed that both bit strings have the same length as the qubit array,
# and that the bit strings differ in at least one bit.
# You can use exactly one measurement.
# Example: for bit strings [false, true, false] and [false, false, true]
#          return 0 corresponds to state |010⟩, and return 1 corresponds to state |001⟩.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import List

def two_bitstrings_measurement(qc: QuantumCircuit, qs: List[int], bits1: List[bool], bits2: List[bool]) -> int:
    """
    Distinguish between two basis states given by bit strings.

    Args:
        qc: Quantum circuit containing the qubits
        qs: List of qubit indices
        bits1: First bit string
        bits2: Second bit string

    Returns:
        0 if qubits were in first bit string state, 1 if in second bit string state
    """
    # Your code here
    pass
