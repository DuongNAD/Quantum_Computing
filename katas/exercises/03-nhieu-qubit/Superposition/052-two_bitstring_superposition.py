# ══════════════════════════════════════════════════════════════════════════════
# BÀI 052/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.12
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.12
#   Gợi ý:      python qk.py hint Superposition/1.12
#   Lời giải:   python qk.py solution Superposition/1.12
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.12. Superposition of two bit strings
# Inputs:
#      1) N qubits in |0...0⟩ state
#      2) two bit string represented as Bool[]s
# Goal: create an equal superposition of two basis states given by the bit strings.
#
# Bit values false and true correspond to |0⟩ and |1⟩ states.
# Example: for bit strings [false, true, false] and [false, false, true]
# the qubit state required is (|010⟩ + |001⟩) / sqrt(2).
# You are guaranteed that the both bit strings have the same length as the qubit array,
# and that the bit strings will differ in at least one bit.

from qiskit import QuantumCircuit
from typing import List

def two_bitstring_superposition(qc: QuantumCircuit, qs: List[int], bits1: List[bool], bits2: List[bool]) -> QuantumCircuit:
    """
    Create equal superposition of two bit strings.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices
        bits1: First bit string
        bits2: Second bit string

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
