# ══════════════════════════════════════════════════════════════════════════════
# BÀI 102/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.2
#   Gợi ý:      python qk.py hint Teleportation/1.2
#   Lời giải:   python qk.py solution Teleportation/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Send the message (Alice's task)
# Entangle the message qubit with Alice's qubit and extract two classical bits to be sent to Bob.
# Inputs:
#     1) Alice's part of the entangled pair of qubits qAlice.
#     2) The message qubit qMessage.
# Output:
#     Two classical bits Alice will send to Bob via classical channel as a tuple of Bool values.
#     The first bit in the tuple should hold the result of measurement of the message qubit,
#     the second bit - the result of measurement of Alice's qubit.
# The state of the qubits in the end of the operation doesn't matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def send_message(qc: QuantumCircuit, q_alice: int, q_message: int) -> tuple[bool, bool]:
    """
    Perform Bell measurement on message and Alice's qubits.

    Args:
        qc: Quantum circuit containing the qubits
        q_alice: Index of Alice's qubit (part of entangled pair)
        q_message: Index of message qubit to teleport

    Returns:
        Tuple of (message_bit, alice_bit) measurement results
    """
    # Your code here
    pass
