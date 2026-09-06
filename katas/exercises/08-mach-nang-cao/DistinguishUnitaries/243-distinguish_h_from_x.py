# ══════════════════════════════════════════════════════════════════════════════
# BÀI 243/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.4
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.4
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Hadamard or Pauli X?
# Input: A function that implements a single-qubit unitary transformation:
#        either the Hadamard gate or the Pauli X gate.
# Output: 0 if the given operation is the H gate,
#         1 if the given operation is the X gate.
# You are allowed to apply the given operation at most twice.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_h_from_x(unitary_func) -> int:
    """
    Distinguish between Hadamard and Pauli X gates.

    Args:
        unitary_func: A function that takes (qc, qubit) and applies either H or X gate

    Returns:
        0 if H gate, 1 if X gate
    """
    # Your code here
    pass
