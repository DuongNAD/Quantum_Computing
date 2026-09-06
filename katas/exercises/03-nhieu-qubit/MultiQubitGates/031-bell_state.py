# ══════════════════════════════════════════════════════════════════════════════
# BÀI 031/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitGates/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitGates/2
#   Gợi ý:      python qk.py hint tutorials/MultiQubitGates/2
#   Lời giải:   python qk.py solution tutorials/MultiQubitGates/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 2: Bell State Preparation
# Input: Two qubits in state |00⟩.
# Goal: Prepare the qubits in the Bell state |φ⁺⟩ = (|00⟩ + |11⟩)/√2.

from qiskit import QuantumCircuit

def bell_state(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Prepare a Bell state |φ⁺⟩ = (|00⟩ + |11⟩)/√2 from |00⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
