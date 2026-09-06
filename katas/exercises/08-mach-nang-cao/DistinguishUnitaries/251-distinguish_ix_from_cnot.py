# ══════════════════════════════════════════════════════════════════════════════
# BÀI 251/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/2.1
#   Gợi ý:      python qk.py hint DistinguishUnitaries/2.1
#   Lời giải:   python qk.py solution DistinguishUnitaries/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. I ⊗ X or CNOT?
# Input: A function that implements a two-qubit unitary transformation:
#        either I ⊗ X (X gate on second qubit) or CNOT gate.
# Output: 0 if the given operation is I ⊗ X,
#         1 if the given operation is CNOT.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_ix_from_cnot(unitary_func) -> int:
    """
    Distinguish between I⊗X and CNOT gates.

    Args:
        unitary_func: A function that takes (qc, qubits) and applies either I⊗X or CNOT

    Returns:
        0 if I⊗X, 1 if CNOT
    """
    # Your code here
    pass
