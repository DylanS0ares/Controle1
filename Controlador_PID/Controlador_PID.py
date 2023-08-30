import numpy as np
import matplotlib.pyplot as plt
import control as co
import ipdb

# Definindo a funcao de transferencia
numG = [0, 1]
denG = [1, 2]
# G = 1/(s+2)
G = co.tf(numG, denG)
#---------------------------------------------------------
# Controle proporcional  (P)
# Criando um vetor T (tempo) para simular : de 0s até 0.5s
T  = np.linspace(0,0.5,51)
# Criando um vetor Krange para variar o ganho proporcional
Krange = np.linspace(40,100,7)
plt.show()
for Kp in Krange:
  G_MF = co.feedback(Kp*G,1)
  t,y  = co.step_response(G_MF,T)
  plt.plot(t,y)
plt.axis([0,0.2,0,1])
plt.grid()
# Debug irá parar na linha se retirar o comentário
# ipdb.set_trace()
#---------------------------------------------------------
# Controle integral  (I)
# Criando um vetor T (tempo) para simular : de 0s até 10s
T  = np.linspace(0,10,1001)
# Criando um vetor Krange para variar o ganho integral
Krange = np.linspace(1,10,10)
plt.show()
for Ki in Krange:
  numC = [0, Ki]
  denC = [1, 0]
  Gi   = co.tf(numC, denC)
  G_MF = co.feedback(Gi*G,1)
  t,y  = co.step_response(G_MF,T)
  plt.plot(t,y)
plt.axis([0,10,0,1.4])
plt.grid()
#---------------------------------------------------------
# Controle proporcional + integral (PI)
# Criando um vetor T (tempo) para simular : de 0s até 0.5s
T  = np.linspace(0,0.5,51)
# Criando um vetor Krange para variar o ganho proporcional
Krange = np.linspace(40,50,6)
Ti = 0.02
plt.show()
for Kp in Krange:
  numC = [Kp*Ti, Kp]
  denC = [Ti, 0]
  Gpi  = co.tf(numC, denC)
  G_MF = co.feedback(Gpi*G,1)
  t,y  = co.step_response(G_MF,T)
  plt.plot(t,y)
plt.axis([0,0.2,0,1.3])
plt.grid()
#---------------------------------------------------------
# Controle proporcional + derivativo (PD)
# Criando um vetor T (tempo) para simular : de 0s até 0.5s
T  = np.linspace(0,0.5,51)
# Criando um vetor Krange para variar o ganho proporcional
Krange = np.linspace(40,100,7)
Td = 0.005
plt.show()
for Kp in Krange:
  numC = [Kp*Td, Kp]
  denC = [0, 1]
  Gpd  = co.tf(numC, denC)
  G_MF = co.feedback(Gpd*G,1)
  t,y  = co.step_response(G_MF,T)
  plt.plot(t,y)
plt.axis([0,0.2,0,1])
plt.grid()
#---------------------------------------------------------
# Controle proporcional + integral + derivativo (PID)
# Criando um vetor T (tempo) para simular : de 0s até 0.5s
T  = np.linspace(0,0.5,51)
# Criando um vetor Krange para variar o ganho proporcional
Krange = np.linspace(50,60,6)
Ti = 0.02
Td = 0.005
plt.show()
for Kp in Krange:
  numC = [Kp*Td*Ti, Kp*Ti, Kp]
  denC = [Ti, 0]
  Gpid = co.tf(numC, denC)
  G_MF = co.feedback(Gpid*G,1)
  t,y  = co.step_response(G_MF,T)
  plt.plot(t,y)
plt.axis([0,0.25,0,1.3])
plt.grid()
#---------------------------------------------------------
# Malha aberta
# Criando um vetor T (tempo) para simular : de 0s até 10s
T  = np.linspace(0,10,1001)
plt.show()
t,y = co.step_response(G,T)
plt.plot(t,y)
plt.axis([0,10,0,1])
plt.grid()