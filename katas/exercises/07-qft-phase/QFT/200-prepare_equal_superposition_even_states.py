# ══════════════════════════════════════════════════════════════════════════════
# BÀI 200/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.4
#   Gợi ý:      python qk.py hint QFT/2.4
#   Lời giải:   python qk.py solution QFT/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Prepare an equal superposition of all even basis states
# Input: A qubits of n qubits in state |0...0⟩.
# Goal: Prepare an equal superposition of all even basis vectors:
#       1/sqrt(2ⁿ⁻¹) (|0⟩ + |2⟩ + ... + |2ⁿ-2⟩).

from qiskit import QuantumCircuit

def prepare_equal_superposition_even_states(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Prepare equal superposition of even basis states using QFT.

    Args:
        qc: Quantum circuit to modify
        qubits: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
