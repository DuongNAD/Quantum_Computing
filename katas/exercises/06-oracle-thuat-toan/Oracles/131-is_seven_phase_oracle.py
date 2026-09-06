# ══════════════════════════════════════════════════════════════════════════════
# BÀI 131/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/Oracles/1.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Oracles/1.2
#   Gợi ý:      python qk.py hint tutorials/Oracles/1.2
#   Lời giải:   python qk.py solution tutorials/Oracles/1.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.2: IsSeven Phase Oracle
# Input: 3 qubits in superposition |x⟩ = Σ αᵢ|i⟩.
# Goal: Apply a -1 phase to the |111⟩ component (which represents 7).
#       Transform |x⟩ to Σ αᵢ(-1)^f(i)|i⟩ where f(i) = 1 if i = 7.

from qiskit import QuantumCircuit

def is_seven_phase_oracle(qc: QuantumCircuit, x: list) -> QuantumCircuit:
    """
    Phase oracle that applies -1 phase to |111⟩ state.

    Args:
        qc: Quantum circuit to modify
        x: List of qubit indices [x0, x1, x2]

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
