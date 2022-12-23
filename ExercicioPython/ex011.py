base = int(input('Digite a sua largura em metros: '))
altura = int(input('Digite sua altura em metros: '))

area = base * altura
litro = area / 2

print('Sua area é de {}m² e você gastaria {}L de tintas para pintar ela toda!! '.format(area, litro))