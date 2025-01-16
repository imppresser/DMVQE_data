import numpy as np

'''
计算标签参数和扩散模型生成的参数之间的余弦相似度
'''

def cosine_similarity_matrix(A, B):
    """
    计算两个矩阵之间的余弦相似度。
    参数：
    A -- 第一个矩阵 (numpy array)
    B -- 第二个矩阵 (numpy array)

    返回：
    cosine_similarity -- 余弦相似度 (float)
    """
    # 将矩阵展平为一维向量
    A_flat = A.flatten()
    B_flat = B.flatten()

    # 计算余弦相似度
    cosine_similarity = np.dot(A_flat, B_flat) / (np.linalg.norm(A_flat) * np.linalg.norm(B_flat))

    return cosine_similarity

# 加载标签参数矩阵
labelPrarms = np.load('Heisenberg/allData_outFor/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs.npy')

# 加载预测的参数矩阵
predictedParams = np.load('Heisenberg_predicted/Heisenberg_Qubits8_layer10_J1-4_h1-4_epoch501_test10_PQC_ParamImgs_predicted.npy')

# 循环计算余弦相似度
cosine_similarity_vec = []
for i in range(len(labelPrarms)):
    cosine_similarity_vec.append(cosine_similarity_matrix(np.squeeze(labelPrarms[i]), np.squeeze(predictedParams[i])))

cosine_similarity_save = np.array([np.arange(1, len(labelPrarms) + 1), cosine_similarity_vec]).T
np.savetxt('Heisenberg_J1-4_h1-4_labelVSpredicted_ParamImgs_cosineSimilarity_Value.txt', cosine_similarity_save)

# 统计余弦相似度数值的分布
dispersed_cosine_similarity_vec = np.linspace(0, 1, 1001)

num_vec = []
for i in range(len(dispersed_cosine_similarity_vec)-1):
    num = 0
    for value in cosine_similarity_vec:

        if dispersed_cosine_similarity_vec[i] <= value <  dispersed_cosine_similarity_vec[i+1]:
            num += 1

    num_vec.append(num)

distribution_vec = np.array(num_vec)/len(cosine_similarity_save)
distribution_save = np.array([dispersed_cosine_similarity_vec[1:], distribution_vec]).T

np.savetxt('Heisenberg_J1-4_h1-4_labelVSpredicted_ParamImgs_cosineSimilarity_Distribution.txt', distribution_save)



















