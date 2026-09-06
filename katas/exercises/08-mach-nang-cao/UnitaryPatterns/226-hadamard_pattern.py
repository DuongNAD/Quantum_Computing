# ══════════════════════════════════════════════════════════════════════════════
# BÀI 226/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# UnitaryPatterns/5
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run UnitaryPatterns/5
#   Gợi ý:      python qk.py hint UnitaryPatterns/5
#   Lời giải:   python qk.py solution UnitaryPatterns/5
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 5. Hadamard pattern
# Input: A quantum circuit qc and a qubit index q.
# Goal: Apply the Hadamard gate to create superposition.
# The H gate transforms |0⟩ → (|0⟩+|1⟩)/√2 and |1⟩ → (|0⟩-|1⟩)/√2.

from qiskit import QuantumCircuit

def hadamard_pattern(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply Hadamard gate to qubit q.

    Args:
        qc: Quantum circuit to modify
        q: Index of qubit to apply H gate

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
