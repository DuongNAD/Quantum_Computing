# ══════════════════════════════════════════════════════════════════════════════
# BÀI 111/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/2.3
#   Gợi ý:      python qk.py hint Teleportation/2.3
#   Lời giải:   python qk.py solution Teleportation/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Reconstruct the message if the entangled qubits were in the state |Ψ⁻⟩ = (|01⟩ - |10⟩) / sqrt(2)
# Input: Bob's part of the entangled pair of qubits qBob and the tuple of classical bits received from Alice.
# Goal: transform Bob's qubit qBob into the state in which the message qubit had been originally.

from qiskit import QuantumCircuit

def reconstruct_message_psi_minus(qc: QuantumCircuit, q_bob: int, message_bit: bool, alice_bit: bool) -> QuantumCircuit:
    """
    Reconstruct message when shared pair was in |Ψ⁻⟩ state.

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
