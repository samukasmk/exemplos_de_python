###
### UMA FUNÇÃO É UM BLOCO DE CÓDIGO
###

# definindo uma variavel global
nome_global = 'samuka'

# imprimindo uma variavel global
print(nome_global, 'esta de fora')

# definiu a funcao
def funcao_teste_de_variavel(teste_arg):

    print(nome_global, 'esta de dentro')
    print(teste_arg, 'local')

# chamando a funcao, com um argumento posicional
funcao_teste_de_variavel('eu sou um posicional')

# chamando a funcao, com um argumento posicional
funcao_teste_de_variavel(teste_arg='eu sou um declarativo')
