salario = int(input('Digite seu sálario: '))
desconto = int(input('Digite quantos porcento deseja aumentar o salario: '))

aumento = desconto / 100 * salario

print('O seu salario é de R${} e adicionado um aumento de {}% ficaria R${}'.format(salario, desconto, aumento + salario))





