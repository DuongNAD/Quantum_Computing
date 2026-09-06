# ══════════════════════════════════════════════════════════════════════════════
# BÀI 241/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.2
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.2
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Identity or Pauli Z?
# Input: A function that implements a single-qubit unitary transformation:
#        either the identity (I gate) or the Pauli Z gate (Z gate).
# Output: 0 if the given operation is the I gate,
#         1 if the given operation is the Z gate.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_i_from_z(unitary_func) -> int:
    """
    Distinguish between Identity and Pauli Z gates.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies either I or Z gate

    Returns:
        0 if I gate, 1 if Z gate
    """
    # Your code here
    pass
