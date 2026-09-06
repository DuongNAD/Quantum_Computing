# ══════════════════════════════════════════════════════════════════════════════
# BÀI 048/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.8
#   Gợi ý:      python qk.py hint Superposition/1.8
#   Lời giải:   python qk.py solution Superposition/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Greenberger–Horne–Zeilinger state
# Input: N qubits in |0...0⟩ state.
# Goal: create a GHZ state (|0...0⟩ + |1...1⟩) / sqrt(2) on these qubits.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def ghz_state(qc: QuantumCircuit, qs: List[int]) -> QuantumCircuit:
    """
    Create GHZ state on N qubits.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
