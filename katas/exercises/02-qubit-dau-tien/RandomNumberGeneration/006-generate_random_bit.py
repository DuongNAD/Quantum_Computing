# ══════════════════════════════════════════════════════════════════════════════
# BÀI 006/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/RandomNumberGeneration/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/RandomNumberGeneration/1
#   Gợi ý:      python qk.py hint tutorials/RandomNumberGeneration/1
#   Lời giải:   python qk.py solution tutorials/RandomNumberGeneration/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1: Random Bit Generation
# Goal: Generate a random bit using quantum superposition and measurement.
#       Create equal superposition and measure to get 0 or 1 with 50% probability each.

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import random

def generate_random_bit() -> int:
    """
    Generate a random bit (0 or 1) using quantum mechanics.

    Returns:
        Random bit: 0 or 1 with equal probability
    """
    # Your code here
    pass
