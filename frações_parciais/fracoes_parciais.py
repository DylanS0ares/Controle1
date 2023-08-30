import numpy as np
import matplotlib.pyplot as plt
import control as co


from scipy import signal
num = [2,5,3,6]
den = [1,6,11,6]
r,p,k = signal.residue(num,den)
for i in range(len(r)):
    print('Resíduos:{:.1f}'.format(r[i]))
for i in range(len(p)): 
    print('Polos:{:.1f} '.format(p[i]))
for i in range(len(k)):
    print('Termo direto: {:.1f}'.format(k[i]))

