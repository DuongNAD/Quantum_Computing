# ══════════════════════════════════════════════════════════════════════════════
# BÀI 198/350  ·  Bậc 7 · QFT & Phase Estimation
# QFT/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QFT/2.2
#   Gợi ý:      python qk.py hint QFT/2.2
#   Lời giải:   python qk.py solution QFT/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Prepare a periodic state
# Inputs:
#      1) A register of n qubits in state |0...0⟩.
#      2) An integer frequency F (0 ≤ F ≤ 2ⁿ-1).
# Goal: Prepare a periodic state with frequency F on this register:
#       1 / sqrt(2ⁿ) Σₖ exp(2πi Fk/2ⁿ) |k⟩
# For example, for n = 2 and F = 1 the goal state is
#       1/2 (|0⟩ + i|1⟩ - |2⟩ - i|3⟩).
# Note: If you're using DumpMachine to debug your solution,
#       remember that this kata uses big endian encoding of states,
#       while DumpMachine uses little endian encoding.

from qiskit import QuantumCircuit

def prepare_periodic_state(qc: QuantumCircuit, register: list, F: int) -> QuantumCircuit:
    """
    Prepare a periodic state with given frequency using QFT.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices
        F: Frequency parameter

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
