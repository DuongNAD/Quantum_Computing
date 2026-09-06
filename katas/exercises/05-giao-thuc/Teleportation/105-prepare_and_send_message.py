# ══════════════════════════════════════════════════════════════════════════════
# BÀI 105/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.5
#   Gợi ý:      python qk.py hint Teleportation/1.5
#   Lời giải:   python qk.py solution Teleportation/1.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.5. Prepare a state and send it as a message (Alice's task)
# Given a Pauli basis along with a state 'true' as 'One' or 'false'
# as 'Zero', prepare a message qubit, entangle it with Alice's qubit,
# and extract two classical bits to be sent to Bob.
# Inputs:
#      1) Alice's part of the entangled pair of qubits qAlice.
#      2) A PauliX, PauliY, or PauliZ basis in which the message
#         qubit should be prepared
#      3) A Bool indicating the eigenstate in which the message
#         qubit should be prepared
# Output:
#      Two classical bits Alice will send to Bob via classical channel as a tuple of Bool values.
#      The first bit in the tuple should hold the result of measurement of the message qubit,
#      the second bit - the result of measurement of Alice's qubit.
#      Represent measurement result 'One' as 'true' and 'Zero' as 'false'.
# The state of the qubit qAlice in the end of the operation doesn't matter.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from typing import Tuple

def prepare_and_send_message(qc: QuantumCircuit, q_alice: int, basis: str, state: bool) -> Tuple[bool, bool]:
    """
    Prepare a message in the given basis and state, then perform teleportation protocol.

    Args:
        qc: Quantum circuit containing Alice's qubit (already entangled with Bob's)
        q_alice: Index of Alice's qubit
        basis: Pauli basis ('X', 'Y', or 'Z')
        state: True for |1⟩/|+⟩/|+i⟩, False for |0⟩/|-⟩/|-i⟩

    Returns:
        Tuple of (message_measurement, alice_measurement)
    """
    # Your code here
    pass
