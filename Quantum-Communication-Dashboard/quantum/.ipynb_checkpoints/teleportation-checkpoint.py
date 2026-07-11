{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "56ed6d88-5b8a-4df1-bfe7-906c6a2d8a65",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Measurement Counts: {'101': 132, '001': 134, '110': 122, '100': 144, '111': 121, '011': 130, '000': 113, '010': 128}\n",
      "     ┌───┐          ┌───┐┌─┐\n",
      "q_0: ┤ H ├───────■──┤ H ├┤M├\n",
      "     ├───┤     ┌─┴─┐└┬─┬┘└╥┘\n",
      "q_1: ┤ H ├──■──┤ X ├─┤M├──╫─\n",
      "     └───┘┌─┴─┐└┬─┬┘ └╥┘  ║ \n",
      "q_2: ─────┤ X ├─┤M├───╫───╫─\n",
      "          └───┘ └╥┘   ║   ║ \n",
      "c: 3/════════════╩════╩═══╩═\n",
      "                 2    1   0 \n"
     ]
    }
   ],
   "source": [
    "from qiskit import QuantumCircuit\n",
    "from qiskit_aer import AerSimulator\n",
    "def create_teleportation():\n",
    "    qc = QuantumCircuit(3,3)\n",
    "    qc.h(0)\n",
    "    qc.h(1)\n",
    "    qc.cx(1,2)\n",
    "    qc.cx(0,1)\n",
    "    qc.h(0)\n",
    "    qc.measure([0,1,2],[0,1,2])\n",
    "    return qc\n",
    "def run_teleportation(qc):\n",
    "    simulator = AerSimulator()\n",
    "    result = simulator.run(qc, shots=1024).result()\n",
    "    return result.get_counts()\n",
    "qc = create_teleportation()\n",
    "\n",
    "counts = run_teleportation(qc)\n",
    "\n",
    "print(\"Measurement Counts:\", counts)\n",
    "\n",
    "print(qc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "543f4dae-db27-4b52-abcb-d57930d2e392",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
