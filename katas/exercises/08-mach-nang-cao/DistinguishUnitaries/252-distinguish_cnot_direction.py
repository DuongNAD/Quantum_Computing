# ══════════════════════════════════════════════════════════════════════════════
# BÀI 252/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/2.2
#   Gợi ý:      python qk.py hint DistinguishUnitaries/2.2
#   Lời giải:   python qk.py solution DistinguishUnitaries/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Figure out the direction of CNOT
# Input: A function that implements a two-qubit unitary transformation:
#        either CNOT₁₂ (control=first, target=second) or CNOT₂₁ (control=second, target=first).
# Output: 0 if the given operation is CNOT₁₂,
#         1 if the given operation is CNOT₂₁.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_cnot_direction(unitary_func) -> int:
    """
    Distinguish between CNOT₁₂ and CNOT₂₁.

    Args:
        unitary_func: A function that takes (qc, qubits) and applies CNOT in one direction

    Returns:
        0 if CNOT₁₂, 1 if CNOT₂₁
    """
    # Your code here
    pass
