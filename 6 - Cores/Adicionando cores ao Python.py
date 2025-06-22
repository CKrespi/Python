# Código ANSI para cores no terminal
# Formato geral: \033[style;text;backgroundm

# Tabela de códigos:
# Style      Text Color   Background Color
#   0            30              40
#   1            31              41
#   4            32              42
#   7            33              43
#                34              44
#                35              45
#                36              46
#                37              47

# Exemplos de uso (exibindo diferentes combinações no terminal):
print('\033[1;30;47mTexto preto em fundo branco\033[m')
print('\033[1;31;40mTexto vermelho em fundo preto\033[m')
print('\033[1;32;40mTexto verde em fundo preto\033[m')
print('\033[1;33;44mTexto amarelo em fundo azul\033[m')
print('\033[1;34;47mTexto azul em fundo branco\033[m')
print('\033[1;35;40mTexto magenta em fundo preto\033[m')
print('\033[1;36;40mTexto ciano em fundo preto\033[m')
print('\033[1;37;40mTexto branco em fundo preto\033[m')

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

nome = 'Cauê'
print('É um prazer te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))