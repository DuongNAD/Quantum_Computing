# ══════════════════════════════════════════════════════════════════════════════
# BÀI 348/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/10
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/10
#   Lời giải:   python qk.py solution QEC_BitFlipCode/10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 10. Full error correction cycle
# Input: A quantum circuit with data qubit to encode, ancillas, and syndrome qubits.
# Goal: Perform complete encode-error-syndrome-correct cycle.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def full_qec_cycle(qc: QuantumCircuit, data: int, ancillas: list, syndrome: list, error_qubit: int = None) -> QuantumCircuit:
    """
    Perform full QEC cycle: encode, introduce error, measure syndrome, correct.

    Args:
        qc: Quantum circuit with data qubit in state to protect
        data: Data qubit index
        ancillas: List of 2 ancilla qubit indices
        syndrome: List of 2 syndrome qubit indices
        error_qubit: Optional qubit index to introduce error (None for no error)

    Returns:
        Modified quantum circuit after error correction
    """
    # Your code here
    pass
