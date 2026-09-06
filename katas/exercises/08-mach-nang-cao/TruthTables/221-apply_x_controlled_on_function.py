# ══════════════════════════════════════════════════════════════════════════════
# BÀI 221/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# TruthTables/10
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run TruthTables/10
#   Gợi ý:      python qk.py hint TruthTables/10
#   Lời giải:   python qk.py solution TruthTables/10
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 10. Apply truth table as a quantum operation
# Goal: Apply the X operation on the target qubit, if and only if
#       the classical state of the controls is a minterm of the truth table.

from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate

class TruthTable:
    def __init__(self, bits: int, num_vars: int):
        self.bits = bits
        self.num_vars = num_vars

    def __eq__(self, other):
        return self.bits == other.bits and self.num_vars == other.num_vars

def all_minterms(tt: TruthTable) -> list[int]:
    """Helper: Find all minterms (true assignments) in truth table."""
    minterms = []
    num_assignments = 1 << tt.num_vars
    for assignment in range(num_assignments):
        if (tt.bits >> assignment) & 1:
            minterms.append(assignment)
    return minterms

def apply_x_controlled_on_function(qc: QuantumCircuit, tt: TruthTable, controls: list[int], target: int) -> QuantumCircuit:
    """
    Apply X gate on target qubit controlled by truth table function on control qubits.

    Args:
        qc: Quantum circuit to modify
        tt: Truth table defining the control function
        controls: List of control qubit indices
        target: Target qubit index

    Returns:
        Modified quantum circuit
    """
    assert len(controls) == tt.num_vars, "Number of control qubits must match truth table variables"

    # Your code here
    pass
