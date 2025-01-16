import numpy as np
import matplotlib.pyplot as plt


allLayer_vec = [10,11,12,13,14,15,16,17,18,19,20]
TLlayer_vec = [0,1,2,3,4,5,6,7,8,9,10]

RPVQE = []
TL_DPVQE = []

RPVQE_var = []
TL_DPVQE_var = []

for allLayer, TLlayer in zip(allLayer_vec, TLlayer_vec):
    RPVQE.append(np.loadtxt(f'Hubbard_Qubits8_allLayer{allLayer}_J3_h3_randomParamLoss_test30_epochs1001.txt')[-1])
    TL_DPVQE.append(np.loadtxt(f'Hubbard_Qubits8_origLayer10_TLlayer{TLlayer}_J3_h3_predictedLoss_test30_epochs1001.txt')[-1])

    RPVQE_var.append(np.loadtxt(f'Hubbard_Qubits8_allLayer{allLayer}_J3_h3_randomParamVar_test30_epochs1001.txt')[-1])
    TL_DPVQE_var.append(np.loadtxt(f'Hubbard_Qubits8_origLayer10_TLlayer{TLlayer}_J3_h3_predictedVar_test30_epochs1001.txt')[-1])

plt.plot(RPVQE, label = 'RPVQE')
plt.plot(TL_DPVQE, label = 'TL_DPVQE')
plt.legend()
plt.show()

np.savetxt(f'RPVQE_layer10-20_J3_h3_mean_var_energy_test30.txt', np.array([RPVQE, RPVQE_var]).T)
np.savetxt(f'TL_DMVQE_TLlayer0-10_J3_h3_mean_var_energy_test30.txt', np.array([TL_DPVQE, TL_DPVQE_var]).T)










