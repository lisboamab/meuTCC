#include <Boards.h>
#include <Firmata.h>
#include <FirmataConstants.h>
#include <FirmataDefines.h>
#include <FirmataMarshaller.h>
#include <FirmataParser.h>

#define pinSensor1 8

bool s_high = 0;
unsigned long contador = 0;

void setup() {

    pinMode(pinSensor1, INPUT);
    Serial.begin(9600);
}

void loop(){
  if(digitalRead(pinSensor1)) s_high = 1 ;

  if(!digitalRead(pinSensor1) && s_high)
  {
    s_high = 0;
    contador += 1;
    Serial.println(contador);
  };

}
