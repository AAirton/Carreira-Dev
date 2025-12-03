'''
Problema 1) 

Sem executar este código pelo VSCode ou python
Execute usando uma folha de Papel e diga o que
Irá aparecer no Print abaixo.
'''

a = 10
b = 3

c = a + b * 2
d = c + a 

e = 0
if d < b:
    e += 1
elif d > b:
    e -= 1
else:
    e = d

f = 9
g = f * (d + e)

print(a, b, c, d, e, f, g)

# Será impresso na tela:
#  10,3,16,26,-1,9,225

# é operador de atribuição composto que adiciona um valor a uma variavel e armazena o resultado na propia variavel.
    # ex: x += 2, x = x + 2

#  nota: -= é utilizado para subtrair um valor de uma variavel e armazenar o resultado de volta.