from qiskit import *
from qiskit_aer import *

q = QuantumRegister(1)
c = ClassicalRegister(1)

qc = QuantumCircuit(q, c)
qc.measure(q, c)

be = Aer.get_backend('aer_simulator')
res = be.run(qc, shots=100).result()

print(res.get_counts(qc))
