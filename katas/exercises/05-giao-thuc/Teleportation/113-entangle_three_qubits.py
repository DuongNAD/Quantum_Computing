# ══════════════════════════════════════════════════════════════════════════════
# BÀI 113/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/4.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/4.1
#   Gợi ý:      python qk.py hint Teleportation/4.1
#   Lời giải:   python qk.py solution Teleportation/4.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4.1*. Entangled trio
# Input: three qubits qAlice, qBob, and qCharlie, each in |0⟩ state.
# Goal: create an entangled state |Ψ³⟩ = (|000⟩ + |011⟩ + |101⟩ + |110⟩) / 2 on these qubits.
#
# In the context of the quantum teleportation protocol, this is the preparation step:
# qubits qAlice, qBob, and qCharlie will be sent to Alice, Bob, and Charlie respectively.

from qiskit import QuantumCircuit

def entangle_three_qubits(qc: QuantumCircuit, q_alice: int, q_bob: int, q_charlie: int) -> QuantumCircuit:
    """
    Create three-qubit entangled state |Ψ³⟩ = (|000⟩ + |011⟩ + |101⟩ + |110⟩) / 2.

    Args:
        qc: Quantum circuit to modify
        q_alice: Alice's qubit index
        q_bob: Bob's qubit index
        q_charlie: Charlie's qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
