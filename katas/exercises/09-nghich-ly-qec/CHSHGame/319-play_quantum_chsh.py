# ══════════════════════════════════════════════════════════════════════════════
# BÀI 319/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# CHSHGame/2.5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run CHSHGame/2.5
#   Gợi ý:      python qk.py hint CHSHGame/2.5
#   Lời giải:   python qk.py solution CHSHGame/2.5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.5. Play the CHSH game using the quantum strategy
# Input: Functions `ask_alice(qc, qubit) -> int` and `ask_bob(qc, qubit) -> int`
#        (as produced in 2.2 and 2.4 with the input bit already bound).  Each
#        function APPENDS Alice's / Bob's measurement gates to the shared
#        circuit `qc` and returns the classical-bit index that will hold its
#        outcome.  Alice and Bob have already been told what their input bits
#        X and Y are.
# Goal: Return Alice and Bob's output bits (A, B) as a tuple of two bools.
#
# Key architectural requirement: simulate the full circuit ONCE so that the
# two measurements are genuinely correlated Bell-pair outcomes, not
# independent samples.

from qiskit import QuantumCircuit
from typing import Callable

def play_quantum_chsh(ask_alice: Callable[[QuantumCircuit, int], int],
                     ask_bob: Callable[[QuantumCircuit, int], int]) -> tuple[bool, bool]:
    """
    Play one round of the CHSH game using shared entanglement.

    Args:
        ask_alice: (qc, qubit_index) -> cbit_index; appends Alice's strategy
        ask_bob:   (qc, qubit_index) -> cbit_index; appends Bob's strategy

    Returns:
        (alice_result, bob_result) as booleans.
    """
    # Your code here
    pass
