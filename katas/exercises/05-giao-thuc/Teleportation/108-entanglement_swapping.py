# ══════════════════════════════════════════════════════════════════════════════
# BÀI 108/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.8
#   Gợi ý:      python qk.py hint Teleportation/1.8
#   Lời giải:   python qk.py solution Teleportation/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Entanglement swapping
# Alice and Bob, independently from each other, each hold an entangled qubit pair in the
# state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2). They hand off one part of their pair to Charlie.
#
# Charlie can now teleport the state of Alice's qubit he holds onto Bob's remaining qubit,
# thus teleporting the entanglement.
# Just like in "standard" teleportation, Bob still needs to apply the reconstruction steps -
# based on Charlie's measurement results - to the other qubit in his possession.
#
# After this procedure the state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2) now spans across
# Alice's and Bob's qubits which they didn't send to Charlie. They are now maximally entangled,
# even though they never interacted in the first place!
#
# Output: A tuple of two functions.
# The first function is Charlie's part of the protocol.
# It will take two qubits as input (the ones Alice and Bob sent to Charlie),
# and produce a message, encoded as an integer, that will be sent to Bob.
# The second function is Bob's part of the protocol.
# It will take the qubit that remained in Bob's possession and Charlie's integer as input,
# and use the integer to adjust the state of Bob's qubit,
# so that Alice's and Bob's qubits end up in the state |φ⁺⟩.

from qiskit import QuantumCircuit

def entanglement_swapping() -> tuple:
    """
    Return tuple of (Charlie's operation, Bob's operation) for entanglement swapping.

    Returns:
        Tuple of two functions:
        - First function: (qc, q_alice1, q_bob1) -> int (Charlie's measurement)
        - Second function: (qc, q_bob2, message) -> None (Bob's reconstruction)
    """
    # Your code here
    pass
