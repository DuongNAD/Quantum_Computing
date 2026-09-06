from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

sampler = SamplerV2()
result = sampler.run([qc],shots=4096).result()
print(result[0].data.meas.get_counts())
print(qc.draw("text"))