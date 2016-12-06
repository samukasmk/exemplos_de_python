###
### UMA LISTA EH UM CONJUNTO DE DADOS NA MESMA VARIAVEL, ORDENADA POR INDICES
###

# exemplo de uma lista
frutas = ['amora', 'pessego', 'melancia', 'uva']

# por padrao uma lista possui o primeiro indice como 0!

# o conceito de acessar os items da lista eh chamdo de slice (fatiar)!

# vamos fatiar/pegando a primeira fruta da lista
print( frutas[0] )

# pegado a terceira fruta da lista, de indice 2!
print( frutas[2] )

# o pulo do gato! pegado a ultima fruta da lista
print( frutas[-1] )

# contando quantas frutas tem na lista
print ('nessa lista tem', len(frutas) ,'frutas')

# checando a quantidade de itens na lista, para pegar um objeto que exista
indice_desejado = 10

if indice_desejado < len(frutas):
    print( frutas[indice_desejado] )
else:
    print('a lista soh tem:', len(frutas), 'frutas! impossivel de pegar o indice:', indice_desejado)


# retirando o 2 item da lista, que possui o indice: 1
print('eu removi a fruta:', frutas.pop(1), 'da lista! agora soh as seguintes frutas: ', frutas )

# adicionando uma nova fruta ao final da lista
frutas.append('banana')

print('agora temos as seguintes frutas:', frutas)
