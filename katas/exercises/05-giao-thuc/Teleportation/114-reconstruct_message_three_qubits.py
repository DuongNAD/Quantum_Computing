# ══════════════════════════════════════════════════════════════════════════════
# BÀI 114/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/4.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/4.2
#   Gợi ý:      python qk.py hint Teleportation/4.2
#   Lời giải:   python qk.py solution Teleportation/4.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4.2*. Reconstruct the message (Charlie's task)
# Alice has a message qubit in the state |Ψ⟩ to be teleported, she has entangled it with
# her own qubit from |Ψ³⟩ in the same manner as task 1.2 and extracted two classical bits
# in order to send them to Charlie. Bob has also measured his own qubit from |Ψ³⟩ and sent
# Charlie the result.
#
# Transform Charlie's qubit into the required state using the two classical bits
# received from Alice, and the one classical bit received from Bob.
# Inputs:
#      1) Charlie's part of the entangled trio of qubits qCharlie.
#      2) The tuple of classical bits received from Alice,
#         in the format used in task 1.2.
#      3) A classical bit resulting from the measurement of Bob's qubit.
# Goal: transform Charlie's qubit qCharlie into the state in which the message qubit had been originally.

from qiskit import QuantumCircuit
from typing import Tuple

def reconstruct_message_three_qubits(qc: QuantumCircuit, q_charlie: int, alice_bits: Tuple[bool, bool], bob_bit: bool) -> QuantumCircuit:
    """
    Reconstruct message using measurements from Alice and Bob in three-qubit teleportation.

    Args:
        qc: Quantum circuit to modify
        q_charlie: Index of Charlie's qubit
        alice_bits: Tuple of (message_measurement, alice_measurement) from Alice
        bob_bit: Measurement result from Bob's qubit

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
