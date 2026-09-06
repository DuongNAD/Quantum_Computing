# ══════════════════════════════════════════════════════════════════════════════
# BÀI 005/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/Qubit/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Qubit/1
#   Gợi ý:      python qk.py hint tutorials/Qubit/1
#   Lời giải:   python qk.py solution tutorials/Qubit/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 1: Qubit State Preparation
# Goal: Prepare a qubit in a specific superposition state.
#       Start with |0⟩ and create the state (|0⟩ + |1⟩)/√2.

from qiskit import QuantumCircuit

def prepare_plus_state(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Prepare the |+⟩ = (|0⟩ + |1⟩)/√2 state.

    Args:
        qc: Quantum circuit to modify
        q: Qubit index

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
