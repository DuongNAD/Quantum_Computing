# ══════════════════════════════════════════════════════════════════════════════
# BÀI 185/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/2.1
#   Gợi ý:      python qk.py hint SolveSATWithGrover/2.1
#   Lời giải:   python qk.py solution SolveSATWithGrover/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. "Exactly one |1⟩" oracle
# Inputs:
#      1) 3 qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
#
# Goal: Transform the state |x, y⟩ into the state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2),
#       where f(x) = 1 if exactly one bit of x is in the |1⟩ state, and 0 otherwise.
#       Leave the query register in the same state it started in.
#
# This oracle is used for exactly-1 3-SAT problems where each clause must have
# exactly one true literal (not just at least one).

from qiskit import QuantumCircuit

def oracle_exactly_one(qc: QuantumCircuit, query_qubits: list[int], target: int) -> QuantumCircuit:
    """
    Exactly-one oracle: flips target if exactly one query qubit is |1⟩.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
