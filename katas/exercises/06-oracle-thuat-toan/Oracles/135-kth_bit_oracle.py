# ══════════════════════════════════════════════════════════════════════════════
# BÀI 135/350  ·  Bậc 6 · Oracle & thuật toán kinh điển
# tutorials/Oracles/3.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run tutorials/Oracles/3.2
#   Gợi ý:      python qk.py hint tutorials/Oracles/3.2
#   Lời giải:   python qk.py solution tutorials/Oracles/3.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.2: Kth Bit Oracle (Phase Oracle)
# Input: Query qubits and bit index k.
# Goal: Apply -1 phase if the k-th qubit (0-indexed) is in state |1⟩.

from qiskit import QuantumCircuit

def kth_bit_oracle(qc: QuantumCircuit, x: list, k: int) -> QuantumCircuit:
    """
    Phase oracle that applies -1 phase if k-th qubit is |1⟩.

    Args:
        qc: Quantum circuit to modify
        x: List of query qubit indices
        k: Index of bit to check (0-indexed)

    Returns:
        Modified quantum circuit
    """
    # Your code here
    pass
