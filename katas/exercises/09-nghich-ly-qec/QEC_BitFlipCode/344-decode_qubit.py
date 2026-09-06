# ══════════════════════════════════════════════════════════════════════════════
# BÀI 344/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/6
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/6
#   Lời giải:   python qk.py solution QEC_BitFlipCode/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 6. Decode logical qubit
# Input: A quantum circuit with encoded state α|000⟩ + β|111⟩.
# Goal: Decode back to single qubit state α|0⟩ + β|1⟩.

from qiskit import QuantumCircuit

def decode_qubit(qc: QuantumCircuit, data: int, ancillas: list) -> QuantumCircuit:
    """
    Decode 3-qubit bit flip code back to single qubit.

    Args:
        qc: Quantum circuit with encoded state
        data: Index of the data qubit (will contain decoded state)
        ancillas: List of 2 ancilla qubit indices

    Returns:
        Modified quantum circuit with decoded state on data qubit
    """
    # Your code here
    pass
