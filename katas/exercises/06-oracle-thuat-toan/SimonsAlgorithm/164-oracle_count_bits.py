# ══════════════════════════════════════════════════════════════════════════════
# BÀI 164/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/1.1
#   Gợi ý:      python qk.py hint SimonsAlgorithm/1.1
#   Lời giải:   python qk.py solution SimonsAlgorithm/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. f(x) = x₀ ⊕ ... ⊕ xₙ₋₁ (parity function)
# Inputs:
#     1) N qubits in an arbitrary state |x⟩
#     2) a qubit in an arbitrary state |y⟩
# Goal: Transform state |x, y⟩ into |x, y ⊕ x₀ ⊕ x₁ ... ⊕ xₙ₋₁⟩.
# This oracle computes the parity (XOR of all bits) of the input.

from qiskit import QuantumCircuit

def oracle_count_bits(qc: QuantumCircuit, x_register: list[int], y: int) -> QuantumCircuit:
    """
    Oracle that computes the parity of all input bits.

    Args:
        qc: Quantum circuit to modify
        x_register: List of input qubit indices
        y: Output qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
