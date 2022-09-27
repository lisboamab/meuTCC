from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def soma(a, b, c):
    return a + b + c

def percentual(total: int, parcela: int):
    return (parcela*100)/total



meusdados = pd.read_csv('./dadosk.csv')

aceitavel, duplo, nulo = 0, 0, 0

trat1 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 1.08]
iso_trat1 = list(trat1['Classificação'])


trat2 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 3.2]
iso_trat2 = list(trat2['Classificação'])


trat3 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 4.8]
iso_trat3 = list(trat3['Classificação'])


tratamentos = [iso_trat1, iso_trat2, iso_trat3]
nomes_tratamentos = ['Velocidade 1.08', 'Velocidade 3.2', 'Velocidade 4.8']

for i, k in zip(tratamentos, nomes_tratamentos):
    for j in i:
        if j == 'Aceitável':
            aceitavel += 1
        elif j == 'Duplo':
            duplo += 1
        elif j == 'Nulo':
            nulo += 1
        else:
            print('Dado Invalido')
    
    somatotal = soma(aceitavel, duplo, nulo)
    
    print(f"Tratamento: {k}\n")
    print(f"Aceitavel: {aceitavel} P: {percentual(somatotal, aceitavel):.2f}%\n")
    print(f"Duplo: {duplo} P: {percentual(somatotal, duplo):.2f}%\n")
    print(f"Nulo: {nulo} P: {percentual(somatotal, nulo):.2f}%")
    aceitavel, duplo, nulo = 0, 0, 0
    

# barWidth = 0.25

# plt.figure(figsize=(10,5))

# r1 = np.arange(len(iso_trat1))
# r2 = [x + barWidth for x in r1]
# r3 = [x + barWidth for x in r2]

# plt.bar(r1, iso_trat1, color= '#6A5ACD', width=barWidth, label='1.08')
# plt.bar(r2, iso_trat2, color= '#6495ED', width=barWidth, label='3.2')
# plt.bar(r3, iso_trat3,  color= '#00BFFF', width=barWidth, label='4.8')

# plt.xlabel('Velocidade (Km/H)')
# plt.xticks([r + barWidth for r in range(len(iso_trat1))], ['1.08', '3.2', '4.8'])
# plt.ylabel('Frequencia')

# plt.legend()
# plt.show()
