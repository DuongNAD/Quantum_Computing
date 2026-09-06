# ══════════════════════════════════════════════════════════════════════════════
# BÀI 247/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.8
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.8
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Y, XZ, -Y or -XZ?
# Input: A function that implements a single-qubit unitary transformation:
#        either Y, XZ, -Y, or -XZ (with possible global phase of -1).
# Output: 0 if the given operation is the Y gate,
#         1 if the given operation is the -XZ gate,
#         2 if the given operation is the -Y gate,
#         3 if the given operation is the XZ gate.
# You are allowed to apply the given operation at most three times.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import numpy as np

def distinguish_y_xz_phases(gate) -> int:
    """
    Distinguish between Y, XZ, -Y, and -XZ gates.

    Args:
        gate: A function that takes (qc, qubit) and applies one of the four gates

    Returns:
        0 if Y, 1 if -XZ, 2 if -Y, 3 if XZ
    """
    # Your code here
    pass
