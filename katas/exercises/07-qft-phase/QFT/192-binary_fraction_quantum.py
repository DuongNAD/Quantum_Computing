# ══════════════════════════════════════════════════════════════════════════════
# BÀI 192/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.4
#   Gợi ý:      python qk.py hint QFT/1.4
#   Lời giải:   python qk.py solution QFT/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Prepare binary fraction exponent (quantum input)
# Inputs:
#      1) A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
#      2) A register of n qubits in state |j₁j₂...jₙ⟩.
# Goal: Change the state of the input
#       from (α |0⟩ + β |1⟩) ⊗ |j₁j₂...jₙ⟩
#         to (α |0⟩ + β · exp(2πi · 0.j₁j₂...jₙ) |1⟩) ⊗ |j₁j₂...jₙ⟩,
#       where 0.j₁j₂...jₙ is a binary fraction corresponding to the basis state j₁j₂...jₙ of the register.
# Note: The register of qubits can be in superposition as well;
#       the behavior in this case is defined by behavior on the basis states and the linearity of unitary transformations.

from qiskit import QuantumCircuit
import numpy as np

def binary_fraction_quantum(qc: QuantumCircuit, q: int, j_register: list) -> QuantumCircuit:
    """
    Apply controlled phase based on quantum register to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of target qubit
        j_register: List of control qubit indices representing binary fraction

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
