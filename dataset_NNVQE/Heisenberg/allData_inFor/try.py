import numpy as np

energy = np.loadtxt('Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch301_test10_RealEnergy.txt')

print(np.min(energy))
print(np.max(energy))