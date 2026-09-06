# ══════════════════════════════════════════════════════════════════════════════
# BÀI 244/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.5
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.5
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Z or -Z?
# Input: A function that implements a single-qubit unitary transformation:
#        either the Pauli Z gate or the minus Pauli Z gate (-Z).
# Output: 0 if the given operation is the Z gate,
#         1 if the given operation is the -Z gate.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_z_from_minus_z(gate) -> int:
    """
    Distinguish between Z and -Z gates.

    Args:
        gate: A function that takes (qc, qubit) and applies either Z or -Z gate

    Returns:
        0 if Z gate, 1 if -Z gate
    """
    # Your code here
    pass
