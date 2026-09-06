# ══════════════════════════════════════════════════════════════════════════════
# BÀI 013/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/7
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/7
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/7
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/7
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 7: Prepare Arbitrary State
# Input: Real numbers α, β, θ and a qubit in |0⟩.
# Goal: Transform the qubit to state α|0⟩ + e^(iθ)β|1⟩.

from qiskit import QuantumCircuit
import numpy as np

def prepare_arbitrary_state(qc: QuantumCircuit, alpha: float, beta: float, theta: float, q: int) -> QuantumCircuit:
    """
    Prepare state α|0⟩ + e^(iθ)β|1⟩ from |0⟩.

    Args:
        qc: Quantum circuit to modify
        alpha: Real amplitude for |0⟩
        beta: Real amplitude magnitude for |1⟩
        theta: Phase angle for |1⟩ component
        q: Qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
