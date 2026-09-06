# ══════════════════════════════════════════════════════════════════════════════
# BÀI 211/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/7
#   Gợi ý:      python qk.py hint PhaseEstimation/7
#   Lời giải:   python qk.py solution PhaseEstimation/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Run complete phase estimation
# Input: Phase angle to estimate and precision.
# Goal: Run full QPE algorithm and return estimated phase.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np

def run_phase_estimation(theta: float, n_precision: int) -> float:
    """
    Run complete quantum phase estimation.

    Args:
        theta: True phase angle to estimate
        n_precision: Number of precision qubits

    Returns:
        Estimated phase in radians
    """
    # Your code here
    pass
