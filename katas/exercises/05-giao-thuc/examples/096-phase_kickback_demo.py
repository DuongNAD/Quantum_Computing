# ══════════════════════════════════════════════════════════════════════════════
# BÀI 096/350  ·  Bậc 5 · Giao thức lượng tử
# examples/PhaseKickbackDemo
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/PhaseKickbackDemo
#   Gợi ý:      python qk.py hint examples/PhaseKickbackDemo
#   Lời giải:   python qk.py solution examples/PhaseKickbackDemo
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Phase Kickback Demonstration
# Goal: Demonstrate phase kickback effect using a controlled operation and ancilla qubit.
#       Show how a phase applied to the target affects the control qubit when target is in |-⟩ state.

from qiskit import QuantumCircuit

def phase_kickback_demo(qc: QuantumCircuit, control: int, target: int) -> QuantumCircuit:
    """
    Demonstrate phase kickback effect.

    Args:
        qc: Quantum circuit
        control: Control qubit index (initially in |+⟩)
        target: Target qubit index (prepared in |-⟩)

    Returns:
        Modified quantum circuit showing phase kickback
    """
    # Your code here
    pass
