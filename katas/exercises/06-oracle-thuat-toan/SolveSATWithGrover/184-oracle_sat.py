# ══════════════════════════════════════════════════════════════════════════════
# BÀI 184/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/1.6
#   Gợi ý:      python qk.py hint SolveSATWithGrover/1.6
#   Lời giải:   python qk.py solution SolveSATWithGrover/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. General SAT problem oracle
#
# For SAT problems, f(x) is represented as a conjunction (AND) of M clauses on N variables:
#      f(x) = ∧ᵢ (∨ₖ yᵢₖ), where yᵢₖ = either xⱼ or ¬xⱼ for some j
#
# Inputs:
#      1) N qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
#      3) a 2D list "problem" describing the SAT problem instance f(x).
#
# i-th element of "problem" describes the i-th clause;
# each clause is a list of (int, bool) tuples as in Task 1.5.
#
# Example: f(x) = (x₀ ∨ x₁ ∨ x₂) is represented as [[(0, True), (1, True), (2, True)]]

from qiskit import QuantumCircuit
from typing import List, Tuple

def oracle_sat(qc: QuantumCircuit, query_qubits: list[int], target: int,
              problem: List[List[Tuple[int, bool]]]) -> QuantumCircuit:
    """
    General SAT oracle: evaluates a complete SAT formula.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index
        problem: List of clauses, each clause is list of (variable_index, is_positive) tuples

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
