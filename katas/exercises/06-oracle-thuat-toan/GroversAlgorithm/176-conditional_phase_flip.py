# ══════════════════════════════════════════════════════════════════════════════
# BÀI 176/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# GroversAlgorithm/2.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run GroversAlgorithm/2.2
#   Gợi ý:      python qk.py hint GroversAlgorithm/2.2
#   Lời giải:   python qk.py solution GroversAlgorithm/2.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.2. Conditional phase flip
# Input: A register of N qubits in an arbitrary state.
# Goal: Flip the sign of the state if it is NOT in the |0...0⟩ state.
# Example: If register is in |0...0⟩, leave unchanged. If in any other basis state, multiply phase by -1.
# Note: This implements the operator 2|0...0⟩⟨0...0| - I (inversion about average).

from qiskit import QuantumCircuit

def conditional_phase_flip(qc: QuantumCircuit, register: list[int]) -> QuantumCircuit:
    """
    Apply phase flip to all states except |0...0⟩.

    Args:
        qc: Quantum circuit to modify
        register: List of qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
