# ══════════════════════════════════════════════════════════════════════════════
# BÀI 186/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/2.2
#   Gợi ý:      python qk.py hint SolveSATWithGrover/2.2
#   Lời giải:   python qk.py solution SolveSATWithGrover/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. "Exactly-1 3-SAT" oracle
# Inputs:
#      1) N qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
#      3) a 2D list "problem" describing the exactly-1 3-SAT problem instance.
# "problem" describes the problem in the same format as in task 1.6;
# each clause is guaranteed to have exactly 3 terms.
#
# Goal: Transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
#       Leave the query register in the same state it started in.
#
# In exactly-1 3-SAT, each clause must have exactly one true literal,
# not just at least one as in regular SAT.
#
# Example: f(x) = (x₀ ∨ x₁ ∨ x₂) represented as [[(0, True), (1, True), (2, True)]]
# Solutions: (1,0,0), (0,1,0), (0,0,1) but NOT (1,1,0) or (1,1,1)

from qiskit import QuantumCircuit
from typing import List, Tuple

def oracle_exactly1_3sat(qc: QuantumCircuit, query_qubits: list[int], target: int,
                        problem: List[List[Tuple[int, bool]]]) -> QuantumCircuit:
    """
    Exactly-1 3-SAT oracle: each clause must have exactly one true literal.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index
        problem: List of clauses, each with exactly 3 (variable_index, is_positive) tuples

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
