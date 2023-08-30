import numpy as np
import matplotlib.pyplot as plt
import control as co
import ipdb



num1 = [10]
den1 = [1, 2, 10]
num2 = [5]
den2 = [1, 5]
sys1 = co.tf(num1, den1)
sys2 = co.tf(num2, den2)
print('Sistema 1:')
print(sys1)
print('Sistema 2:')
print(sys2)
sys_series = co.series(sys1, sys2)
print('Sistemas em cascata/série:')
print(sys_series)
sys_parallel = co.parallel(sys1, sys2)
print('Sistemas em paralelo:')
print(sys_parallel)
sys_feedback = co.feedback(sys1, sys2)
print('Sistemas com realimentação:')
print(sys_feedback)
