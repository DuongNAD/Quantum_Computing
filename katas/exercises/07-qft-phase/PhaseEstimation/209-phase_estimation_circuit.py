# ══════════════════════════════════════════════════════════════════════════════
# BÀI 209/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/5
#   Gợi ý:      python qk.py hint PhaseEstimation/5
#   Lời giải:   python qk.py solution PhaseEstimation/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Phase estimation circuit
# Input: Number of precision qubits, target qubit, and phase angle.
# Goal: Build the complete phase estimation circuit.

from qiskit import QuantumCircuit
import numpy as np

def phase_estimation_circuit(n_precision: int, theta: float) -> QuantumCircuit:
    """
    Build quantum phase estimation circuit.

    Args:
        n_precision: Number of precision qubits
        theta: Phase angle to estimate (U|1> = e^(i*theta)|1>)

    Returns:
        Quantum circuit for phase estimation
    """
    # Your code here
    pass
