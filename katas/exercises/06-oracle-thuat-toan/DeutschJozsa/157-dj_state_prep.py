# ══════════════════════════════════════════════════════════════════════════════
# BÀI 157/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/2.1
#   Gợi ý:      python qk.py hint DeutschJozsa/2.1
#   Lời giải:   python qk.py solution DeutschJozsa/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. State preparation for Deutsch-Jozsa algorithm
# Inputs:
#      1) N qubits in |0⟩ state (query register)
#      2) a qubit in |0⟩ state (answer register)
# Goal:
#      1) prepare an equal superposition of all basis vectors from |0...0⟩ to |1...1⟩ on query register
#         (i.e., state (|0...0⟩ + ... + |1...1⟩) / sqrt(2^N) )
#      2) prepare |-⟩ state (|-⟩ = (|0⟩ - |1⟩) / sqrt(2)) on answer register

from qiskit import QuantumCircuit
from typing import List

def dj_state_prep(qc: QuantumCircuit, query: List[int], answer: int) -> QuantumCircuit:
    """
    Prepare initial state for Deutsch-Jozsa algorithm.

    Args:
        qc: Quantum circuit to modify
        query: List of query qubit indices
        answer: Answer qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
