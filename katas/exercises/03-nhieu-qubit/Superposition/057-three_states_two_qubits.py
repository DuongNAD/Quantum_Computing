# ══════════════════════════════════════════════════════════════════════════════
# BÀI 057/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.3
#   Gợi ý:      python qk.py hint Superposition/2.3
#   Lời giải:   python qk.py solution Superposition/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3*. |00⟩ + |01⟩ + |10⟩ state
# Input: 2 qubits in |00⟩ state (stored in an array of length 2).
# Goal: change the state to (|00⟩ + |01⟩ + |10⟩) / sqrt(3).

from qiskit import QuantumCircuit
import numpy as np

def three_states_two_qubits(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Create state (|00⟩ + |01⟩ + |10⟩) / sqrt(3) from |00⟩.

    Args:
        qc: Quantum circuit to modify
        qubits: List of 2 qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
