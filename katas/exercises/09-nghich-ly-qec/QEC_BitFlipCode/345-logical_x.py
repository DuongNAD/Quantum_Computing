# ══════════════════════════════════════════════════════════════════════════════
# BÀI 345/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/7
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/7
#   Lời giải:   python qk.py solution QEC_BitFlipCode/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 7. Logical X gate
# Input: A quantum circuit with encoded logical qubit.
# Goal: Apply logical X gate (bit flip) to the encoded state.
# Logical X flips |0⟩_L ↔ |1⟩_L, i.e., |000⟩ ↔ |111⟩.

from qiskit import QuantumCircuit

def logical_x(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Apply logical X gate to encoded qubit.

    Args:
        qc: Quantum circuit with encoded state
        qubits: List of 3 qubit indices for the code

    Returns:
        Modified quantum circuit with logical X applied
    """
    # Your code here
    pass
