from re import M
from pyfirmata import Arduino, util
from datetime import datetime

Uno = Arduino('') #Colocar a porta USB do Arduino
Uno.digital[8].read

id = 2
tempoInicial = datetime.now()
tempoInicial = tempoInicial.strftime("%H:%M:%S")
velocidadeKMH = 7
linhaDeDado = (f"{id};{tempoInicial};{velocidadeKMH}\n")


print(f" São {linhaDeDado}")


arquivo = open("MeusDados.txt", "a")
arquivo.write(linhaDeDado)
arquivo.close
