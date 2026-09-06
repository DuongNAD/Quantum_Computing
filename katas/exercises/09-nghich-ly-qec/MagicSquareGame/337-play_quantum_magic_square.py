# ══════════════════════════════════════════════════════════════════════════════
# BÀI 337/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# MagicSquareGame/2.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run MagicSquareGame/2.7
#   Gợi ý:      python qk.py hint MagicSquareGame/2.7
#   Lời giải:   python qk.py solution MagicSquareGame/2.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.7. Play the magic square game using the quantum strategy
# Input: Functions `ask_alice(qc, qs) -> (cbits, decoder)` and
#        `ask_bob(qc, qs) -> (cbits, decoder)` as produced in 2.6 (with the
#        row/column indices already bound into the closure).  Each appends its
#        player's basis-change + measurements to the shared circuit and returns
#        (classical_bit_indices, decoder_callable).
# Goal: Return (alice_row, bob_col) as two lists of three +/-1 integers.
#
# Key architectural requirement: simulate the full 4-qubit circuit ONCE so
# that Alice's and Bob's measurement outcomes come from the shared Bell-pair
# state and hence respect the Mermin-Peres correlations.

from qiskit import QuantumCircuit
from typing import Callable

def create_entangled_state(qc: QuantumCircuit, qs: list[int]) -> QuantumCircuit:
    """Helper: prepare the two Bell pairs (qs[0], qs[2]) and (qs[1], qs[3])."""
    qc.h(qs[0]); qc.cx(qs[0], qs[2])
    qc.h(qs[1]); qc.cx(qs[1], qs[3])
    return qc

def play_quantum_magic_square(ask_alice: Callable, ask_bob: Callable) -> tuple:
    """
    Play one round of the magic square game.

    Args:
        ask_alice: (qc, qs) -> (cbit_indices, decoder)
        ask_bob:   (qc, qs) -> (cbit_indices, decoder)

    Returns:
        (alice_row, bob_column) as lists of three +/-1 integers.
    """
    # Your code here
    pass
