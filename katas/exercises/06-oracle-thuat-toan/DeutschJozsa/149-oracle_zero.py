# ══════════════════════════════════════════════════════════════════════════════
# BÀI 149/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.1
#   Gợi ý:      python qk.py hint DeutschJozsa/1.1
#   Lời giải:   python qk.py solution DeutschJozsa/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. f(x) = 0 (Zero function)
# Inputs:
#     1) N qubits in arbitrary state |x⟩ (input register)
#     2) a qubit in arbitrary state |y⟩ (output qubit)
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ where f(x) = 0 for all x.
# Since f(x) = 0, |y ⊕ 0⟩ = |y⟩, so no transformation is needed.

from qiskit import QuantumCircuit

def oracle_zero(qc: QuantumCircuit, x_register: list[int], y: int) -> QuantumCircuit:
    """
    Oracle for the constant zero function f(x) = 0.

    Args:
        qc: Quantum circuit to modify
        x_register: List of input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit (unchanged since f(x) = 0)
    """
    # Your code here
    pass
