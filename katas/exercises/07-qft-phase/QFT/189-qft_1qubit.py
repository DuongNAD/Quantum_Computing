# ══════════════════════════════════════════════════════════════════════════════
# BÀI 189/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.1
#   Gợi ý:      python qk.py hint QFT/1.1
#   Lời giải:   python qk.py solution QFT/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. 1-qubit QFT
# Input: A qubit in an arbitrary state |Ψ⟩.
# Goal: Apply QFT to this qubit.
# Note: 1-qubit QFT is just a Hadamard gate.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def qft_1qubit(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply 1-qubit Quantum Fourier Transform.

    Args:
        qc: Quantum circuit to modify
        q: Qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
