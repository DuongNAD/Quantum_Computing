# ══════════════════════════════════════════════════════════════════════════════
# BÀI 194/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/1.6
#   Gợi ý:      python qk.py hint QFT/1.6
#   Lời giải:   python qk.py solution QFT/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Reverse the order of qubits
# Input: A register of n qubits in state |x₁x₂...xₙ⟩.
# Goal: Reverse the order of qubits, i.e., convert the state of the register to |xₙ...x₂x₁⟩.

from qiskit import QuantumCircuit

def reverse_register(qc: QuantumCircuit, register: list) -> QuantumCircuit:
    """
    Reverse the order of qubits in the register.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices to reverse

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
