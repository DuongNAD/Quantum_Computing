# ══════════════════════════════════════════════════════════════════════════════
# BÀI 339/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/1
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/1
#   Lời giải:   python qk.py solution QEC_BitFlipCode/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1. Encode logical |0⟩
# Input: A quantum circuit with 3 qubits initialized to |000⟩.
# Goal: Encode the logical |0⟩ state using the 3-qubit bit flip code.
# The logical |0⟩ is encoded as |000⟩ (all three physical qubits in |0⟩).

from qiskit import QuantumCircuit

def encode_logical_zero(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Encode logical |0⟩ using 3-qubit bit flip code.

    Args:
        qc: Quantum circuit to modify
        qubits: List of 3 qubit indices for the code

    Returns:
        Modified quantum circuit with encoded |0⟩_L
    """
    # Your code here
    pass
