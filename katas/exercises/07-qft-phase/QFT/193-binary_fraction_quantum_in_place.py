# ══════════════════════════════════════════════════════════════════════════════
# BÀI 193/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.5
#   Gợi ý:      python qk.py hint QFT/1.5
#   Lời giải:   python qk.py solution QFT/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Prepare binary fraction exponent in place (quantum input)
# Input: A register of n qubits in state |j₁j₂...jₙ⟩.
# Goal: Change the state of the register
#       from |j₁⟩ ⊗ |j₂...jₙ⟩
#         to 1/sqrt(2) (|0⟩ + exp(2πi · 0.j₁j₂...jₙ) |1⟩) ⊗ |j₂...jₙ⟩.
# Note: The register of qubits can be in superposition as well;
#       the behavior in this case is defined by behavior on the basis states and the linearity of unitary transformations.
# Hint: This task is very similar to task 1.4, but the digit j₁ is encoded in-place, using task 1.1.

from qiskit import QuantumCircuit
import numpy as np

def binary_fraction_quantum_in_place(qc: QuantumCircuit, register: list) -> QuantumCircuit:
    """
    Apply in-place binary fraction transformation to the first qubit controlled by the rest.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices in the register

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
