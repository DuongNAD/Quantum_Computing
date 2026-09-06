# ══════════════════════════════════════════════════════════════════════════════
# BÀI 167/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/1.4
#   Gợi ý:      python qk.py hint SimonsAlgorithm/1.4
#   Lời giải:   python qk.py solution SimonsAlgorithm/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Multidimensional linear operator
# Inputs:
#      1) N1 qubits in an arbitrary state |x⟩ (input register)
#      2) N2 qubits in an arbitrary state |y⟩ (output register)
#      3) an N2 x N1 matrix (represented as list of lists) describing operator A
# The first dimension of the matrix (rows) corresponds to the output register,
# the second dimension (columns) - the input register.
# Goal: Transform state |x, y⟩ into |x, y ⊕ A(x) ⟩ (⊕ is addition modulo 2).

from qiskit import QuantumCircuit

def oracle_multidimensional_operator_output(qc: QuantumCircuit, x: list[int], y: list[int], A: list[list[int]]) -> QuantumCircuit:
    """
    Oracle for multidimensional linear operator f(x) = A·x.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: List of output qubit indices
        A: Binary matrix as list of lists (N2 x N1)

    Returns:
        Modified quantum circuit
    """
    assert len(x) == len(A[0]), "Arrays x and A[0] should have the same length"
    assert len(y) == len(A), "Arrays y and A should have the same length"

    # Your code here
    pass
