import random

alunoA = str(input('Digite seu nome: '))
alunoB = str(input('Digite seu nome: '))
alunoC = str(input('Digite seu nome: '))
alunoD = str(input('Digite seu nome: '))

lista = [alunoA, alunoB, alunoC, alunoD]
sorteio = random.choice(lista)

print('o ganhador foi: ' + sorteio)