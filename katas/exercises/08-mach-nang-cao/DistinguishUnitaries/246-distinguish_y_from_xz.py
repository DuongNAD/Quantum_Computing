# ══════════════════════════════════════════════════════════════════════════════
# BÀI 246/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.7
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.7
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. Y or XZ?
# Input: A function that implements a single-qubit unitary transformation:
#        either the Pauli Y gate or the sequence XZ (Z gate followed by X gate).
# Output: 0 if the given operation is the Y gate,
#         1 if the given operation is the XZ sequence.
# You are allowed to apply the given operation at most twice.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_y_from_xz(gate) -> int:
    """
    Distinguish between Y and XZ gates.

    Args:
        gate: A function that takes (qc, qubit) and applies either Y or XZ

    Returns:
        0 if Y gate, 1 if XZ gate
    """
    # Your code here
    pass
