# ══════════════════════════════════════════════════════════════════════════════
# BÀI 203/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/3.1
#   Gợi ý:      python qk.py hint QFT/3.1
#   Lời giải:   python qk.py solution QFT/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1. Implement powers of the QFT
# Inputs:
#      1) A register of n qubits in an arbitrary state.
#      2) An integer P (0 ≤ P ≤ 2²⁰ - 1).
#
# Goal: Transform state |x⟩ into state QFTᴾ |x⟩,
#       where QFT is the quantum Fourier transform implemented in part I.
# Note: Your solution has to run fast for any P in the given range!

from qiskit import QuantumCircuit
from typing import List

def qft_power(qc: QuantumCircuit, P: int, input_register: List[int]) -> QuantumCircuit:
    """
    Apply P-th power of QFT efficiently.

    Args:
        qc: Quantum circuit to modify
        P: Power to apply (0 ≤ P ≤ 2²⁰ - 1)
        input_register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
