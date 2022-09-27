import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

meusdados = pd.read_csv('./dadosk.csv')

trat1 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 1.08]
iso_trat1 = trat1['Classificação']

trat2 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 3.2]
iso_trat2 = trat2['Classificação']

trat3 = meusdados.loc[meusdados['Velocidade(KM/h)'] == 4.8]
iso_trat3 = trat3['Classificação']

barWidth = 0.25

plt.figure(figsize=(10,5))

r1 = np.arange(len(iso_trat1))