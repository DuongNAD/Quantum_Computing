# ══════════════════════════════════════════════════════════════════════════════
# BÀI 150/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.2
#   Gợi ý:      python qk.py hint DeutschJozsa/1.2
#   Lời giải:   python qk.py solution DeutschJozsa/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. f(x) = 1 (One function)
# Inputs:
#     1) N qubits in arbitrary state |x⟩ (input register)
#     2) a qubit in arbitrary state |y⟩ (output qubit)
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ where f(x) = 1 for all x.
# Since f(x) = 1, |y ⊕ 1⟩ = |NOT y⟩, so we need to flip the output qubit.

from qiskit import QuantumCircuit

def oracle_one(qc: QuantumCircuit, x_register: list[int], y: int) -> QuantumCircuit:
    """
    Oracle for the constant one function f(x) = 1.

    Args:
        qc: Quantum circuit to modify
        x_register: List of input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit with output qubit flipped
    """
    # Your code here
    pass
