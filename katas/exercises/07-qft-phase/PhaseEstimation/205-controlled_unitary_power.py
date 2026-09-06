# ══════════════════════════════════════════════════════════════════════════════
# BÀI 205/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/1
#   Gợi ý:      python qk.py hint PhaseEstimation/1
#   Lời giải:   python qk.py solution PhaseEstimation/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Controlled unitary power
# Input: A quantum circuit, control qubit, target qubit, and power k.
# Goal: Apply U^(2^k) controlled by the control qubit, where U is a phase gate.

from qiskit import QuantumCircuit
import numpy as np

def controlled_unitary_power(qc: QuantumCircuit, control: int, target: int, theta: float, power: int) -> QuantumCircuit:
    """
    Apply controlled U^(2^power) where U = phase(theta).

    Args:
        qc: Quantum circuit to modify
        control: Control qubit index
        target: Target qubit index
        theta: Phase angle of the unitary U
        power: Power k such that U^(2^k) is applied

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
