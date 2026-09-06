# ══════════════════════════════════════════════════════════════════════════════
# BÀI 009/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/3
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/3
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 3: Sign flip on |0⟩ state
# Input: A qubit in an arbitrary state |Ψ⟩ = α|0⟩ + β|1⟩.
# Goal: Use several Pauli gates to change the qubit state to -α|0⟩ + β|1⟩.
#       This applies a -1 phase to the |0⟩ component while leaving |1⟩ unchanged.

from qiskit import QuantumCircuit

def sign_flip_on_zero(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply a -1 phase to |0⟩ component using Pauli gates.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply transformation to

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
