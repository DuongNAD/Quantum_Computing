# ══════════════════════════════════════════════════════════════════════════════
# BÀI 316/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/2.2
#   Gợi ý:      python qk.py hint CHSHGame/2.2
#   Lời giải:   python qk.py solution CHSHGame/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Alice's quantum strategy
# Inputs:
#     1) Alice's input bit X,
#     2) the index of Alice's qubit in the SHARED circuit,
#     3) the SHARED quantum circuit `qc` that already contains Alice and Bob's
#        entangled pair.
# Goal: Append to `qc` the gates that measure Alice's qubit in the Z basis
#       if X is 0, or in the X basis if X is 1.  Allocate a classical bit for
#       the outcome and return its index (int).
#
# Note: Do NOT run the simulator inside this function.  The orchestrator in
#       task 2.5 simulates the full circuit ONCE so that Alice's and Bob's
#       outcomes are correlated Bell-pair measurements rather than independent
#       samples.

from qiskit import QuantumCircuit

def alice_quantum(qc: QuantumCircuit, bit: bool, qubit: int) -> int:
    """
    Append Alice's measurement to the shared circuit.

    Args:
        qc: Shared quantum circuit (will be modified in place)
        bit: Alice's input bit X
        qubit: Index of Alice's qubit in the shared circuit

    Returns:
        The classical-bit index into which Alice's measurement result will be written.
    """
    # Your code here
    pass
