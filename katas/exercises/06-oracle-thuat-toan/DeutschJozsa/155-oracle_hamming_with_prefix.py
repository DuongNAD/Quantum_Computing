# ══════════════════════════════════════════════════════════════════════════════
# BÀI 155/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# DeutschJozsa/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DeutschJozsa/1.7
#   Gợi ý:      python qk.py hint DeutschJozsa/1.7
#   Lời giải:   python qk.py solution DeutschJozsa/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. f(x) = Σᵢ xᵢ + (1 if prefix of x is equal to the given bit vector, and 0 otherwise) modulo 2
# Inputs:
#      1) N qubits in arbitrary state |x⟩ (input register)
#      2) a qubit in arbitrary state |y⟩ (output qubit)
#      3) a bit vector of length P represented as list of integers (1 <= P <= N)
# Goal: transform state |x, y⟩ into state |x, y ⊕ f(x)⟩ (⊕ is addition modulo 2).
#
# A prefix of length k of a state |x⟩ = |x₁, ..., xₙ⟩ is the state of its first k qubits |x₁, ..., xₖ⟩.
# For example, a prefix of length 2 of a state |0110⟩ is 01.

from qiskit import QuantumCircuit

def oracle_hamming_with_prefix(qc: QuantumCircuit, x: list[int], y: int, prefix: list[int]) -> QuantumCircuit:
    """
    Oracle for f(x) = Σᵢ xᵢ + (1 if prefix matches) mod 2.

    Args:
        qc: Quantum circuit to modify
        x: List of input qubit indices
        y: Output qubit index
        prefix: Bit vector defining the required prefix

    Returns:
        Modified quantum circuit
    """
    P = len(prefix)
    assert 1 <= P <= len(x), "P should be between 1 and N, inclusive"

    # Your code here
    pass
