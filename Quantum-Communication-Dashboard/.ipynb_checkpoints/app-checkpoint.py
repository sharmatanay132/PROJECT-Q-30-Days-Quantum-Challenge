{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a655ce0d-25fd-42db-8122-8b1d325893ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''from quantum.bell_states import create_bell, run_circuit\n",
    "from quantum.entanglement import create_entanglement, run_entanglement\n",
    "from quantum.teleportation import create_teleportation, run_teleportation'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1490f6c0-0985-4f27-ae7d-bd1c4fe144fa",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''#Adding route to Bell State\n",
    "@app.route(\"/bell\")\n",
    "def bell():\n",
    "    qc = create_bell()\n",
    "    counts = run_circuit(qc)\n",
    "    return render_template(\"bell.html\", counts=counts)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f841f9ff-2873-428f-8593-e8d98526ded2",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''#Adding route to entanglement\n",
    "@app.route(\"/entanglement\")\n",
    "def entanglement():\n",
    "    qc = create_entanglement()\n",
    "    counts = run_entanglement(qc)\n",
    "    return render_template(\"entanglement.html\", counts=counts)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d7e3cd7-2585-442d-88ca-251f2a6bdc67",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''#Adding route to teleportation\n",
    "@app.route(\"/teleportation\")\n",
    "def teleportation():\n",
    "    qc = create_teleportation()\n",
    "    counts = run_teleportation(qc)\n",
    "    return render_template(\"teleportation.html\", counts=counts)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8a213af-024d-45ba-96fe-d12c5aaf2d44",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''from flask import Flask, render_template\n",
    "app = Flask(__name__)\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "if __name__== \"__main__\":\n",
    "    #app.run(debug=True,use_reloader=False)\n",
    "    app.run(host=\"127.0.0.1\", port=5001, debug=False, use_reloader=False)'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c71bd62-6f85-4c76-a618-1ba34511f0c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "print(os.listdir(\"quantum\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43a62622-e8bb-424a-8c70-8da37c91eaa1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "import import_ipynb\n",
    "from quantum.bell_states import create_bell, run_circuit\n",
    "from quantum.entanglement import create_entanglement, run_entanglement\n",
    "from quantum.teleportation import create_teleportation, run_teleportation\n",
    "\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/bell\")\n",
    "def bell():\n",
    "    qc = create_bell()\n",
    "    counts = run_circuit(qc)\n",
    "    return render_template(\"bell.html\", counts=counts)\n",
    "\n",
    "@app.route(\"/entanglement\")\n",
    "def entanglement():\n",
    "    qc = create_entanglement()\n",
    "    counts = run_entanglement(qc)\n",
    "    return render_template(\"entanglement.html\", counts=counts)\n",
    "\n",
    "@app.route(\"/teleportation\")\n",
    "def teleportation():\n",
    "    qc = create_teleportation()\n",
    "    counts = run_teleportation(qc)\n",
    "    return render_template(\"teleportation.html\", counts=counts)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(host=\"127.0.0.1\", port=5002, debug=False, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ffc002d-c918-4c23-aa88-76558ad4db98",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ded16470-4e96-4313-aa2d-102b4b855b60",
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
