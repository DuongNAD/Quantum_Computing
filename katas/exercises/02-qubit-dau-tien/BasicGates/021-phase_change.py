# ══════════════════════════════════════════════════════════════════════════════
# BÀI 021/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.6
#   Gợi ý:      python qk.py hint BasicGates/1.6
#   Lời giải:   python qk.py solution BasicGates/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6*. Phase change
# Inputs:
#     1) Angle alpha, in radians, represented as float.
#     2) A qubit in state β|0⟩ + γ|1⟩.
# Goal: Change the state of the qubit as follows:
#        If the qubit is in state |0⟩, don't change its state.
#        If the qubit is in state |1⟩, change its state to exp(i*alpha)|1⟩.
#        If the qubit is in superposition, change its state according to the effect on basis vectors.

from qiskit import QuantumCircuit

def phase_change(qc: QuantumCircuit, alpha: float, q: int) -> QuantumCircuit:
    """
    Apply phase change to the |1⟩ component of the qubit state.

    Args:
        qc: Quantum circuit to modify
        alpha: Phase angle in radians
        q: Index of qubit to apply phase change

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
