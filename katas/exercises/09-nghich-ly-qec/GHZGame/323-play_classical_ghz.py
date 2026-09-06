# ══════════════════════════════════════════════════════════════════════════════
# BÀI 323/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# GHZGame/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GHZGame/1.4
#   Gợi ý:      python qk.py hint GHZGame/1.4
#   Lời giải:   python qk.py solution GHZGame/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4. Referee classical GHZ game
# Inputs:
#      1) A function which implements a classical strategy
#         (i.e., takes an input bit and produces an output bit),
#      2) A list of 3 input bits that should be passed to the players.
# Output:
#      A list of 3 bits that will be produced if each player uses this strategy.
#
# This function simulates playing the classical GHZ game with a given strategy.

from typing import Callable

def play_classical_ghz(strategy: Callable[[bool], bool], inputs: list[bool]) -> list[bool]:
    """
    Simulate playing the classical GHZ game.

    Args:
        strategy: Function that takes input bit and returns output bit
        inputs: List of 3 input bits [r, s, t] for Alice, Bob, Charlie

    Returns:
        List of 3 output bits [a, b, c] from applying strategy to each input
    """
    # Your code here
    pass
