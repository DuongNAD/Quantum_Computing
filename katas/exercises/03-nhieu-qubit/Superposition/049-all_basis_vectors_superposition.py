# ══════════════════════════════════════════════════════════════════════════════
# BÀI 049/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.9
#   Gợi ý:      python qk.py hint Superposition/1.9
#   Lời giải:   python qk.py solution Superposition/1.9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.9. Superposition of all basis vectors
# Input: N qubits in |0...0⟩ state.
# Goal: create an equal superposition of all basis vectors from |0...0⟩ to |1...1⟩
# (i.e. state (|0...0⟩ + ... + |1...1⟩) / sqrt(2^N) ).

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def all_basis_vectors_superposition(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create equal superposition of all N-qubit basis vectors.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
