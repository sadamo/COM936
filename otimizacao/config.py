import random as random

inst = "p55"

caminho = "../dataset/" + inst + ".txt"

solucao = {
    'instalacao': [],
    'custo': []
}

validade_tabu = 20
max_int_tabu = 400

# Possiveis
#   'gulosa'
#   'aleatoria'
#   'hibrida'

random.seed(5)

estrategia = 'gulosa'

estrategias = ['gulosa']

erros_solucao = []

