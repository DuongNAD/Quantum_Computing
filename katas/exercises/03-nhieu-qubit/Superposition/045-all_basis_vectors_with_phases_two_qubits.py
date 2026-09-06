# ══════════════════════════════════════════════════════════════════════════════
# BÀI 045/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.5
#   Gợi ý:      python qk.py hint Superposition/1.5
#   Lời giải:   python qk.py solution Superposition/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Superposition of basis vectors with phases
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: create the following state on these qubits: (|00⟩ + i*|01⟩ - |10⟩ - i*|11⟩) / 2.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def all_basis_vectors_with_phases_two_qubits(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create superposition with complex phases.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
