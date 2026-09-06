# ══════════════════════════════════════════════════════════════════════════════
# BÀI 325/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# GHZGame/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GHZGame/2.2
#   Gợi ý:      python qk.py hint GHZGame/2.2
#   Lời giải:   python qk.py solution GHZGame/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Quantum strategy
# Inputs:
#     1) The input bit r, s, or t for one of the three players,
#     2) the index of that player's qubit in the SHARED circuit,
#     3) the SHARED quantum circuit `qc` containing the entangled triple.
# Goal: Append gates to `qc` that measure the player's qubit in the Z basis
#       if the input bit is 0, or in the X basis if it is 1.  Allocate a
#       classical bit and return its index (int).
#
# Note: Do NOT run the simulator inside this function.  The orchestrator in
#       task 2.3 simulates the full circuit ONCE so that the three players'
#       outcomes are correlated GHZ-state measurements.

from qiskit import QuantumCircuit

def quantum_strategy(qc: QuantumCircuit, input_bit: bool, qubit: int) -> int:
    """
    Append the player's measurement to the shared circuit.

    Args:
        qc: Shared quantum circuit (will be modified in place)
        input_bit: The player's input bit (r, s, or t)
        qubit: Index of the player's qubit

    Returns:
        Classical-bit index where the outcome will be written.
    """
    # Your code here
    pass
