# ══════════════════════════════════════════════════════════════════════════════
# BÀI 349/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/11
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/11
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/11
#   Lời giải:   python qk.py solution QEC_BitFlipCode/11
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 11. Logical CNOT gate
# Input: Two encoded logical qubits (6 physical qubits total).
# Goal: Apply logical CNOT between two encoded qubits.
# Logical CNOT requires transversal CNOT gates between corresponding physical qubits.

from qiskit import QuantumCircuit

def logical_cnot(qc: QuantumCircuit, control: list, target: list) -> QuantumCircuit:
    """
    Apply logical CNOT between two encoded qubits.

    Args:
        qc: Quantum circuit with two encoded logical qubits
        control: List of 3 qubit indices for control logical qubit
        target: List of 3 qubit indices for target logical qubit

    Returns:
        Modified quantum circuit with logical CNOT applied
    """
    # Your code here
    pass
