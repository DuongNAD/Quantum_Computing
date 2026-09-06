# ══════════════════════════════════════════════════════════════════════════════
# BÀI 041/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.1
#   Gợi ý:      python qk.py hint Superposition/1.1
#   Lời giải:   python qk.py solution Superposition/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Plus state
# Input: a qubit in the |0⟩ state.
# Goal: prepare a |+⟩ state on this qubit (|+⟩ = (|0⟩ + |1⟩) / sqrt(2)).

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def plus_state(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Prepare a |+⟩ state on qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to prepare in |+⟩ state

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
