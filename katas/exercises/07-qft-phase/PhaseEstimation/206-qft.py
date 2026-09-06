# ══════════════════════════════════════════════════════════════════════════════
# BÀI 206/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/2
#   Gợi ý:      python qk.py hint PhaseEstimation/2
#   Lời giải:   python qk.py solution PhaseEstimation/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Quantum Fourier Transform
# Input: A quantum circuit and list of qubit indices.
# Goal: Apply the Quantum Fourier Transform to the specified qubits.

from qiskit import QuantumCircuit
from typing import List
import numpy as np

def qft(qc: QuantumCircuit, qubits: List[int]) -> QuantumCircuit:
    """
    Apply Quantum Fourier Transform.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices for QFT

    Returns:
        Modified quantum circuit with QFT applied
    """
    # Your code here
    pass
