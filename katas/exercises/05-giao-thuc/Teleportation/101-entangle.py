# ══════════════════════════════════════════════════════════════════════════════
# BÀI 101/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.1
#   Gợi ý:      python qk.py hint Teleportation/1.1
#   Lời giải:   python qk.py solution Teleportation/1.1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.1. Entangled pair
# Input: two qubits qAlice and qBob, each in |0⟩ state.
# Goal: prepare a Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2) on these qubits.
#
# In the context of the quantum teleportation protocol, this is the preparation step:
# qubits qAlice and qBob will be sent to Alice and Bob, respectively.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

def entangle(qc: QuantumCircuit, q_alice: int, q_bob: int) -> QuantumCircuit:
    """
    Create Bell state |φ⁺⟩ between Alice's and Bob's qubits.

    Args:
        qc: Quantum circuit to modify
        q_alice: Alice's qubit index
        q_bob: Bob's qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
