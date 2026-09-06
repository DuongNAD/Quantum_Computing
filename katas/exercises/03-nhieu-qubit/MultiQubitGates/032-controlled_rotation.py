# ══════════════════════════════════════════════════════════════════════════════
# BÀI 032/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitGates/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitGates/3
#   Gợi ý:      python qk.py hint tutorials/MultiQubitGates/3
#   Lời giải:   python qk.py solution tutorials/MultiQubitGates/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Exercise 3: Controlled Rotation
# Input: Two qubits in an arbitrary state, and a rotation angle theta.
# Goal: Apply a controlled rotation Rx(theta) to the second qubit, controlled by the first qubit.
#       If the control qubit is |0⟩, do nothing to the target.
#       If the control qubit is |1⟩, apply Rx(theta) to the target qubit.

from qiskit import QuantumCircuit

def controlled_rotation(qc: QuantumCircuit, qs: list, theta: float) -> QuantumCircuit:
    """
    Apply controlled rotation Rx(theta) with first qubit as control.

    Args:
        qc: Quantum circuit to modify
        qs: List of qubit indices [control, target]
        theta: Rotation angle in radians

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
