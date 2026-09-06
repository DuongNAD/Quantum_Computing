# ══════════════════════════════════════════════════════════════════════════════
# BÀI 201/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.5
#   Gợi ý:      python qk.py hint QFT/2.5
#   Lời giải:   python qk.py solution QFT/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5*. Prepare a square-wave signal
# Input: A register of n ≥ 2 qubits in state |0...0⟩.
# Goal: Prepare a periodic state with alternating 1, 1, -1, -1 amplitudes of basis states:
#       1/sqrt(2ⁿ) (|0⟩ + |1⟩ - |2⟩ - |3⟩ + ... - |2ⁿ-2⟩ - |2ⁿ-1⟩).

from qiskit import QuantumCircuit
import numpy as np

def prepare_square_wave_signal(qc: QuantumCircuit, register: list) -> QuantumCircuit:
    """
    Prepare square wave signal using QFT.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices (n ≥ 2)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
