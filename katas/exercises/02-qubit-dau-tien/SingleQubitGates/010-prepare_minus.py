# ══════════════════════════════════════════════════════════════════════════════
# BÀI 010/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/4
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/4
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 4: Prepare |-⟩ state
# Input: A qubit in state |0⟩.
# Goal: Transform the qubit into state |-⟩ = (|0⟩ - |1⟩)/√2.

from qiskit import QuantumCircuit

def prepare_minus(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Prepare the |-⟩ state from |0⟩.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to prepare

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
