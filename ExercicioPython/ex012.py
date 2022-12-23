valor = int(input('Digite o preço que você quer descontar: '))
porcento = int(input('Digite quantos porcento deseja descontar: '))

porcentagem = porcento / 100 * valor
desconto = valor - porcentagem

print('Valor do produto é R${} menos {}% de desconto Ficaria R${}'.format(valor, porcento,desconto))