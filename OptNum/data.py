import numpy as np
import matplotlib.pyplot as plt


Slice_list = [20,30,40,50,60,70,80,90,100,110,121]


RPVQE = []
DMVQE = []

for Slice in Slice_list:
    RPVQE.append(np.loadtxt(f'Ising_Qubits8_layer10_J2-3_h2-3_OrigVQE_MRE0.005_OptNum_transferLearning_slice{Slice}.txt'))
    DMVQE.append(np.loadtxt(f'Ising_Qubits8_layer10_J2-3_h2-3_DMVQE_MRE0.005_OptNum_transferLearning_slice{Slice}.txt'))

RPVQE_all = np.concatenate(RPVQE, axis=0).T
DMVQE_all = np.concatenate(DMVQE, axis=0).T

plt.plot(RPVQE_all, label = 'RPVQE')
plt.plot(DMVQE_all, label = 'DMVQE')
plt.legend()
plt.show()

np.savetxt(f'RPVQE_layer10_J2-3_h2-3_MRE0.005_OptNum.txt', RPVQE_all)
np.savetxt(f'DMVQE_layer10_J2-3_h2-3_MRE0.005_OptNum.txt', DMVQE_all)










