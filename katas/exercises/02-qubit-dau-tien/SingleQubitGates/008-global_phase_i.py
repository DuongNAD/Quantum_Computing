# ══════════════════════════════════════════════════════════════════════════════
# BÀI 008/350  ·  Bậc 2 · Qubit đầu tiên
# tutorials/SingleQubitGates/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/SingleQubitGates/2
#   Gợi ý:      python qk.py hint tutorials/SingleQubitGates/2
#   Lời giải:   python qk.py solution tutorials/SingleQubitGates/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 2: Applying a global phase i
# Input: A qubit in an arbitrary state |Ψ⟩ = α|0⟩ + β|1⟩.
# Goal: Use several Pauli gates to change the qubit state to i|Ψ⟩ = iα|0⟩ + iβ|1⟩.

from qiskit import QuantumCircuit

def global_phase_i(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply a global phase of i to the qubit using Pauli gates.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply global phase to

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
