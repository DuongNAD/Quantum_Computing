# ══════════════════════════════════════════════════════════════════════════════
# BÀI 158/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/2.2
#   Gợi ý:      python qk.py hint DeutschJozsa/2.2
#   Lời giải:   python qk.py solution DeutschJozsa/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Deutsch-Jozsa algorithm implementation
# Inputs:
#      1) the number of qubits in the input register N for the function f
#      2) a quantum operation which implements the oracle |x⟩|y⟩ -> |x⟩|y ⊕ f(x)⟩, where
#         x is an N-qubit input register, y is a 1-qubit answer register, and f is a Boolean function
# You are guaranteed that the function f implemented by the oracle is either
# constant (returns 0 on all inputs or 1 on all inputs) or
# balanced (returns 0 on exactly one half of the input domain and 1 on the other half).
# Output:
#      true if the function f is constant
#      false if the function f is balanced

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import Callable

def dj_algorithm(n: int, oracle_func: Callable[[QuantumCircuit, list, int], QuantumCircuit]) -> bool:
    """
    Deutsch-Jozsa algorithm implementation.

    Args:
        n: Number of input qubits
        oracle_func: Function that applies the oracle to a quantum circuit

    Returns:
        True if function is constant, False if balanced
    """
    # Your code here
    pass
