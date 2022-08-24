from re import M
from pyfirmata import Arduino, util
from datetime import datetime
import time

Uno = Arduino('COM3') #Colocar a porta USB do Arduino
it = util.Iterator(Uno)
it.start()
time.sleep(1)

sensorOptico = Uno.get_pin('d:8:i')
repeticao = 1 #alterar manualamente
contador = 0
controlador = 0

while True:
    time.sleep(0.15)
    estSensor = sensorOptico.read()
    
    if estSensor and controlador == 0:
        controlador = 1
    
    if ((not estSensor) and controlador == 1):

        contador += 1
        tempoInicial = datetime.now()
        tempoInicial = tempoInicial.strftime("%H:%M:%S")
        velocidadeKMH = 7
        linhaDeDado = (f"{repeticao};{contador};{tempoInicial};{velocidadeKMH};DE\n")
        time.sleep(0.15)


        print(linhaDeDado)
        controlador = 0

        

        arquivo = open("MeusDados.txt", "a")
        arquivo.write(linhaDeDado)
        arquivo.close
