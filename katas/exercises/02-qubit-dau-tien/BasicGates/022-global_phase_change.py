# ══════════════════════════════════════════════════════════════════════════════
# BÀI 022/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.7
#   Gợi ý:      python qk.py hint BasicGates/1.7
#   Lời giải:   python qk.py solution BasicGates/1.7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.7. Global phase change
# Input: A qubit in state β|0⟩ + γ|1⟩.
# Goal: Change the state of the qubit to - β|0⟩ - γ|1⟩.
#
# Note: This change on its own is not observable -
# there is no experiment you can do on a standalone qubit
# to figure out whether it acquired the global phase or not.
# However, you can use a controlled version of this operation
# to observe the global phase it introduces. This is used
# in later katas as part of more complicated tasks.

from qiskit import QuantumCircuit
import numpy as np

def global_phase_change(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply global phase change to multiply the state by -1.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply global phase change

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
