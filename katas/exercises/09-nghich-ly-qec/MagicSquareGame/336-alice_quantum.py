# ══════════════════════════════════════════════════════════════════════════════
# BÀI 336/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.6
#   Gợi ý:      python qk.py hint MagicSquareGame/2.6
#   Lời giải:   python qk.py solution MagicSquareGame/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6. Alice and Bob's quantum strategy (Mermin-Peres magic square)
# Both players share the entangled state prepared in 2.1: two Bell pairs
# (|Phi+>_{q0,q2}) (x) (|Phi+>_{q1,q3}), with Alice holding (q0, q1) and Bob
# holding (q2, q3).
#
# Alice's inputs:
#     1) row_index (0, 1, or 2)
#     2) her two shared-circuit qubit indices (a list of length 2)
#     3) the SHARED circuit qc
#
# Alice's output: a tuple (cbit_indices, decoder) where:
#     - cbit_indices is the list of classical bit indices her 2 measurement
#       results will be written to (length 2),
#     - decoder is a function that, given the 2 measurement bits, returns
#       her 3-cell row [+/- 1, +/- 1, +/- 1] for the magic square.
# Bob is symmetric with column_index.
#
# The 3x3 magic square used here is the Peres arrangement:
#     Row 0:   +I(x)Z     +Z(x)I     +Z(x)Z
#     Row 1:   +X(x)I     +I(x)X     +X(x)X
#     Row 2:   -X(x)Z     -Z(x)X     +Y(x)Y
# (each row product = +I, each column product = -I -- a valid magic square).
#
# Do NOT run a simulator inside these functions; the orchestrator in task 2.7
# will simulate the full circuit ONCE so that Alice's and Bob's measurements
# are correlated Bell-pair samples.

from qiskit import QuantumCircuit, ClassicalRegister
from typing import Callable

def alice_quantum(qc: QuantumCircuit, row_index: int, qs: list[int]) -> tuple[list[int], Callable[[int, int], list[int]]]:
    """
    Alice's quantum strategy: append the row-r diagonalizing Clifford + Z-basis
    measurements of her two qubits to `qc`, and return (cbit_indices, decoder).
    """
    # Your code here
    pass

def bob_quantum(qc: QuantumCircuit, column_index: int, qs: list[int]) -> tuple[list[int], Callable[[int, int], list[int]]]:
    """
    Bob's quantum strategy: append the column-c diagonalizing Clifford + Z-basis
    measurements of his two qubits to `qc`, and return (cbit_indices, decoder).
    """
    # Your code here
    pass
