# ══════════════════════════════════════════════════════════════════════════════
# BÀI 250/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.11
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.11
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.11. Distinguish 4 Pauli unitaries
# Input: A function that implements a single-qubit unitary transformation:
#        either I, X, Y, or Z gate.
# Output: 0 if the given operation is the I gate,
#         1 if the given operation is the X gate,
#         2 if the given operation is the Y gate,
#         3 if the given operation is the Z gate.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_four_paulis(unitary_func) -> int:
    """
    Distinguish between the four Pauli gates I, X, Y, Z.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies I, X, Y, or Z

    Returns:
        0 if I, 1 if X, 2 if Y, 3 if Z
    """
    # Your code here
    pass
