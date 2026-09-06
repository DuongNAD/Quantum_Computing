# ══════════════════════════════════════════════════════════════════════════════
# BÀI 093/350  ·  Bậc 5 · Giao thức lượng tử
# examples/BasicQuantumTeleportation
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/BasicQuantumTeleportation
#   Gợi ý:      python qk.py hint examples/BasicQuantumTeleportation
#   Lời giải:   python qk.py solution examples/BasicQuantumTeleportation
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Basic Quantum Teleportation Protocol
# Goal: Implement the quantum teleportation protocol to transfer an unknown quantum state.
#       Alice has a qubit in unknown state |Ψ⟩ and wants to send it to Bob using classical communication and entanglement.

from qiskit import QuantumCircuit
from typing import Tuple

def quantum_teleportation_alice(qc: QuantumCircuit, psi: int, alice: int, bob: int) -> QuantumCircuit:
    """
    Alice's part of quantum teleportation protocol.

    Args:
        qc: Quantum circuit
        psi: Qubit with unknown state to teleport
        alice: Alice's half of entangled pair
        bob: Bob's half of entangled pair (not directly accessible to Alice)

    Returns:
        Modified quantum circuit after Alice's operations
    """
    # Your code here
    pass
