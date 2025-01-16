import numpy as np
import pickle

J_list = np.arange(1, 4.1, 0.1)

Heisenberg_HStr_CLIP = []
Heisenberg_HStr_qml = []
Heisenberg_LabelEnergy = []
Heisenberg_PQC_ParamImgs = []
Heisenberg_RealEnergy = []
for J in J_list:
    with open(f'Heisenberg_Qubits8_layer10_J{np.round(J, 2)}_h1-4_epoch501_test10_HStr_CLIP.pkl', 'rb') as file:
        Hstr_CLIP = pickle.load(file)
    with open(f'Heisenberg_Qubits8_layer10_J{np.round(J, 2)}_h1-4_epoch501_test10_HStr_qml.pkl', 'rb') as file:
        Hstr_qml = pickle.load(file)
    PQC_ParamImgs = np.load(f'Heisenberg_Qubits8_layer10_J{np.round(J, 2)}_h1-4_epoch501_test10_PQC_ParamImgs.npy')
    RealEnergy = np.loadtxt(f'Heisenberg_Qubits8_layer10_J{np.round(J, 2)}_h1-4_epoch501_test10_RealEnergy.txt')
    LabelEnergy = np.loadtxt(f'Heisenberg_Qubits8_layer10_J{np.round(J, 2)}_h1-4_epoch501_test10_LabelEnergy.txt')

    Heisenberg_HStr_CLIP += Hstr_CLIP
    Heisenberg_HStr_qml += Hstr_qml
    Heisenberg_PQC_ParamImgs.append(PQC_ParamImgs)
    Heisenberg_RealEnergy.append(RealEnergy)
    Heisenberg_LabelEnergy.append(LabelEnergy)


Heisenberg_PQC_ParamImgs_save = np.concatenate(Heisenberg_PQC_ParamImgs, axis=0)
Heisenberg_RealEnergy_save = np.concatenate(Heisenberg_RealEnergy, axis=0)
Heisenberg_LabelEnergy_save = np.concatenate(Heisenberg_LabelEnergy, axis=0)

# 存储数据
with open('allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_HStr_CLIP.pkl', 'wb') as file:
    pickle.dump(Heisenberg_HStr_CLIP, file)
with open('allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_HStr_qml.pkl', 'wb') as file:
    pickle.dump(Heisenberg_HStr_qml, file)
np.save('allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs.npy', Heisenberg_PQC_ParamImgs_save)
np.savetxt('allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_RealEnergy.txt', Heisenberg_RealEnergy_save)
np.savetxt('allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_LabelEnergy.txt', Heisenberg_LabelEnergy_save)












