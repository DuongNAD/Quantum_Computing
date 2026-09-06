# ══════════════════════════════════════════════════════════════════════════════
# BÀI 044/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.4
#   Gợi ý:      python qk.py hint Superposition/1.4
#   Lời giải:   python qk.py solution Superposition/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Superposition of basis vectors with phase flip.
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: create the following state on these qubits: (|00⟩ + |01⟩ + |10⟩ - |11⟩) / 2.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def all_basis_vectors_with_phase_flip_two_qubits(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create superposition with phase flip on |11⟩ state.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
