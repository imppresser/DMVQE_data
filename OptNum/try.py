import numpy as np

optnum = np.loadtxt('RPVQE_layer10_J2-3_h2-3_MRE0.005_OptNum.txt')

n=0
for num in optnum:
    if num == 2000:
        n += 1

print(n)