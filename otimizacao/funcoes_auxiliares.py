import numpy as np
from config import *

def entrada_dados():
    with open(caminho, 'r') as f:
        data = f.readlines()
        header = data.pop(0)
        n_clientes, n_plantas = header.split()
        n_clientes = int(n_clientes)
        n_plantas = int(n_plantas)
        for i in range(0, n_clientes):
            cliente = data.pop(0)
            dados_clientes['custo'].append(
                [int(float(cli)) for cli in cliente.split()])
            [dados_clientes['posicao'].append(i)]
            [dados_clientes['disponivel'].append(1)]
        n_linhas_array_clientes = int(n_clientes / n_plantas)
        for i in range(0, n_linhas_array_clientes):
            demanda = data.pop(0)
            [dados_clientes['demanda'].append(
                int(float(dem))) for dem in demanda.split()]
            [dados_clientes['disponivel'].append(1)]

        dados_plantas['custo'] = [
            int(float(cus)) for cus in data.pop(0).split()]
        dados_plantas['capacidade'] = [
            int(float(cap)) for cap in data.pop(0).split()]


def saida_dados(text, tipo):
    np.savetxt('result_%s.txt' % tipo, text, fmt="%s")
    return

def calcula_cxb():
    dados_plantas['cxb'] = []
    for i in range(0, len(dados_plantas['custo'])):
        dados_plantas['cxb'].append(dados_plantas['capacidade'][i] /
                                  dados_plantas['custo'][i])
