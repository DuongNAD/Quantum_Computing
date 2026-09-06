# ══════════════════════════════════════════════════════════════════════════════
# BÀI 060/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.6
#   Gợi ý:      python qk.py hint Superposition/2.6
#   Lời giải:   python qk.py solution Superposition/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6*. W state on 2ᵏ qubits
# Input: N = 2ᵏ qubits in |0...0⟩ state.
# Goal: create a W state (https://en.wikipedia.org/wiki/W_state) on these qubits.
# W state is an equal superposition of all basis states on N qubits of Hamming weight 1.
# Example: for N = 4, W state is (|1000⟩ + |0100⟩ + |0010⟩ + |0001⟩) / 2.

from qiskit import QuantumCircuit
import numpy as np
from typing import List

def wstate_power_of_two(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create W state on 2ᵏ qubits.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices (length must be power of 2)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
