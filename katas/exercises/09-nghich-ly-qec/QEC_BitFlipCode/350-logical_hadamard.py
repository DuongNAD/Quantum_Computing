# ══════════════════════════════════════════════════════════════════════════════
# BÀI 350/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/12
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/12
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/12
#   Lời giải:   python qk.py solution QEC_BitFlipCode/12
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 12. Logical Hadamard gate
# Input: An encoded logical qubit (3 physical qubits).
# Goal: Apply logical Hadamard to transform |0>_L <-> |+>_L and |1>_L <-> |->_L
#       (where |+>_L = (|000> + |111>)/sqrt(2) and |->_L = (|000> - |111>)/sqrt(2)).
#
# Note: Unlike logical X (which is transversal X⊗X⊗X) and logical Z (which is
#       transversal Z on any one qubit), transversal H on the 3-qubit repetition
#       code does NOT implement logical H -- it takes |0>_L = |000> to |+++>,
#       which is OUTSIDE the code space.  A valid logical Hadamard must first
#       decode the repetition code onto a single qubit, apply H, then re-encode.

from qiskit import QuantumCircuit

def logical_hadamard(qc: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Apply logical Hadamard gate to a 3-qubit repetition-code encoded qubit.

    Args:
        qc: Quantum circuit with encoded state
        qubits: List of 3 qubit indices for the code (qubits[0] is the "data" qubit)

    Returns:
        Modified quantum circuit with logical H applied (state stays inside the code space)
    """
    # Your code here
    pass
