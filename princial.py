from re import M
from pyfirmata import Arduino, util
from datetime import datetime

# Uno = Arduino('') #Colocar a porta USB do Arduino

repeticao = 1
contador = 0

while True:
    if not True:
        contador += 1
    tempoInicial = datetime.now()
    tempoInicial = tempoInicial.strftime("%H:%M:%S")
    velocidadeKMH = 7
    linhaDeDado = (f"{repeticao};{contador};{tempoInicial};{velocidadeKMH};DE\n")


    print(linhaDeDado)


    arquivo = open("MeusDados.txt", "a")
    arquivo.write(linhaDeDado)
    arquivo.close
