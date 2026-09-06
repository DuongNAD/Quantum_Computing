# ══════════════════════════════════════════════════════════════════════════════
# BÀI 112/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/3.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/3.1
#   Gợi ý:      python qk.py hint Teleportation/3.1
#   Lời giải:   python qk.py solution Teleportation/3.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.1. Measurement-free teleportation
# The principle of deferred measurement claims that measurements can be moved from an intermediate stage
# of a quantum circuit to the end of the circuit. If the measurement results are used to perform
# classically controlled operations, they can be replaced by controlled quantum operations.
# Inputs:
#     1) The two qubits qAlice and qBob in |φ⁺⟩ state.
#     2) The message qubit qMessage in the state |Ψ⟩ to be teleported.
# Goal: transform Bob's qubit qBob into the state |Ψ⟩ using no measurements.
# At the end of the operation qubits qAlice and qMessage should not be entangled with qBob.

from qiskit import QuantumCircuit

def measurement_free_teleport(qc: QuantumCircuit, q_alice: int, q_bob: int, q_message: int) -> QuantumCircuit:
    """
    Quantum teleportation without intermediate measurements using controlled operations.

    Args:
        qc: Quantum circuit containing qubits (Alice and Bob start entangled)
        q_alice: Index of Alice's qubit (part of |φ⁺⟩ pair)
        q_bob: Index of Bob's qubit (part of |φ⁺⟩ pair)
        q_message: Index of message qubit to teleport

    Returns:
        Modified quantum circuit with message state teleported to Bob's qubit
    """
    # Your code here
    pass
