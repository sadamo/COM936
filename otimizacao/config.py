import copy
import numpy as np
import time as time


dados_clientes = {
    'custo': [],
    'demanda': [],
    'disponivel': [],
    'posicao': []
}

dados_plantas = {
    'custo': [],
    'capacidade': [],
    'posicao': [],
}

solucao = {
    'instalacao': [],
    'custo': [],
    'total': int
}

inst = "p3"

caminho = "../dataset/" + inst + ".txt"

# Possiveis
#   'gulosa'
#   'aleatoria'
#   'hibrida'

estrategia = 'gulosa'

estrategias = ['gulosa']
