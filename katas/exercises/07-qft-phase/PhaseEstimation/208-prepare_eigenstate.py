# ══════════════════════════════════════════════════════════════════════════════
# BÀI 208/350  ·  Bậc 7 · QFT & Phase Estimation
# PhaseEstimation/4
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run PhaseEstimation/4
#   Gợi ý:      python qk.py hint PhaseEstimation/4
#   Lời giải:   python qk.py solution PhaseEstimation/4
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 4. Prepare eigenstate
# Input: A quantum circuit and target qubit.
# Goal: Prepare an eigenstate of the phase gate U = P(theta).
# For P(theta), |1> is an eigenstate with eigenvalue e^(i*theta).

from qiskit import QuantumCircuit

def prepare_eigenstate(qc: QuantumCircuit, target: int) -> QuantumCircuit:
    """
    Prepare eigenstate |1> of the phase gate.

    Args:
        qc: Quantum circuit to modify
        target: Target qubit index

    Returns:
        Modified quantum circuit with eigenstate prepared
    """
    # Your code here
    pass
