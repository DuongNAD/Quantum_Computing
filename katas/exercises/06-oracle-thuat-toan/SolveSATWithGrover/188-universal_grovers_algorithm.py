# ══════════════════════════════════════════════════════════════════════════════
# BÀI 188/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/3.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/3.2
#   Gợi ý:      python qk.py hint SolveSATWithGrover/3.2
#   Lời giải:   python qk.py solution SolveSATWithGrover/3.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.2. Universal implementation of Grover's algorithm
# Inputs:
#      1) the number of qubits N,
#      2) a marking oracle which implements a boolean expression.
# Output:
#      A list of N boolean values which satisfy the expression implemented by the oracle
#      (i.e., any basis state marked by the oracle).
#
# This implementation should be robust to not knowing the optimal number of iterations.
# You need to try different numbers of iterations until you find a solution.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from typing import Callable, List
import math

def universal_grovers_algorithm(n: int, oracle: Callable[[QuantumCircuit, List[int], int], QuantumCircuit]) -> List[bool]:
    """
    Universal Grover's algorithm that doesn't require knowing the number of solutions.

    Args:
        n: Number of qubits
        oracle: Oracle function that takes (circuit, query_qubits, target_qubit) and returns modified circuit

    Returns:
        List of N boolean values representing a solution
    """
    # Your code here
    pass
