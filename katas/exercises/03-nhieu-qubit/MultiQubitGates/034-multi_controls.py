# ══════════════════════════════════════════════════════════════════════════════
# BÀI 034/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitGates/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitGates/5
#   Gợi ý:      python qk.py hint tutorials/MultiQubitGates/5
#   Lời giải:   python qk.py solution tutorials/MultiQubitGates/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 5: Multi-Controls
# Input: Control qubits, target qubit, and control bit pattern.
# Goal: Apply X gate to target if controls match the specified pattern.

from qiskit import QuantumCircuit
from typing import List

def multi_controls(qc: QuantumCircuit, controls: List[int], target: int, control_bits: List[bool]) -> QuantumCircuit:
    """
    Apply controlled X gate with multiple controls matching a pattern.

    Args:
        qc: Quantum circuit to modify
        controls: List of control qubit indices
        target: Target qubit index
        control_bits: Pattern that controls must match

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
