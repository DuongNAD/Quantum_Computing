# ══════════════════════════════════════════════════════════════════════════════
# BÀI 156/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.8
#   Gợi ý:      python qk.py hint DeutschJozsa/1.8
#   Lời giải:   python qk.py solution DeutschJozsa/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8*. f(x) = 1 if x has two or three bits (out of three) set to 1, and 0 otherwise (majority function)
# Inputs:
#      1) 3 qubits in arbitrary state |x⟩ (input register)
#      2) a qubit in arbitrary state |y⟩ (output qubit)
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
#
# Hint: represent f(x) in terms of AND and ⊕ operations

from qiskit import QuantumCircuit

def oracle_majority_function(qc: QuantumCircuit, x: list[int], y: int) -> QuantumCircuit:
    """
    Oracle for majority function on 3 bits.

    Args:
        qc: Quantum circuit to modify
        x: List of 3 input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit
    """
    assert len(x) == 3, "x should have exactly 3 qubits"

    # Your code here
    pass
