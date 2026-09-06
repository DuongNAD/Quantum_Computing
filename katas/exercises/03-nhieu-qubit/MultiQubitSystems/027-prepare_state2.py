# ══════════════════════════════════════════════════════════════════════════════
# BÀI 027/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitSystems/2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitSystems/2
#   Gợi ý:      python qk.py hint tutorials/MultiQubitSystems/2
#   Lời giải:   python qk.py solution tutorials/MultiQubitSystems/2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# PrepareState2: Prepare |0⟩ ⊗ |-⟩ state
# Input: Two qubits in state |00⟩.
# Goal: Transform the qubits to state |0⟩ ⊗ |-⟩ = |0⟩ ⊗ (|0⟩ - |1⟩)/√2.

from qiskit import QuantumCircuit

def prepare_state2(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Prepare the state |0⟩ ⊗ |-⟩ from initial state |00⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
