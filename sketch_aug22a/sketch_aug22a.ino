#define pinSensor1 7

int contador = 0;

void setup() {

    pinMode(pinSensor1, INPUT);
    Serial.begin(9600);
}

void loop(){

    bool estadoSensor1 = digitalRead(pinSensor1);

    if (estadoSensor1){
        contador += 0;
    } else{ 
        contador += 1;
    }

    Serial.println(contador);
}
