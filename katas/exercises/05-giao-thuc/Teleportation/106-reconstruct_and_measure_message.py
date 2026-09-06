# ══════════════════════════════════════════════════════════════════════════════
# BÀI 106/350  ·  Bậc 5 · Giao thức lượng tử
# Teleportation/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Teleportation/1.6
#   Gợi ý:      python qk.py hint Teleportation/1.6
#   Lời giải:   python qk.py solution Teleportation/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Reconstruct and measure the message state (Bob's task)
# Transform Bob's qubit into the required state using the two classical bits
# received from Alice and measure it in the same basis in which she prepared the message.
# Inputs:
#      1) Bob's part of the entangled pair of qubits qBob.
#      2) The tuple of classical bits received from Alice,
#         in the format used in task 1.5.
#      3) The PauliX, PauliY, or PauliZ basis in which the
#         message qubit was originally prepared
# Output:
#      A Bool indicating the eigenstate in which the message qubit was prepared, 'One' as
#      'True' and 'Zero' as 'False'.
# To get the output, transform Bob's qubit qBob into the state
# in which the message qubit was originally prepared, then measure it.
# The state of the qubit qBob in the end of the operation doesn't matter.

from qiskit import QuantumCircuit

def reconstruct_and_measure_message(qc: QuantumCircuit, q_bob: int, alice_bits: tuple, basis: str) -> bool:
    """
    Reconstruct teleported message and measure in specified basis.

    Args:
        qc: Quantum circuit to modify
        q_bob: Bob's qubit index
        alice_bits: Tuple (b1, b2) received from Alice
        basis: Pauli basis ('X', 'Y', or 'Z') for measurement

    Returns:
        Boolean indicating measurement result (True for One, False for Zero)
    """
    # Your code here
    return False
