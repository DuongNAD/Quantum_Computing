# ══════════════════════════════════════════════════════════════════════════════
# BÀI 099/350  ·  Bậc 5 · Giao thức lượng tử
# examples/QuantumRandomWalk
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/QuantumRandomWalk
#   Gợi ý:      python qk.py hint examples/QuantumRandomWalk
#   Lời giải:   python qk.py solution examples/QuantumRandomWalk
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Quantum Random Walk
# Goal: Implement a simple quantum random walk on a line using a coin and position qubit.
#       The coin determines the direction, position tracks location.

from qiskit import QuantumCircuit

def quantum_random_walk_step(qc: QuantumCircuit, coin: int, position: int) -> QuantumCircuit:
    """
    Perform one step of quantum random walk.

    Args:
        qc: Quantum circuit
        coin: Coin qubit (determines direction)
        position: Position qubit (tracks location)

    Returns:
        Modified quantum circuit after one walk step
    """
    # Your code here
    pass
