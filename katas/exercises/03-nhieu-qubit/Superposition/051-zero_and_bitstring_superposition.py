# ══════════════════════════════════════════════════════════════════════════════
# BÀI 051/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.11
#   Gợi ý:      python qk.py hint Superposition/1.11
#   Lời giải:   python qk.py solution Superposition/1.11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.11. Superposition of |0...0⟩ and given bit string
# Inputs:
#      1) N qubits in |0...0⟩ state
#      2) bit string represented as Bool[]
# Goal: create an equal superposition of |0...0⟩ and basis state given by the bit string.
# Bit values false and true correspond to |0⟩ and |1⟩ states.
# You are guaranteed that the qubit array and the bit string have the same length.
# You are guaranteed that the first bit of the bit string is true.
# Example: for bit string = [true, false] the qubit state required is (|00⟩ + |10⟩) / sqrt(2).

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def zero_and_bitstring_superposition(qc: QuantumCircuit, qs: List[int], bits: List[bool]) -> QuantumCircuit:
    """
    Create superposition of |0...0⟩ and given bit string.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices
        bits: Bit string as list of booleans

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
