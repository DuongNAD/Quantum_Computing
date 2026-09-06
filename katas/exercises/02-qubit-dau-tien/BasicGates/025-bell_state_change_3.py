# ══════════════════════════════════════════════════════════════════════════════
# BÀI 025/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.10
#   Gợi ý:      python qk.py hint BasicGates/1.10
#   Lời giải:   python qk.py solution BasicGates/1.10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.10. Bell state change - 3
# Input: Two entangled qubits in Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2).
# Goal: Change the two-qubit state to |Ψ⁻⟩ = (|01⟩ - |10⟩) / sqrt(2).

from qiskit import QuantumCircuit

def bell_state_change_3(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Change Bell state |φ⁺⟩ to |Ψ⁻⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
