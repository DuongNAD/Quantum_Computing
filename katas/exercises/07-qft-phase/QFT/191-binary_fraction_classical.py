# ══════════════════════════════════════════════════════════════════════════════
# BÀI 191/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.3
#   Gợi ý:      python qk.py hint QFT/1.3
#   Lời giải:   python qk.py solution QFT/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Prepare binary fraction exponent (classical input)
# Inputs:
#      1) A qubit in state |Ψ⟩ = α |0⟩ + β |1⟩.
#      2) An array of n bits [j₁, j₂, ..., jₙ], stored as list (jₖ ∈ {0, 1}).
# Goal: Change the state of the qubit to α |0⟩ + β · exp(2πi · 0.j₁j₂...jₙ) |1⟩,
# where 0.j₁j₂...jₙ is a binary fraction, similar to decimal fractions:
#       0.j₁j₂...jₙ = j₁ / 2¹ + j₂ / 2² + ... + jₙ / 2ⁿ.

from qiskit import QuantumCircuit
import numpy as np

def binary_fraction_classical(qc: QuantumCircuit, q: int, j: list) -> QuantumCircuit:
    """
    Apply phase based on classical binary fraction to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply phase
        j: List of bits representing binary fraction

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
