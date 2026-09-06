# ══════════════════════════════════════════════════════════════════════════════
# BÀI 207/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/3
#   Gợi ý:      python qk.py hint PhaseEstimation/3
#   Lời giải:   python qk.py solution PhaseEstimation/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Inverse Quantum Fourier Transform
# Input: A quantum circuit and list of qubit indices.
# Goal: Apply the inverse QFT to extract phase information.

from qiskit import QuantumCircuit
from typing import List
import numpy as np

def inverse_qft(qc: QuantumCircuit, qubits: List[int]) -> QuantumCircuit:
    """
    Apply inverse Quantum Fourier Transform.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices for inverse QFT

    Returns:
        Modified quantum circuit with inverse QFT applied
    """
    # Your code here
    pass
