# ══════════════════════════════════════════════════════════════════════════════
# BÀI 181/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SolveSATWithGrover/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SolveSATWithGrover/1.3
#   Gợi ý:      python qk.py hint SolveSATWithGrover/1.3
#   Lời giải:   python qk.py solution SolveSATWithGrover/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. The XOR oracle: f(x) = x₀ ⊕ x₁
# Inputs:
#      1) 2 qubits in an arbitrary state |x⟩ (input/query register)
#      2) a qubit in an arbitrary state |y⟩ (target qubit)
# Goal: Transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2),
#       i.e., flip the target state if the qubits of the query register are in different states,
#       and leave it unchanged otherwise.
#       Leave the query register in the same state it started in.
#
# This oracle marks states where input qubits have DIFFERENT values.

from qiskit import QuantumCircuit

def oracle_xor(qc: QuantumCircuit, query_qubits: list[int], target: int) -> QuantumCircuit:
    """
    XOR oracle: flips target if query qubits have different values.

    Args:
        qc: Quantum circuit to modify
        query_qubits: List of input qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
