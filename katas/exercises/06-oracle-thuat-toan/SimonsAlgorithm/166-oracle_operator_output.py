# ══════════════════════════════════════════════════════════════════════════════
# BÀI 166/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/1.3
#   Gợi ý:      python qk.py hint SimonsAlgorithm/1.3
#   Lời giải:   python qk.py solution SimonsAlgorithm/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Linear operator
# Inputs:
#      1) N qubits in an arbitrary state |x⟩
#      2) a qubit in an arbitrary state |y⟩
#      3) a 1xN binary matrix (represented as a list of integers) describing operator A
# Goal: Transform state |x, y⟩ into |x, y ⊕ A(x) ⟩ (⊕ is addition modulo 2).

from qiskit import QuantumCircuit

def oracle_operator_output(qc: QuantumCircuit, x: list[int], y: int, A: list[int]) -> QuantumCircuit:
    """
    Oracle for linear operator function f(x) = A·x.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index
        A: Binary matrix as list (1xN)

    Returns:
        Modified quantum circuit
    """
    assert len(x) == len(A), "Arrays x and A should have the same length"

    # Your code here
    pass
