import numpy as np
from scipy import stats

# Salários em Reais (R$) de profissionais no mesmo nível nas duas empresas

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]



def analisar_empresa(nome, dados):
    print(f'''
    Análise: {nome}
    Média: {np.mean(dados):.2f}
    Mediana: {np.median(dados):.2f}
    Moda: {stats.mode(dados, keepdims=True).mode[0]}
    Desvio Padrão: {np.std(dados):.2f}
            ''')
analisar_empresa("empresa1", empresa1)
analisar_empresa("empresa2", empresa2)
analisar_empresa("empresa3", empresa3)
analisar_empresa("empresa4", empresa4)

