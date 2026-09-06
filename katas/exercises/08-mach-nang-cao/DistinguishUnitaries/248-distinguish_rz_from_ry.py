# ══════════════════════════════════════════════════════════════════════════════
# BÀI 248/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.9
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.9
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.9. Rz or Ry (fixed angle)?
# Input: A function that implements a single-qubit unitary transformation:
#        either Rz(θ) or Ry(θ) with a fixed angle θ ∈ [0.01π, 0.99π].
# Output: 0 if the given operation is the Rz(θ) gate,
#         1 if the given operation is the Ry(θ) gate.
# You are allowed to apply the given operation any number of times.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import numpy as np

def distinguish_rz_from_ry(unitary_func, theta: float) -> int:
    """
    Distinguish between Rz(θ) and Ry(θ) gates.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies either Rz(θ) or Ry(θ)
        theta: The rotation angle

    Returns:
        0 if Rz gate, 1 if Ry gate
    """
    # Your code here
    pass
