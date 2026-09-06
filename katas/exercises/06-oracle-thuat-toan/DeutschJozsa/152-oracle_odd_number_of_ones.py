# ══════════════════════════════════════════════════════════════════════════════
# BÀI 152/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.4
#   Gợi ý:      python qk.py hint DeutschJozsa/1.4
#   Lời giải:   python qk.py solution DeutschJozsa/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. f(x) = 1 if x has odd number of 1s, and 0 otherwise
# Inputs:
#      1) N qubits in arbitrary state |x⟩ (input register)
#      2) a qubit in arbitrary state |y⟩ (output qubit)
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
# Hint: f(x) can be represented as x_0 ⊕ x_1 ⊕ ... ⊕ x_(N-1)

from qiskit import QuantumCircuit
from typing import List

def oracle_odd_number_of_ones(qc: QuantumCircuit, x: List[int], y: int) -> QuantumCircuit:
    """
    Oracle for parity function f(x) = 1 if x has odd number of 1s.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
