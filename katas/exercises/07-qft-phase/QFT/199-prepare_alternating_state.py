# ══════════════════════════════════════════════════════════════════════════════
# BÀI 199/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.3
#   Gợi ý:      python qk.py hint QFT/2.3
#   Lời giải:   python qk.py solution QFT/2.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.3. Prepare a periodic state with alternating 1 and -1 amplitudes
# Input: A register of n qubits in state |0...0⟩.
# Goal: Prepare a periodic state with alternating 1 and -1 amplitudes of basis states:
#       1 / sqrt(2ⁿ) (|0⟩ - |1⟩ + |2⟩ - |3⟩ + ... - |2ⁿ-1⟩).
# For example, for n = 2 the goal state is
#       1/2 (|0⟩ - |1⟩ + |2⟩ - |3⟩).

from qiskit import QuantumCircuit

def prepare_alternating_state(qc: QuantumCircuit, register: list) -> QuantumCircuit:
    """
    Prepare alternating amplitude state using QFT.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
