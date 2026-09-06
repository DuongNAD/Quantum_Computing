# ══════════════════════════════════════════════════════════════════════════════
# BÀI 165/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# SimonsAlgorithm/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SimonsAlgorithm/1.2
#   Gợi ý:      python qk.py hint SimonsAlgorithm/1.2
#   Lời giải:   python qk.py solution SimonsAlgorithm/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Bitwise right shift
# Inputs:
#     1) N qubits in an arbitrary state |x⟩
#     2) N qubits in an arbitrary state |y⟩
# Goal: Transform |x, y⟩ into |x, y ⊕ f(x)⟩, where f is bitwise right shift function.
# |y ⊕ f(x)⟩ = |y₀, y₁ ⊕ x₀, y₂ ⊕ x₁, ..., yₙ₋₁ ⊕ xₙ₋₂⟩
# The rightmost bit (y₀) remains unchanged, each other bit gets XORed with the previous input bit.

from qiskit import QuantumCircuit

def oracle_bitwise_right_shift(qc: QuantumCircuit, x_register: list[int], y_register: list[int]) -> QuantumCircuit:
    """
    Oracle that applies bitwise right shift function.

    Args:
        qc: Quantum circuit to modify
        x_register: List of input qubit indices
        y_register: List of output qubit indices (same length as x_register)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
