# ══════════════════════════════════════════════════════════════════════════════
# BÀI 056/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/2.2
#   Gợi ý:      python qk.py hint Superposition/2.2
#   Lời giải:   python qk.py solution Superposition/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. 1/sqrt(2)|00⟩ + 1/2|10⟩ + 1/2|11⟩ state
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: change the state to 1/sqrt(2)|00⟩ + 1/2|10⟩ + 1/2|11⟩.

from qiskit import QuantumCircuit
import numpy as np

def controlled_rotation(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Create state 1/sqrt(2)|00⟩ + 1/2|10⟩ + 1/2|11⟩ from |00⟩.

    Args:
        qc: Quantum circuit to modify
        qubits: List of 2 qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
