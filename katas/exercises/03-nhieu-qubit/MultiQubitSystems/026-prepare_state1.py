# ══════════════════════════════════════════════════════════════════════════════
# BÀI 026/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitSystems/1
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitSystems/1
#   Gợi ý:      python qk.py hint tutorials/MultiQubitSystems/1
#   Lời giải:   python qk.py solution tutorials/MultiQubitSystems/1
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# PrepareState1: Prepare |11⟩ state
# Input: Two qubits in state |00⟩.
# Goal: Transform the qubits to state |11⟩.

from qiskit import QuantumCircuit

def prepare_state1(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Prepare the two-qubit state |11⟩ from initial state |00⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
