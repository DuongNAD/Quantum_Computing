# ══════════════════════════════════════════════════════════════════════════════
# BÀI 346/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/8
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/8
#   Lời giải:   python qk.py solution QEC_BitFlipCode/8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 8. Logical Z gate
# Input: A quantum circuit with encoded logical qubit.
# Goal: Apply logical Z gate (phase flip) to the encoded state.
# Logical Z adds -1 phase to |1⟩_L: α|000⟩ + β|111⟩ → α|000⟩ - β|111⟩.

from qiskit import QuantumCircuit

def logical_z(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Apply logical Z gate to encoded qubit.

    Args:
        qc: Quantum circuit with encoded state
        qubits: List of 3 qubit indices for the code

    Returns:
        Modified quantum circuit with logical Z applied
    """
    # Your code here
    pass
