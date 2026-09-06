# ══════════════════════════════════════════════════════════════════════════════
# BÀI 043/350  ·  Bậc 3 · Nhiều qubit & vướng víu
# Superposition/1.3
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run Superposition/1.3
#   Gợi ý:      python qk.py hint Superposition/1.3
#   Lời giải:   python qk.py solution Superposition/1.3
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.3. Superposition of all basis vectors on two qubits
# Input: two qubits in |00⟩ state (stored in an array of length 2).
# Goal: create the following state on these qubits: (|00⟩ + |01⟩ + |10⟩ + |11⟩) / 2.

from qiskit import QuantumCircuit

def all_basis_vectors_two_qubits(qc: QuantumCircuit, qs: list) -> QuantumCircuit:
    """
    Create superposition of all basis vectors on two qubits.

    Args:
        qc: Quantum circuit to modify
        qs: List of two qubit indices

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
