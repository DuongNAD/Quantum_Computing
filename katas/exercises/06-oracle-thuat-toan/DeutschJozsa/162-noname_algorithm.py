# ══════════════════════════════════════════════════════════════════════════════
# BÀI 162/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/4.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/4.1
#   Gợi ý:      python qk.py hint DeutschJozsa/4.1
#   Lời giải:   python qk.py solution DeutschJozsa/4.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4.1. Reconstruct the oracle from task 1.6
# Inputs:
#      1) the number of qubits in the input register N for the function f
#      2) a quantum operation which implements the oracle |x⟩|y⟩ -> |x⟩|y ⊕ f(x)⟩, where
#         x is an N-qubit input register, y is a 1-qubit answer register, and f is a Boolean function
# You are guaranteed that the function f implemented by the oracle can be represented as
# f(x₀, ..., xₙ₋₁) = Σᵢ (rᵢ xᵢ + (1 - rᵢ)(1 - xᵢ)) modulo 2 for some bit vector r = (r₀, ..., rₙ₋₁).
# Output:
#      A bit vector r which generates the same oracle as the one you are given
#
# Hint: The bit vector r does not need to be the same as the one used by the oracle,
#       it just needs to produce equivalent results.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Callable

def noname_algorithm(N: int, uf_func: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> list[int]:
    """
    Algorithm to reconstruct bit vector r from oracle implementing
    f(x) = Σᵢ (rᵢ xᵢ + (1 - rᵢ)(1 - xᵢ)) mod 2.

    Args:
        N: Number of qubits in input register
        uf_func: Oracle function

    Returns:
        A bit vector r that produces equivalent oracle
    """
    # Your code here
    pass
