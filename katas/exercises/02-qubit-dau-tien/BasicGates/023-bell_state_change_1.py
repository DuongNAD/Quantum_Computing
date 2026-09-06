# ══════════════════════════════════════════════════════════════════════════════
# BÀI 023/350  ·  Bậc 2 · Qubit đầu tiên
# BasicGates/1.8
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run BasicGates/1.8
#   Gợi ý:      python qk.py hint BasicGates/1.8
#   Lời giải:   python qk.py solution BasicGates/1.8
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.8. Bell state change - 1
# Input: Two entangled qubits in Bell state |φ⁺⟩ = (|00⟩ + |11⟩) / sqrt(2).
# Goal: Change the two-qubit state to |φ⁻⟩ = (|00⟩ - |11⟩) / sqrt(2).

from qiskit import QuantumCircuit

def bell_state_change_1(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Change Bell state |φ⁺⟩ to |φ⁻⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
