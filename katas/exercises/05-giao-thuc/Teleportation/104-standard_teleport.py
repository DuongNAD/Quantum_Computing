# ══════════════════════════════════════════════════════════════════════════════
# BÀI 104/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.4
#   Gợi ý:      python qk.py hint Teleportation/1.4
#   Lời giải:   python qk.py solution Teleportation/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Standard teleportation protocol
# Put together the steps implemented in tasks 1.1 - 1.3 to implement the full teleportation protocol.
# Inputs:
#     1) The two qubits qAlice and qBob in |0⟩ state.
#     2) The message qubit qMessage in the state |Ψ⟩ to be teleported.
# Goal: transform Bob's qubit qBob into the state |Ψ⟩.
# The state of the qubits qAlice and qMessage in the end of the operation doesn't matter.

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

def standard_teleport(qc: QuantumCircuit, q_alice: int, q_bob: int, q_message: int) -> QuantumCircuit:
    """
    Complete quantum teleportation protocol.

    Args:
        qc: Quantum circuit containing all qubits
        q_alice: Index of Alice's qubit (initially |0⟩)
        q_bob: Index of Bob's qubit (initially |0⟩)
        q_message: Index of message qubit (in state |Ψ⟩ to teleport)

    Returns:
        Modified quantum circuit where Bob's qubit is in the original message state
    """
    # Your code here
    pass
