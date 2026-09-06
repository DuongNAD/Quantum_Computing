# ══════════════════════════════════════════════════════════════════════════════
# BÀI 109/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/2.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/2.1
#   Gợi ý:      python qk.py hint Teleportation/2.1
#   Lời giải:   python qk.py solution Teleportation/2.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.1. Reconstruct the message if the entangled qubits were in the state |φ⁻⟩ = (|00⟩ - |11⟩) / sqrt(2)
# In this section we will take a look at the changes in the reconstruction process (Bob's task)
# if the qubits shared between Alice and Bob are entangled in a different state.
# Alice's part of the protocol remains the same in all tasks.
# Input: Bob's part of the entangled pair of qubits qBob and the tuple of classical bits received from Alice.
# Goal: transform Bob's qubit qBob into the state in which the message qubit had been originally.

from qiskit import QuantumCircuit

def reconstruct_message_phi_minus(qc: QuantumCircuit, q_bob: int, message_bit: bool, alice_bit: bool) -> QuantumCircuit:
    """
    Reconstruct message when shared pair was in |φ⁻⟩ state.

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
