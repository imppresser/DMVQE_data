import numpy as np

Slice_list = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 961]

imgParams_predict = []
PredictedEnergy_mean_var = []
for Slice in Slice_list:
    imgParams_predict.append(np.load(f'Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs_predicted_slice{Slice}.npy'))
    PredictedEnergy_mean_var.append(np.loadtxt(f'Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs_predicted_EnergyMeanVar_slice{Slice}.txt'))

imgParams_predict_all = np.concatenate(imgParams_predict, axis=0)
print(np.shape(imgParams_predict_all))
PredictedEnergy_mean_var_all = np.concatenate(PredictedEnergy_mean_var, axis=0)
print(np.shape(PredictedEnergy_mean_var_all))

np.save('Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs_predicted.npy', imgParams_predict_all)
np.savetxt('Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs_predicted_EnergyMeanVar.txt', PredictedEnergy_mean_var_all)


