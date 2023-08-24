import numpy as np
import matplotlib.pyplot as plt
import control as co


from scipy import signal
num = [2,5,3,6]
den = [1,6,11,6]
r,p,k = signal.residue(num,den)
print('Resíduos:',r)
print('Polos: ',p)
print('Termo direto:',k)

