dias = float(input('Quantos dias o caro foi alugado? '))
km = float(input('Quantos Km rodados? '))
preço = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(preço))
