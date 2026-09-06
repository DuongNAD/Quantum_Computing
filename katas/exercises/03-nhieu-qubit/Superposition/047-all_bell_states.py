# ══════════════════════════════════════════════════════════════════════════════
# BÀI 047/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.7
#   Gợi ý:      python qk.py hint Superposition/1.7
#   Lời giải:   python qk.py solution Superposition/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. All Bell states
# Inputs:
#      1) two qubits in |00⟩ state (stored in an array of length 2)
#      2) an integer index
# Goal: create one of the Bell states based on the value of index:
#       0: |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2)
#       1: |φ⁻⟩ = (|00⟩ - |11⟩) / sqrt(2)
#       2: |Ψ⁺⟩ = (|01⟩ + |10⟩) / sqrt(2)
#       3: |Ψ⁻⟩ = (|01⟩ - |10⟩) / sqrt(2)

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def all_bell_states(qc: QuantumCircuit, qs: List[int], index: int) -> QuantumCircuit:
    """
    Create one of the four Bell states based on index.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices
        index: Bell state index (0-3)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
