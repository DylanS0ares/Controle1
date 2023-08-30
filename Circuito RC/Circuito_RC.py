import numpy as np
import matplotlib.pyplot as plt
import control as co
import ipdb


#
# Circuito RC do fim da aula: condições iniciais nulas
#
print('Circuito RC: função de transferência com e sem condições iniciais nulas no capacitor:');
print('- Traçado do gráfico da dinâmica da função de transferência ao ligar a fonte');
tfinal = 0.01 # tempo de simulação
R = 100       # ohms
C = 20e-6     # farads
num1 = [0, 1]
den1 = [0, R]
G1   = co.tf(num1, den1)
num2 = [0, 1]
den2 = [C, 0]
G2   = co.tf(num2, den2)
G12  = co.series(G1,G2)
GMF  = co.feedback(G12,1,-1)
# Ligando a fonte (degrau unitário) e observando a dinâmica
t,y0 = co.step_response(GMF,tfinal)
#
# Circuito RC do fim da aula: condições iniciais NÃO NULAS!
# O capacitor tem uma carga prévia e tensão inicial Vcini
#
plt.show()
Vrange = np.linspace(0.1,0.9,9)
#print(Vrange)
for Vcini in Vrange: # tensão inicial do capacitor variando
    GMF1  = co.feedback(G12,1,-1)
    GMF2  = co.feedback(1,G12,-1)
    # Ligando a fonte e observando a dinâmica
    t1,y1 = co.step_response(GMF1,tfinal)
    # Incluindo a tensão inicial do capacitor e observando a dinâmica
    t2,y2 = co.forced_response(GMF2,t,Vcini)
    # Superposição: soma do efeito de ligar a fonte e incluir Vcini do capacitor
    y = y1 + y2 # superposição
    plt.plot(t1,y)
plt.plot(t,y0)
plt.axis([0,tfinal,0,1])
plt.grid()
