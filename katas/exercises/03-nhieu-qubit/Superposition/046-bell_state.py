# ══════════════════════════════════════════════════════════════════════════════
# BÀI 046/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.6
#   Gợi ý:      python qk.py hint Superposition/1.6
#   Lời giải:   python qk.py solution Superposition/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Bell state
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: create a Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2) on these qubits.

from qiskit import QuantumCircuit

def bell_state(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Create Bell state |φ⁺⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
