# ══════════════════════════════════════════════════════════════════════════════
# BÀI 117/350  ·  Bậc 5 · Giao thức lượng tử
# SuperdenseCoding/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SuperdenseCoding/3
#   Gợi ý:      python qk.py hint SuperdenseCoding/3
#   Lời giải:   python qk.py solution SuperdenseCoding/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3. Decode the message and reset the qubits (Bob's task)
# Decode the message using the qubit received from Alice and reset both qubits to a |00⟩ state.
# Inputs:
#     1) The qubit received from Alice qAlice.
#     2) Bob's part of the entangled pair qBob.
# Goal: Retrieve two bits of classical data from the qubits and return them.
# The state of the qubits at the end should be |00⟩.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def decode_message_from_qubits(qc: QuantumCircuit, q_alice: int, q_bob: int) -> tuple[bool, bool]:
    """
    Decode the classical message from the Bell state and reset qubits.

    Args:
        qc: Quantum circuit containing the encoded Bell state
        q_alice: Index of Alice's qubit
        q_bob: Index of Bob's qubit

    Returns:
        Tuple of (bit1, bit2) representing the decoded message
    """
    # Your code here
    pass
