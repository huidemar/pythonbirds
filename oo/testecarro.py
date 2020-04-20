from motor import Motor
from direcao import Direcao
from carro import Carro

print('testando motor')
motor = Motor()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
motor.frear()
print(motor.velocidade)

direcao = Direcao()
carro = Carro(direcao=direcao, motor=motor)
carro.calcular_velocidade()
