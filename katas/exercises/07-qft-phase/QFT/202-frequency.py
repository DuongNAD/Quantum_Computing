# ══════════════════════════════════════════════════════════════════════════════
# BÀI 202/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.6
#   Gợi ý:      python qk.py hint QFT/2.6
#   Lời giải:   python qk.py solution QFT/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6. Get the frequency of a signal
# Input: A register of n ≥ 2 qubits in state 1/sqrt(2ⁿ) Σₖ exp(2πikF/2ⁿ) |k⟩, 0 ≤ F ≤ 2ⁿ - 1.
# Goal: Return the frequency F of the "signal" encoded in this state.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import List

def frequency(qc: QuantumCircuit, register: List[int]) -> int:
    """
    Extract the frequency from a periodic quantum state.

    Args:
        qc: Quantum circuit containing the periodic state
        register: List of qubit indices

    Returns:
        The frequency F of the periodic state
    """
    # Your code here
    pass
