# ══════════════════════════════════════════════════════════════════════════════
# BÀI 179/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/1.1
#   Gợi ý:      python qk.py hint SolveSATWithGrover/1.1
#   Lời giải:   python qk.py solution SolveSATWithGrover/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. The AND oracle: f(x) = x₀ ∧ x₁
# Inputs:
#      1) 2 qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2),
#       i.e., flip the target state if all qubits of the query register are in the |1⟩ state,
#       and leave it unchanged otherwise.
#       Leave the query register in the same state it started in.
#
# This oracle marks states where ALL input qubits are |1⟩.

from qiskit import QuantumCircuit

def oracle_and(qc: QuantumCircuit, query_qubits: list[int], target: int) -> QuantumCircuit:
    """
    AND oracle: flips target if all query qubits are |1⟩.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
