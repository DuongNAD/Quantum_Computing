# ══════════════════════════════════════════════════════════════════════════════
# BÀI 058/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.4
#   Gợi ý:      python qk.py hint Superposition/2.4
#   Lời giải:   python qk.py solution Superposition/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4*. (|00⟩ + ω |01⟩ + ω² |10⟩) / sqrt(3)
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: change the state to (|00⟩ + ω |01⟩ + ω² |10⟩) / sqrt(3) where ω is exp(2πi/3).

from qiskit import QuantumCircuit
import numpy as np
from typing import List

def three_states_two_qubits_phases(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create (|00⟩ + ω |01⟩ + ω² |10⟩) / sqrt(3) where ω = exp(2πi/3).

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
