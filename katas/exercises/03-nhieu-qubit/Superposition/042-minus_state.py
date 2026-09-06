# ══════════════════════════════════════════════════════════════════════════════
# BÀI 042/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.2
#   Gợi ý:      python qk.py hint Superposition/1.2
#   Lời giải:   python qk.py solution Superposition/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2. Minus state
# Input: a qubit in the |0⟩ state.
# Goal: prepare a |-⟩ state on this qubit (|-⟩ = (|0⟩ - |1⟩) / sqrt(2)).

from qiskit import QuantumCircuit

def minus_state(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Prepare the |-⟩ state on qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to prepare in |-⟩ state

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
