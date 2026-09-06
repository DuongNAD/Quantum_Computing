# ══════════════════════════════════════════════════════════════════════════════
# BÀI 178/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/GroversSearch
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/GroversSearch
#   Gợi ý:      python qk.py hint GroversAlgorithm/GroversSearch
#   Lời giải:   python qk.py solution GroversAlgorithm/GroversSearch
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Grover's Search Algorithm Implementation
# Goal: Implement the complete Grover's search algorithm that can find marked items
#       in an unsorted database with quadratic speedup over classical search.
#
# The algorithm consists of:
# 1. Initialize qubits in equal superposition
# 2. Apply Grover iterations: Oracle + Diffusion operator
# 3. Measure to get the marked item with high probability

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np
from typing import Callable

def grovers_search(n_qubits: int, oracle: Callable[[QuantumCircuit, list[int]], QuantumCircuit],
                  iterations: int = None) -> dict:
    """
    Implement Grover's search algorithm.

    Args:
        n_qubits: Number of qubits in the search register
        oracle: Phase-flipping oracle function that marks the target state(s)
        iterations: Number of Grover iterations (if None, use optimal √(2^n))

    Returns:
        Dictionary of measurement results (bitstring -> count)
    """
    # Your code here
    pass

def grover_diffusion_operator(qc: QuantumCircuit, register: list[int]) -> QuantumCircuit:
    """
    Apply the diffusion operator (inversion about average) used in Grover's algorithm.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
