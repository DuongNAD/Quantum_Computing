# ══════════════════════════════════════════════════════════════════════════════
# BÀI 103/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.3
#   Gợi ý:      python qk.py hint Teleportation/1.3
#   Lời giải:   python qk.py solution Teleportation/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Reconstruct the message (Bob's task)
# Transform Bob's qubit into the required state using the two classical bits received from Alice.
# Inputs:
#     1) Bob's part of the entangled pair of qubits qBob.
#     2) The tuple of classical bits received from Alice, in the format used in task 1.2.
# Goal: transform Bob's qubit qBob into the state in which the message qubit had been originally.

from qiskit import QuantumCircuit

def reconstruct_message(qc: QuantumCircuit, q_bob: int, message_bit: bool, alice_bit: bool) -> QuantumCircuit:
    """
    Apply corrections to Bob's qubit based on Alice's measurement results.

    Args:
        qc: Quantum circuit to modify
        q_bob: Index of Bob's qubit
        message_bit: First classical bit from Alice (message measurement)
        alice_bit: Second classical bit from Alice (Alice's qubit measurement)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
