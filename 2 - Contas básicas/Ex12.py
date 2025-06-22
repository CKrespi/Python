preço = (float(input('Qual é o valor do produto? R$')))
novoValor = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preço, novoValor))