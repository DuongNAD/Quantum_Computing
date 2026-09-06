# ══════════════════════════════════════════════════════════════════════════════
# BÀI 249/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.10
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.10
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.10. Rz or R1 (fixed angle)?
# Input: A function that implements a single-qubit unitary transformation:
#        either Rz(θ) or R1(θ) with a fixed angle θ ∈ [0.01π, 0.99π].
# Output: 0 if the given operation is the Rz(θ) gate,
#         1 if the given operation is the R1(θ) gate.
# You are allowed to apply the given operation any number of times.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
from qiskit.quantum_info import process_fidelity, Operator
import numpy as np

def distinguish_rz_from_r1_angle(unitary_func, theta: float) -> int:
    """
    Distinguish between Rz(θ) and R1(θ) gates with known angle.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies either Rz(θ) or R1(θ)
        theta: The rotation angle

    Returns:
        0 if Rz gate, 1 if R1 gate
    """
    # Your code here
    pass
