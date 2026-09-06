# ══════════════════════════════════════════════════════════════════════════════
# BÀI 347/350  ·  Bậc 9 · Nghịch lý lượng tử & Sửa lỗi
# QEC_BitFlipCode/9
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run QEC_BitFlipCode/9
#   Gợi ý:      python qk.py hint QEC_BitFlipCode/9
#   Lời giải:   python qk.py solution QEC_BitFlipCode/9
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 9. Detect single bit flip error
# Input: A quantum circuit with encoded state that may have a single bit flip error.
# Goal: Detect if an error occurred (without identifying which qubit).
# Returns True if an error is detected.

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator

def detect_error(qc: QuantumCircuit, data: list, ancilla: int) -> bool:
    """
    Detect if a bit flip error occurred.

    Args:
        qc: Quantum circuit with possibly corrupted encoded state
        data: List of 3 data qubit indices
        ancilla: Ancilla qubit index for detection

    Returns:
        True if error detected, False otherwise
    """
    # Your code here
    pass
