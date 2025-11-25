# Fundamentos da programação em **python**

##Variável
1. Tipos de variável:
- _print(type())_
1.1. Char - **str**
1.2. Numérica - **int**  
1.3. Ponto flutuante - **float**
1.4. Booleana <true/false> - **bool**

##Operadores aritméticos
- (+),(-),(*),(/)
- Divisão inteira: //
    + Ignora as casas decimais.
- Módulo resto: %
- Potência: **

###Utilizando **format strig**: 
- Format Strings (ou formatação de strings) é a técnica usada no Python para misturar texto fixo com variáveis de forma organizada, sem precisar ficar usando o sinal de + para colar pedaços de texto. Para usar, basta colocar a letra f antes das aspas e colocar as variáveis dentro de chaves {}.
- Ex: 
n1 = 5
n2 = 5
r = n1+n2

print(**f**'A soma de **{** n1 **}** + **{** n2 **}** é **{** r **}**')

- Ex:
print("Informe dois números para que possa ser realizado as dieferentes formas de operação:")
print('O primeiro número:')
a = int(input())
print('O segundo número:')
b = int(input())

print(f'Soma de {a + b} é:')
print(f'Subtração de {a - b} é:')
print(f'Multiplicação de {a * b} é:')
print(f'Divisão de {a / b} é:')


##Operadores lógicos
1. and(e)
or(ou)
not(negação)


##Operadores relacionais
1.
== (igual a)
!= (diferente de)
> 
<
>=
<=


#Coleções
1.**Listas**
- <variável> = []
- ordenada, mutável, aceita valores duplicados.

1.1.Acessando objeto da lista.
_n = ['Frango','Carne','Linguiça']_
	_print(n[1])_

será printado: Carne.

1.2.Adicionando objeto na lista.
- <variável>**.append**()

1.3.Inserindo objeto na lista 
- <variável>**.insert**(<indice>)

1.4.Atualizando objeto do índice.
- <variável>[indice] = "str"

1.5.Removendo objeto especifico 
- <variável>**.remove** = "str"
	+ <variável>**.pop**()
	
1.6.Tamanho da lista.
- print(len(<variável>))

1.7.Contar repetições 
- <variavel>**.count**()

1.8.Juntar listas
- <variável a> = []
- <variável b> = []

- <variável c> = <variável a> + <variável b>
- print(<variável c>)


2.**Tuplas**
- <variável> = (...)
- imutável, dados fixo, heterogêneos.
Ex: dias da semana, coordenadas.


3.**Set** 
- Declaração 
- <variável> = {...}
	+ <variável> = set([...])
- não ordenado, mutável, não permite duplicação.





