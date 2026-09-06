# ══════════════════════════════════════════════════════════════════════════════
# BÀI 028/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# tutorials/MultiQubitSystems/3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/MultiQubitSystems/3
#   Gợi ý:      python qk.py hint tutorials/MultiQubitSystems/3
#   Lời giải:   python qk.py solution tutorials/MultiQubitSystems/3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# PrepareState3: Prepare |+⟩ ⊗ |-⟩ state
# Input: Two qubits in state |00⟩.
# Goal: Transform the qubits to state |+⟩ ⊗ |-⟩ = (|0⟩ + |1⟩)/√2 ⊗ (|0⟩ - |1⟩)/√2.

from qiskit import QuantumCircuit

def prepare_state3(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Prepare the state |+⟩ ⊗ |-⟩ from initial state |00⟩.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices [q0, q1]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
