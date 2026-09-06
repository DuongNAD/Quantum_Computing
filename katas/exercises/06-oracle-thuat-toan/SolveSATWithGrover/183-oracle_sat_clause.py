# ══════════════════════════════════════════════════════════════════════════════
# BÀI 183/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/1.5
#   Gợi ý:      python qk.py hint SolveSATWithGrover/1.5
#   Lời giải:   python qk.py solution SolveSATWithGrover/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Evaluate one clause of a SAT formula
#
# For SAT problems, f(x) is represented as a conjunction of clauses,
# and each clause is a disjunction of variables or negated variables:
#      clause(x) = ∨ₖ yₖ, where yₖ = either xⱼ or ¬xⱼ for some j
#
# For example: clause(x) = x₀ ∨ ¬x₁
#
# Inputs:
#      1) N qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
#      3) a list of tuples "clause" describing one clause of a SAT problem.
#
# Each tuple is an (int, bool) pair:
#  - first element is the index j of the variable xⱼ
#  - second element is True if variable appears as xⱼ, False if as ¬xⱼ
#
# Example: x₀ ∨ ¬x₁ is represented as [(0, True), (1, False)]

from qiskit import QuantumCircuit
from typing import List, Tuple

def oracle_sat_clause(qc: QuantumCircuit, query_qubits: list[int], target: int,
                     clause: List[Tuple[int, bool]]) -> QuantumCircuit:
    """
    SAT clause oracle: evaluates one clause of a SAT formula.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index
        clause: List of (variable_index, is_positive) tuples

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
