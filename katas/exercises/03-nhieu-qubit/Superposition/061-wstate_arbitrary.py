# ══════════════════════════════════════════════════════════════════════════════
# BÀI 061/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.7
#   Gợi ý:      python qk.py hint Superposition/2.7
#   Lời giải:   python qk.py solution Superposition/2.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.7**. W state on arbitrary number of qubits
# Input: N qubits in |0...0⟩ state (N is not necessarily a power of 2).
# Goal: create a W state (https://en.wikipedia.org/wiki/W_state) on these qubits.
# W state is an equal superposition of all basis states on N qubits of Hamming weight 1.
# Example: for N = 3, W state is (|100⟩ + |010⟩ + |001⟩) / sqrt(3).

from qiskit import QuantumCircuit
import numpy as np
from typing import List

def wstate_arbitrary(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create W state on arbitrary number of qubits.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
