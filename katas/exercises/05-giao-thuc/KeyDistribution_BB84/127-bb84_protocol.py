# ══════════════════════════════════════════════════════════════════════════════
# BÀI 127/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/2.6
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/2.6
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/2.6
#   Lời giải:   python qk.py solution KeyDistribution_BB84/2.6
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 2.6. Putting it all together - BB84 Protocol
# Goal: Implement the entire BB84 protocol using tasks 2.1 - 2.5
#       and following the implementation steps.
#
# This demonstrates the complete BB84 quantum key distribution protocol
# without eavesdropping. The generated keys should always match since
# there's no interference.

from typing import Tuple
import random
from qiskit import QuantumCircuit

def bb84_protocol(n_qubits: int) -> Tuple[bool, list, list]:
    """
    Implement the complete BB84 quantum key distribution protocol.

    Args:
        n_qubits: Number of qubits to use in the protocol

    Returns:
        Tuple of (success, alice_key, bob_key) where:
        - success: True if keys match within acceptable error rate
        - alice_key: Alice's version of the shared key
        - bob_key: Bob's version of the shared key
    """
    # Your code here
    pass
