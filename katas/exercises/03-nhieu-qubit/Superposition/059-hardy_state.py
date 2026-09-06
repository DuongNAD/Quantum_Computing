# ══════════════════════════════════════════════════════════════════════════════
# BÀI 059/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.5
#   Gợi ý:      python qk.py hint Superposition/2.5
#   Lời giải:   python qk.py solution Superposition/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5*. Hardy State
# Input: 2 qubits in |00⟩ state.
# Goal: create the state (3|00⟩ + |01⟩ + |10⟩ + |11⟩) / sqrt(12) on these qubits.

from qiskit import QuantumCircuit
import numpy as np
from typing import List

def hardy_state(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create Hardy state: (3|00⟩ + |01⟩ + |10⟩ + |11⟩) / sqrt(12).

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
