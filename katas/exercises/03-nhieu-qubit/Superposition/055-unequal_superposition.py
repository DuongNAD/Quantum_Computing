# ══════════════════════════════════════════════════════════════════════════════
# BÀI 055/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.1
#   Gợi ý:      python qk.py hint Superposition/2.1
#   Lời giải:   python qk.py solution Superposition/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Unequal superposition
# Inputs:
#      1) a qubit in the |0⟩ state.
#      2) angle alpha, in radians, represented as Double.
# Goal: prepare a cos(alpha) * |0⟩ + sin(alpha) * |1⟩ state on this qubit.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def unequal_superposition(qc: QuantumCircuit, q: int, alpha: float) -> QuantumCircuit:
    """
    Prepare unequal superposition state with given angle.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to prepare
        alpha: Angle parameter in radians

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
