# ══════════════════════════════════════════════════════════════════════════════
# BÀI 340/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/2
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/2
#   Lời giải:   python qk.py solution QEC_BitFlipCode/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Encode logical |1⟩
# Input: A quantum circuit with 3 qubits initialized to |000⟩.
# Goal: Encode the logical |1⟩ state using the 3-qubit bit flip code.
# The logical |1⟩ is encoded as |111⟩ (all three physical qubits in |1⟩).

from qiskit import QuantumCircuit

def encode_logical_one(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Encode logical |1⟩ using 3-qubit bit flip code.

    Args:
        qc: Quantum circuit to modify
        qubits: List of 3 qubit indices for the code

    Returns:
        Modified quantum circuit with encoded |1⟩_L
    """
    # Your code here
    pass
