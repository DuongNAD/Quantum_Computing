# ══════════════════════════════════════════════════════════════════════════════
# BÀI 160/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/3.1
#   Gợi ý:      python qk.py hint DeutschJozsa/3.1
#   Lời giải:   python qk.py solution DeutschJozsa/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1. Bernstein-Vazirani algorithm implementation
# Inputs:
#      1) the number of qubits in the input register N for the function f
#      2) a quantum operation which implements the oracle |x⟩|y⟩ -> |x⟩|y ⊕ f(x)⟩, where
#         x is an N-qubit input register, y is a 1-qubit answer register, and f is a Boolean function
# You are guaranteed that the function f implemented by the oracle is a scalar product function
# (can be represented as f(x₀, ..., xₙ₋₁) = Σᵢ rᵢ xᵢ modulo 2 for some bit vector r = (r₀, ..., rₙ₋₁)).
# Output:
#      A bit vector r reconstructed from the function
#
# Note: a trivial approach is to call the oracle N times:
#       |10...0⟩|0⟩ = |10...0⟩|r₀⟩, |010...0⟩|0⟩ = |010...0⟩|r₁⟩ and so on.
# Quantum computing allows to perform this task in just one call to the oracle.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Callable

def bv_algorithm(N: int, uf_func: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> list[int]:
    """
    Bernstein-Vazirani algorithm implementation.

    Args:
        N: Number of qubits in input register
        uf_func: Oracle function implementing f(x) = r·x

    Returns:
        Bit vector r that defines the scalar product function
    """
    # Your code here
    pass
