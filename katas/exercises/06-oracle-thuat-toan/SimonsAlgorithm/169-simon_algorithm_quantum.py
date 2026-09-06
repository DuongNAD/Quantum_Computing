# ══════════════════════════════════════════════════════════════════════════════
# BÀI 169/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/2.2
#   Gợi ý:      python qk.py hint SimonsAlgorithm/2.2
#   Lời giải:   python qk.py solution SimonsAlgorithm/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Quantum part of Simon's algorithm
# Inputs:
#      1) the number of qubits in the input register N for the function f
#      2) a quantum operation which implements the oracle |x⟩|y⟩ -> |x⟩|y ⊕ f(x)⟩, where
#         x is N-qubit input register, y is N-qubit answer register, and f is a function
#         from N-bit strings into N-bit strings
#
# The function f is guaranteed to satisfy the following property:
# there exists some N-bit string s such that for all N-bit strings b and c (b != c)
# we have f(b) = f(c) if and only if b = c ⊕ s. In other words, f is a two-to-one function.
#
# Output:
#      Any bit string b such that Σᵢ bᵢ sᵢ = 0 modulo 2.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Callable

def simon_algorithm_quantum(N: int, uf_func: Callable[[QuantumCircuit, list[int], list[int]], QuantumCircuit]) -> list[int]:
    """
    Quantum part of Simon's algorithm.

    Args:
        N: Number of qubits in input/output registers
        uf_func: Oracle function implementing f

    Returns:
        Bit string b orthogonal to secret string s
    """
    # Your code here
    pass
