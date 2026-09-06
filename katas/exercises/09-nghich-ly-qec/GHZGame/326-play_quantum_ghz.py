# ══════════════════════════════════════════════════════════════════════════════
# BÀI 326/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# GHZGame/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GHZGame/2.3
#   Gợi ý:      python qk.py hint GHZGame/2.3
#   Lời giải:   python qk.py solution GHZGame/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Play the GHZ game using the quantum strategy
# Input: A list of three functions, each with signature (qc, qubit_index) -> int.
#        Each appends that player's measurement to the shared circuit and
#        returns the classical-bit index where their outcome will be written.
#        The three input bits (r, s, t) are already bound into the closures.
# Goal: Return the three players' output bits as a list of bools in the same
#       order as the input strategy list.
#
# Key architectural requirement: simulate the full circuit ONCE so that the
# three measurement outcomes come from a single shot of the entangled state.

from qiskit import QuantumCircuit
from typing import Callable

def play_quantum_ghz(strategies: list[Callable[[QuantumCircuit, int], int]]) -> list[bool]:
    """
    Play one round of the GHZ game using the GHZ-type entangled state.

    Args:
        strategies: List of 3 strategy functions, each (qc, qubit_idx) -> cbit_idx

    Returns:
        List of 3 booleans: the players' output bits (a, b, c).
    """
    # Your code here
    pass
