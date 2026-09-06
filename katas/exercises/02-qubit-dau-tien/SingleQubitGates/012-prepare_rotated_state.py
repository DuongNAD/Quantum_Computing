# ══════════════════════════════════════════════════════════════════════════════
# BÀI 012/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/6
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/6
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 6: Prepare Rotated State
# Input: Real numbers α and β such that α² + β² = 1, and a qubit in |0⟩.
# Goal: Transform the qubit to state α|0⟩ - iβ|1⟩ using rotation gates.

from qiskit import QuantumCircuit
import numpy as np

def prepare_rotated_state(qc: QuantumCircuit, alpha: float, beta: float, q: int) -> QuantumCircuit:
    """
    Prepare state α|0⟩ - iβ|1⟩ from |0⟩.

    Args:
        qc: Quantum circuit to modify
        alpha: Real amplitude for |0⟩
        beta: Real amplitude magnitude for |1⟩ (with -i phase)
        q: Qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
