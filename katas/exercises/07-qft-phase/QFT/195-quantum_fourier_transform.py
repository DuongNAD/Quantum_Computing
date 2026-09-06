# ══════════════════════════════════════════════════════════════════════════════
# BÀI 195/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.7
#   Gợi ý:      python qk.py hint QFT/1.7
#   Lời giải:   python qk.py solution QFT/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. Quantum Fourier transform
# Input: A register of n qubits in state |j₁j₂...jₙ⟩.
# Goal: Apply quantum Fourier transform to the input register,
#       i.e., transform it to a state
#       1/sqrt(2ⁿ) ∑ₖ exp(2πi · jk / 2ⁿ) |k⟩ =
#     = 1/sqrt(2) (|0⟩ + exp(2πi · 0.jₙ) |1⟩) ⊗
#     ⊗ 1/sqrt(2) (|0⟩ + exp(2πi · 0.jₙ₋₁jₙ) |1⟩) ⊗ ... ⊗
#     ⊗ 1/sqrt(2) (|0⟩ + exp(2πi · 0.j₁j₂...jₙ₋₁jₙ) |1⟩)
#
# Note: The register of qubits can be in superposition as well;
#       the behavior in this case is defined by behavior on the basis states and the linearity of unitary transformations.
# Note: You can do this with a library call, but we recommend
#       implementing the algorithm yourself for learning purposes, using the previous tasks.

from qiskit import QuantumCircuit
import numpy as np

def quantum_fourier_transform(qc: QuantumCircuit, register: list) -> QuantumCircuit:
    """
    Apply Quantum Fourier Transform to the register.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices to transform

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
