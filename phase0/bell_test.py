from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def lay_statevector(qc):
    # Dùng AerSimulator để tính Statevector (tương thích mọi phiên bản NumPy/Qiskit)
    qc_clone = qc.copy()
    qc_clone.save_statevector()
    sim = AerSimulator(method="statevector")
    res = sim.run(qc_clone).result()
    vec = res.get_statevector().data
    return [round(float(val.real), 3) for val in vec]

def tao_bell_phi_cong(qc):
    # |Φ⁺⟩ = (|00⟩ + |11⟩) / √2
    qc.h(0)
    qc.cx(0, 1)

def tao_bell_phi_tru(qc):
    # |Φ⁻⟩ = (|00⟩ - |11⟩) / √2
    qc.h(0)
    qc.z(0)
    qc.cx(0, 1)

def tao_bell_psi_cong(qc):
    # |Ψ⁺⟩ = (|01⟩ + |10⟩) / √2
    qc.h(0)
    qc.x(1)
    qc.cx(0, 1)

def tao_bell_psi_tru(qc):
    # |Ψ⁻⟩ = (-|01⟩ + |10⟩) / √2
    qc.h(0)
    qc.x(1)
    qc.z(0)
    qc.cx(0, 1)

# Danh sách 4 trạng thái
danh_sach_bell = [
    ("1. Trạng thái |Φ⁺⟩ (Phi cộng)", tao_bell_phi_cong),
    ("2. Trạng thái |Φ⁻⟩ (Phi trừ) ", tao_bell_phi_tru),
    ("3. Trạng thái |Ψ⁺⟩ (Psi cộng)", tao_bell_psi_cong),
    ("4. Trạng thái |Ψ⁻⟩ (Psi trừ) ", tao_bell_psi_tru),
]

print("=" * 60)
print("     KIỂM TRA VECTOR TRẠNG THÁI 4 TRẠNG THÁI BELL")
print("=" * 60)

for ten, fn in danh_sach_bell:
    qc = QuantumCircuit(2)
    fn(qc)
    vec = lay_statevector(qc)
    print(f"\n{ten}")
    print(f"   Statevector [00, 01, 10, 11] = {vec}")
    print("   Mạch:")
    print("   " + "\n   ".join(qc.draw("text").__str__().splitlines()))