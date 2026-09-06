# ══════════════════════════════════════════════════════════════════════════════
# BÀI 204/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/3.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/3.2
#   Gợi ý:      python qk.py hint QFT/3.2
#   Lời giải:   python qk.py solution QFT/3.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.2. Implement roots of the QFT
# Inputs:
#      1) A register of n qubits in an arbitrary state.
#      2) An integer P (2 ≤ P ≤ 8).
# Goal: Transform state |x⟩ into state V |x⟩, where Vᴾ = QFT.
#       In other words, implement a P-th root of the QFT.
#       You can implement the required unitary up to a global phase.

from qiskit import QuantumCircuit
from typing import List

def qft_root(qc: QuantumCircuit, P: int, input_register: List[int]) -> QuantumCircuit:
    """
    Apply P-th root of QFT.

    Args:
        qc: Quantum circuit to modify
        P: Root order (2 ≤ P ≤ 8)
        input_register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
