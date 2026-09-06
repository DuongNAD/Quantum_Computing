# ══════════════════════════════════════════════════════════════════════════════
# BÀI 254/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/2.4
#   Gợi ý:      python qk.py hint DistinguishUnitaries/2.4
#   Lời giải:   python qk.py solution DistinguishUnitaries/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Identity, CNOTs or SWAP?
# Input: A function that implements a two-qubit unitary transformation:
#        either I⊗I, CNOT₁₂, CNOT₂₁, or SWAP gate.
# Output: 0 if the given operation is I⊗I,
#         1 if the given operation is CNOT₁₂,
#         2 if the given operation is CNOT₂₁,
#         3 if the given operation is SWAP.
# You are allowed to apply the given operation at most twice.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def distinguish_two_qubit_unitaries(unitary_func) -> int:
    """
    Distinguish between I⊗I, CNOT₁₂, CNOT₂₁, and SWAP gates.

    Args:
        unitary_func: A function that takes (qc, qubits) and applies one of four gates

    Returns:
        0 if I⊗I, 1 if CNOT₁₂, 2 if CNOT₂₁, 3 if SWAP
    """
    # Your code here
    pass
