# ══════════════════════════════════════════════════════════════════════════════
# BÀI 196/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.8
#   Gợi ý:      python qk.py hint QFT/1.8
#   Lời giải:   python qk.py solution QFT/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Inverse QFT
# Input: A register of n qubits in state |j₁j₂...jₙ⟩.
# Goal: Apply inverse QFT to the input register,
#       i.e., transform it to a state
#       1/sqrt(2ⁿ) ∑ₖ exp(-2πi · jk / 2ⁿ) |k⟩.
# Hint: Inverse QFT is literally the inverse transformation of QFT.
#       Do you know a quantum way to express this?

from qiskit import QuantumCircuit
from typing import List

def inverse_qft(qc: QuantumCircuit, register: List[int]) -> QuantumCircuit:
    """
    Apply inverse quantum Fourier transform.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
