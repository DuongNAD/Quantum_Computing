# ══════════════════════════════════════════════════════════════════════════════
# BÀI 341/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/3
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/3
#   Lời giải:   python qk.py solution QEC_BitFlipCode/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Encode arbitrary qubit state
# Input: A quantum circuit where qubit 0 has an arbitrary state |ψ⟩ = α|0⟩ + β|1⟩.
# Goal: Encode this state into the 3-qubit bit flip code.
# |ψ⟩_L = α|000⟩ + β|111⟩

from qiskit import QuantumCircuit

def encode_qubit(qc: QuantumCircuit, data: int, ancillas: list) -> QuantumCircuit:
    """
    Encode arbitrary qubit state into 3-qubit bit flip code.

    Args:
        qc: Quantum circuit with data qubit in state |ψ⟩
        data: Index of the data qubit to encode
        ancillas: List of 2 ancilla qubit indices

    Returns:
        Modified quantum circuit with encoded state
    """
    # Your code here
    pass
