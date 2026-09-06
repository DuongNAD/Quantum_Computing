# ══════════════════════════════════════════════════════════════════════════════
# BÀI 129/350  ·  Bậc 5 · Giao thức lượng tử
# KeyDistribution_BB84/3.2
# ══════════════════════════════════════════════════════════════════════════════
#
#   Chấm bài:   python qk.py run KeyDistribution_BB84/3.2
#   Gợi ý:      python qk.py hint KeyDistribution_BB84/3.2
#   Lời giải:   python qk.py solution KeyDistribution_BB84/3.2
#
#   Viết code vào chỗ `# Your code here`, xoá dòng `pass`, rồi lưu file.
# ══════════════════════════════════════════════════════════════════════════════

# Task 3.2. Catch the eavesdropper - BB84 Protocol with Eavesdropper
# Add an eavesdropper into the BB84 protocol from task 2.6.
# Now Alice and Bob should be able to detect Eve's presence through increased
# error rates, and they should discard compromised key bits.
#
# This demonstrates how quantum mechanics provides security - any eavesdropping
# attempt introduces detectable disturbances.

from typing import Tuple
import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def bb84_protocol_with_eavesdropper(n_qubits: int, eve_probability: float = 1.0) -> Tuple[bool, list, list, float]:
    """
    Implement BB84 protocol with an eavesdropper.

    Args:
        n_qubits: Number of qubits to use in the protocol
        eve_probability: Probability that Eve eavesdrops on each qubit (0.0 to 1.0)

    Returns:
        Tuple of (success, alice_key, bob_key, error_rate) where:
        - success: True if keys are secure (error rate acceptable)
        - alice_key: Alice's version of the shared key
        - bob_key: Bob's version of the shared key
        - error_rate: Percentage of bit errors detected
    """
    # Your code here
    pass
