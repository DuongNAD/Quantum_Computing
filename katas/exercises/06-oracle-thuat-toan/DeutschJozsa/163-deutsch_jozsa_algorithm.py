# ══════════════════════════════════════════════════════════════════════════════
# BÀI 163/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/Algorithm
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/Algorithm
#   Gợi ý:      python qk.py hint DeutschJozsa/Algorithm
#   Lời giải:   python qk.py solution DeutschJozsa/Algorithm
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Deutsch-Jozsa Algorithm Implementation
# The Deutsch-Jozsa algorithm determines whether a Boolean function is constant (always 0 or always 1)
# or balanced (returns 0 for half the inputs and 1 for the other half) with just one query.
# This provides an exponential speedup over classical algorithms which need up to 2^(n-1) + 1 queries.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import Callable

def deutsch_jozsa_algorithm(n_qubits: int, oracle: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> bool:
    """
    Implement the Deutsch-Jozsa algorithm to determine if a function is constant or balanced.

    Args:
        n_qubits: Number of input qubits
        oracle: Function that implements the oracle f(x)

    Returns:
        True if function is constant, False if balanced
    """
    # Your code here
    pass

def bernstein_vazirani_algorithm(n_qubits: int, oracle: Callable[[QuantumCircuit, list[int], int], QuantumCircuit]) -> str:
    """
    Implement the Bernstein-Vazirani algorithm to find the hidden bit string s
    for a function f(x) = s·x (dot product mod 2).

    Args:
        n_qubits: Number of input qubits
        oracle: Function that implements f(x) = s·x

    Returns:
        Hidden bit string s as a binary string
    """
    # Your code here
    pass
