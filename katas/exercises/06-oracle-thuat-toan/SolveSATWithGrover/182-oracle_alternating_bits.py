# ══════════════════════════════════════════════════════════════════════════════
# BÀI 182/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/1.4
#   Gợi ý:      python qk.py hint SolveSATWithGrover/1.4
#   Lời giải:   python qk.py solution SolveSATWithGrover/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Alternating bits oracle: f(x) = (x₀ ⊕ x₁) ∧ (x₁ ⊕ x₂) ∧ ... ∧ (xₙ₋₂ ⊕ xₙ₋₁)
# Inputs:
#      1) N qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
#       Leave the query register in the same state it started in.
#
# This oracle marks alternating bit patterns like |10101...⟩ and |01010...⟩
# where adjacent bits are always different.

from qiskit import QuantumCircuit

def oracle_alternating_bits(qc: QuantumCircuit, query_qubits: list[int], target: int) -> QuantumCircuit:
    """
    Alternating bits oracle: marks states where adjacent bits are different.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
