# ══════════════════════════════════════════════════════════════════════════════
# BÀI 019/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.4
#   Gợi ý:      python qk.py hint BasicGates/1.4
#   Lời giải:   python qk.py solution BasicGates/1.4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.4*. Amplitude change: |0⟩ to cos(alpha)*|0⟩ + sin(alpha)*|1⟩.
# Inputs:
#     1) Angle alpha, in radians, represented as float.
#     2) A qubit in state β|0⟩ + γ|1⟩.
# Goal: Change the state of the qubit as follows:
#        If the qubit is in state |0⟩, change its state to cos(alpha)*|0⟩ + sin(alpha)*|1⟩.
#        If the qubit is in state |1⟩, change its state to -sin(alpha)*|0⟩ + cos(alpha)*|1⟩.
#        If the qubit is in superposition, change its state according to the effect on basis vectors.
# This is the first operation in this kata that is not self-adjoint,
# i.e., applying it for a second time does not return the qubit to the original state.

from qiskit import QuantumCircuit

def amplitude_change(qc: QuantumCircuit, alpha: float, q: int) -> QuantumCircuit:
    """
    Apply amplitude change rotation to qubit q.

    Args:
        qc: Quantum circuit to modify
        alpha: Rotation angle in radians
        q: Index of qubit to apply rotation

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
