# ══════════════════════════════════════════════════════════════════════════════
# BÀI 253/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/2.3
#   Gợi ý:      python qk.py hint DistinguishUnitaries/2.3
#   Lời giải:   python qk.py solution DistinguishUnitaries/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. CNOT₁₂ or SWAP?
# Input: A function that implements a two-qubit unitary transformation:
#        either CNOT₁₂ (control=first, target=second) or SWAP gate.
# Output: 0 if the given operation is CNOT₁₂,
#         1 if the given operation is SWAP.
# You are allowed to apply the given operation exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_cnot_from_swap(unitary_func) -> int:
    """
    Distinguish between CNOT₁₂ and SWAP gates.

    Args:
        unitary_func: A function that takes (qc, qubits) and applies either CNOT₁₂ or SWAP

    Returns:
        0 if CNOT₁₂, 1 if SWAP
    """
    # Your code here
    pass
