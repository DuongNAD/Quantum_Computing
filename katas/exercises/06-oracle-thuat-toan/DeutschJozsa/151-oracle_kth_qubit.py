# ══════════════════════════════════════════════════════════════════════════════
# BÀI 151/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.3
#   Gợi ý:      python qk.py hint DeutschJozsa/1.3
#   Lời giải:   python qk.py solution DeutschJozsa/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. f(x) = xₖ (the value of k-th qubit)
# Inputs:
#      1) N qubits in arbitrary state |x⟩ (input register)
#      2) a qubit in arbitrary state |y⟩ (output qubit)
#      3) 0-based index of the qubit from input register (0 <= k < N)
# Goal: transform state |x, y⟩ into state |x, y ⊕ xₖ⟩ (⊕ is addition modulo 2).

from qiskit import QuantumCircuit
from typing import List

def oracle_kth_qubit(qc: QuantumCircuit, x: List[int], y: int, k: int) -> QuantumCircuit:
    """
    Oracle for function f(x) = x_k (value of k-th qubit).

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index
        k: Index of the qubit to read (0-based)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
