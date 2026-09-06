# ══════════════════════════════════════════════════════════════════════════════
# BÀI 153/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.5
#   Gợi ý:      python qk.py hint DeutschJozsa/1.5
#   Lời giải:   python qk.py solution DeutschJozsa/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. f(x) = Σᵢ rᵢ xᵢ modulo 2 for a given bit vector r (scalar product function)
# Inputs:
#      1) N qubits in arbitrary state |x⟩ (input register)
#      2) a qubit in arbitrary state |y⟩ (output qubit)
#      3) a bit vector of length N represented as list of integers
# You are guaranteed that the qubit array and the bit vector have the same length.
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
#
# Note: the functions featured in tasks 1.1, 1.3 and 1.4 are special cases of this function.

from qiskit import QuantumCircuit

def oracle_product_function(qc: QuantumCircuit, x: list[int], y: int, r: list[int]) -> QuantumCircuit:
    """
    Oracle for scalar product function f(x) = Σᵢ rᵢ xᵢ mod 2.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index
        r: Bit vector defining the function

    Returns:
        Modified quantum circuit
    """
    assert len(x) == len(r), "Arrays should have the same length"

    # Your code here
    pass
