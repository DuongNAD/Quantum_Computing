# ══════════════════════════════════════════════════════════════════════════════
# BÀI 318/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/2.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/2.4
#   Gợi ý:      python qk.py hint CHSHGame/2.4
#   Lời giải:   python qk.py solution CHSHGame/2.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.4. Bob's quantum strategy
# Inputs:
#     1) Bob's input bit Y,
#     2) the index of Bob's qubit in the SHARED circuit,
#     3) the SHARED quantum circuit `qc` that already contains Alice and Bob's
#        entangled pair.
# Goal: Append gates to `qc` that measure Bob's qubit in the (cos(pi/8), sin(pi/8))
#       basis if Y is 0, or in the (cos(-pi/8), sin(-pi/8)) basis if Y is 1.  In
#       Qiskit, this is done via a y-axis rotation followed by a Z-basis
#       measurement.  Allocate a classical bit and return its index (int).
#
# Note: Do NOT run the simulator inside this function.  The orchestrator in
#       task 2.5 simulates the full circuit ONCE so that Alice's and Bob's
#       outcomes are correlated Bell-pair measurements.

from qiskit import QuantumCircuit
import numpy as np

def bob_quantum(qc: QuantumCircuit, bit: bool, qubit: int) -> int:
    """
    Append Bob's measurement to the shared circuit.

    Args:
        qc: Shared quantum circuit (will be modified in place)
        bit: Bob's input bit Y
        qubit: Index of Bob's qubit in the shared circuit

    Returns:
        Classical-bit index into which Bob's measurement result will be written.
    """
    # Your code here
    pass
