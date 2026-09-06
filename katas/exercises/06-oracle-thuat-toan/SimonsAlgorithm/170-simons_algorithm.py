# ══════════════════════════════════════════════════════════════════════════════
# BÀI 170/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/Algorithm
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/Algorithm
#   Gợi ý:      python qk.py hint SimonsAlgorithm/Algorithm
#   Lời giải:   python qk.py solution SimonsAlgorithm/Algorithm
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Simon's Algorithm Implementation
# Simon's algorithm finds a hidden bit string s such that f(x) = f(x ⊕ s) for all x.
# It provides exponential speedup over classical algorithms for this problem.
#
# The algorithm works by:
# 1. Creating superposition over all inputs
# 2. Computing f(x) using quantum oracle
# 3. Measuring to get vectors orthogonal to the hidden string s
# 4. Solving the system of linear equations to find s

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np
from typing import Callable, List

def simons_algorithm(n_qubits: int, oracle: Callable[[QuantumCircuit, list[int], list[int]], QuantumCircuit],
                    max_iterations: int = None) -> str:
    """
    Implement Simon's algorithm to find the hidden bit string.

    Args:
        n_qubits: Number of qubits in input register
        oracle: Oracle function that implements f(x)
        max_iterations: Maximum number of iterations (default: n_qubits - 1)

    Returns:
        Hidden bit string s as binary string
    """
    # Your code here
    pass

def create_simons_oracle(hidden_string: str) -> Callable[[QuantumCircuit, list[int], list[int]], QuantumCircuit]:
    """
    Create a Simon's oracle for a given hidden string s.
    The oracle satisfies f(x) = f(x ⊕ s) for all x.

    Args:
        hidden_string: Hidden bit string s

    Returns:
        Oracle function
    """
    def oracle(qc: QuantumCircuit, x_register: list[int], y_register: list[int]) -> QuantumCircuit:
        # Your code here
        pass

    return oracle

def solve_linear_system_gf2(equations: List[List[int]]) -> str:
    """
    Solve system of linear equations over GF(2) to find the hidden string.

    Args:
        equations: List of equations (each equation is a list of coefficients)

    Returns:
        Solution as binary string
    """
    # Your code here
    pass
