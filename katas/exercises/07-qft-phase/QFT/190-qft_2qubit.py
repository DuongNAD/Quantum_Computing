# ══════════════════════════════════════════════════════════════════════════════
# BÀI 190/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.2
#   Gợi ý:      python qk.py hint QFT/1.2
#   Lời giải:   python qk.py solution QFT/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. 2-qubit QFT
# Input: A 2-qubit register in an arbitrary state |Ψ⟩.
# Goal: Apply QFT to this register.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def qft_2qubit(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Apply 2-qubit Quantum Fourier Transform.

    Args:
        qc: Quantum circuit to modify
        qs: List of 2 qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
