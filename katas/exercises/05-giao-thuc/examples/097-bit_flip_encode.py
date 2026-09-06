# ══════════════════════════════════════════════════════════════════════════════
# BÀI 097/350  ·  Bậc 5 · Giao thức lượng tử
# examples/QuantumErrorCorrectionBit
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/QuantumErrorCorrectionBit
#   Gợi ý:      python qk.py hint examples/QuantumErrorCorrectionBit
#   Lời giải:   python qk.py solution examples/QuantumErrorCorrectionBit
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Quantum Error Correction - Bit Flip
# Goal: Implement a simple 3-qubit bit flip error correction code.
#       Encode 1 logical qubit into 3 physical qubits to protect against single bit flip errors.

from qiskit import QuantumCircuit

def bit_flip_encode(qc: QuantumCircuit, logical: int, physical: list) -> QuantumCircuit:
    """
    Encode logical qubit into 3-qubit bit flip code.

    Args:
        qc: Quantum circuit
        logical: Logical qubit to encode
        physical: List of 3 physical qubit indices [p0, p1, p2]

    Returns:
        Modified quantum circuit after encoding
    """
    # Your code here
    pass
