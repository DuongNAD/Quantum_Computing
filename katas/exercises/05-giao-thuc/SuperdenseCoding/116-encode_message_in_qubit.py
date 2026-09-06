# ══════════════════════════════════════════════════════════════════════════════
# BÀI 116/350  ·  Bậc 5 · Giao thức lượng tử
# SuperdenseCoding/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run SuperdenseCoding/2
#   Gợi ý:      python qk.py hint SuperdenseCoding/2
#   Lời giải:   python qk.py solution SuperdenseCoding/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2. Send the message (Alice's task)
# Encode the message (two classical bits) in the state of Alice's qubit.
# Inputs:
#     1) Alice's part of the entangled pair of qubits qAlice.
#     2) Two classical bits to encode.
# Goal: Transform Alice's qubit to encode the two classical bits by changing the Bell state:
# [0, 0]: |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2)  (no change)
# [0, 1]: |Ψ⁺⟩ = (|01⟩ + |10⟩) / sqrt(2)  (apply X)
# [1, 0]: |φ⁻⟩ = (|00⟩ - |11⟩) / sqrt(2)  (apply Z)
# [1, 1]: |Ψ⁻⟩ = (|01⟩ - |10⟩) / sqrt(2)  (apply Z then X)

from qiskit import QuantumCircuit

def encode_message_in_qubit(qc: QuantumCircuit, q_alice: int, bit1: bool, bit2: bool) -> QuantumCircuit:
    """
    Encode two classical bits in Alice's qubit for superdense coding.

    Args:
        qc: Quantum circuit to modify
        q_alice: Index of Alice's qubit (part of entangled pair)
        bit1: First classical bit to encode
        bit2: Second classical bit to encode

    Returns:
        Modified quantum circuit with encoded message
    """
    # Your code here
    pass
