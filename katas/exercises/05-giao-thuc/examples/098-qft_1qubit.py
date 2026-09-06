# ══════════════════════════════════════════════════════════════════════════════
# BÀI 098/350  ·  Bậc 5 · Giao thức lượng tử
# examples/QuantumFourierTransform1Qubit
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/QuantumFourierTransform1Qubit
#   Gợi ý:      python qk.py hint examples/QuantumFourierTransform1Qubit
#   Lời giải:   python qk.py solution examples/QuantumFourierTransform1Qubit
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# 1-Qubit Quantum Fourier Transform
# Goal: Implement the quantum Fourier transform for a single qubit.
#       For 1 qubit, QFT is just a Hadamard gate.

from qiskit import QuantumCircuit

def qft_1qubit(qc: QuantumCircuit, q: int) -> QuantumCircuit:
    """
    Apply 1-qubit Quantum Fourier Transform.

    Args:
        qc: Quantum circuit
        q: Qubit index

    Returns:
        Modified quantum circuit after QFT
    """
    # Your code here
    pass
