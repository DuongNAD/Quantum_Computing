# ══════════════════════════════════════════════════════════════════════════════
# BÀI 050/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.10
#   Gợi ý:      python qk.py hint Superposition/1.10
#   Lời giải:   python qk.py solution Superposition/1.10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.10. Superposition of all even or all odd numbers
# Inputs:
#      1) N qubits in |0...0⟩ state.
#      2) A boolean isEven.
# Goal: create a superposition of all even numbers on N qubits if isEven is true,
#       or a superposition of all odd numbers on N qubits if isEven is false.
#
# A basis state encodes an integer number using big-endian binary notation:
# state |01⟩ corresponds to the integer 1, and state |10⟩ - to the integer 2.
#
# Example: for N = 2 and isEven = true the required state is (|00⟩ + |10⟩) / sqrt(2),
#      and for N = 2 and isEven = false - (|01⟩ + |11⟩) / sqrt(2).

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import List
import numpy as np

def even_odd_numbers_superposition(qc: QuantumCircuit, qs: List[int], is_even: bool) -> QuantumCircuit:
    """
    Create superposition of all even or all odd numbers.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices
        is_even: If True, create even numbers superposition; if False, odd numbers

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
