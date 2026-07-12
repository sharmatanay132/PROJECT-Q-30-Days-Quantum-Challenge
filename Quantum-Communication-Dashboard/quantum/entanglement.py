from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
def create_entanglement():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc
def run_entanglement(qc):
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    return result.get_counts()
# Create the Bell state circuit
qc = create_entanglement()
# Execute it
counts = run_entanglement(qc)
# Display the measurement counts
print("Measurement Counts:", counts)
# Display the circuit
print(qc)
fig = qc.draw(output="mpl")
fig.savefig("outputs/entanglement.png")
plt.close(fig)