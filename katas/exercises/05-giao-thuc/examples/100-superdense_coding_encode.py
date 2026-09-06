# ══════════════════════════════════════════════════════════════════════════════
# BÀI 100/350  ·  Bậc 5 · Giao thức lượng tử
# examples/QuantumSuperdenseCoding
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run examples/QuantumSuperdenseCoding
#   Gợi ý:      python qk.py hint examples/QuantumSuperdenseCoding
#   Lời giải:   python qk.py solution examples/QuantumSuperdenseCoding
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Quantum Superdense Coding
# Goal: Implement superdense coding to send 2 classical bits using 1 qubit and prior entanglement.
#       Alice encodes 2 classical bits into her qubit and sends it to Bob.
from qiskit import QuantumCircuit

def superdense_coding_encode(qc: QuantumCircuit, alice_qubit: int, message: int) -> QuantumCircuit:
    """
    Encode 2-bit message using superdense coding.


    Args:
        qc: Quantum circuit with pre-shared entanglement
        alice_qubit: Alice's qubit index
        message: 2-bit message (0, 1, 2, or 3)

    Returns:
        Modified quantum circuit after encoding
    """
    # Your code here
    pass
