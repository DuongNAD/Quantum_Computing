# ══════════════════════════════════════════════════════════════════════════════
# BÀI 245/350  ·  Bậc 8 · Mạch nâng cao & ứng dụng
# DistinguishUnitaries/1.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run DistinguishUnitaries/1.6
#   Gợi ý:      python qk.py hint DistinguishUnitaries/1.6
#   Lời giải:   python qk.py solution DistinguishUnitaries/1.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 1.6. Rz or R1 (arbitrary angle)?
# Input: A gate class (the Qiskit class itself, e.g. RZGate or PhaseGate) that, when
#        instantiated with a rotation angle, produces either an Rz gate or an R1 (phase) gate.
#        Also provided: the `angle` the caller originally had in mind. You are NOT required
#        to query the gate at this angle — you may instantiate `gate_class(theta)` with any
#        angle `theta` of your choosing (typically theta = 2*pi, which makes Rz = I up to a
#        global phase while R1(2*pi) is a nontrivial identity, enabling phase-kickback
#        discrimination).
# Output: 0 if the given gate class is Rz, 1 if it is R1.
# You are allowed to call `gate_class` and apply the resulting gate exactly once.

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import numpy as np

def distinguish_rz_from_r1(gate_class, angle: float) -> int:
    """
    Distinguish between the Rz and R1 (Phase) gate classes via controlled-phase kickback.

    Args:
        gate_class: A Qiskit gate class (e.g. RZGate or PhaseGate) that takes an angle.
        angle: The rotation angle originally specified by the caller. The implementation is
               free to ignore this value and query `gate_class(theta)` at any chosen `theta`.

    Returns:
        0 if gate_class is Rz, 1 if gate_class is R1.
    """
    # Your code here
    pass

