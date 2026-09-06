# ══════════════════════════════════════════════════════════════════════════════
# BÀI 242/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.3
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.3
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Z or S?
# Input: A function that implements a single-qubit unitary transformation:
#        either the Pauli Z gate or the S gate.
# Output: 0 if the given operation is the Z gate,
#         1 if the given operation is the S gate.
# You are allowed to apply the given operation at most twice.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_z_from_s(unitary_func) -> int:
    """
    Distinguish between Z and S gates.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies either Z or S gate

    Returns:
        0 if Z gate, 1 if S gate
    """
    # Your code here
    pass
