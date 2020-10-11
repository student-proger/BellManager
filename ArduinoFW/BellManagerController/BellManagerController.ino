/*******************************************************************************
* Author:         Gladyshev Dmitriy (2020) 
* 
* Design Name:    BellManager
* Target Devices: Arduino
* Tool versions:  Arduino 1.8.5 
* Description:    Контроллер управления освещением и звонками в школе
* Version:        1.0
* 
*******************************************************************************/

#define PIN_RING_AB 2
#define PIN_RING_C  3
#define PIN_LIGHT_A 5
#define PIN_LIGHT_B 6
#define PIN_LIGHT_C 7

#define PIN_LED_RING_AB  17
#define PIN_LED_RING_C   15
#define PIN_LED_LIGHT_AB 14
#define PIN_LED_LIGHT_C  18
#define PIN_LED_RX       19

bool LightOn = false;
bool LightNachalkaOn = false;
bool inits = false;
bool watchDogEnabled = false;

unsigned long lastComm = 0;

char buf[5] = {' ', ' ', ' ', ' ', ' '};

void resetWatchDog()
{
  lastComm = millis();
  digitalWrite(PIN_LED_RX, HIGH);
}

void watchDog()
{
  if (millis() - lastComm > 5000)
  {
    digitalWrite(PIN_LIGHT_C, LOW);
    digitalWrite(PIN_LIGHT_B, LOW);
    digitalWrite(PIN_LIGHT_A, LOW);
    digitalWrite(PIN_RING_C, HIGH);
    digitalWrite(PIN_RING_AB, HIGH);

    digitalWrite(PIN_LED_LIGHT_AB, LOW);
    digitalWrite(PIN_LED_RING_C, LOW);
    digitalWrite(PIN_LED_RING_AB, LOW);
    digitalWrite(PIN_LED_LIGHT_C, LOW);
    digitalWrite(PIN_LED_RX, LOW);
    watchDogEnabled = false;
  }
  if (millis() - lastComm > 100)
  {
    digitalWrite(PIN_LED_RX, LOW);
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(PIN_LIGHT_C, OUTPUT);
  pinMode(PIN_LIGHT_B, OUTPUT);
  pinMode(PIN_LIGHT_A, OUTPUT);
  pinMode(PIN_RING_C, OUTPUT);
  pinMode(PIN_RING_AB, OUTPUT);

  digitalWrite(PIN_LIGHT_C, LOW);
  digitalWrite(PIN_LIGHT_B, LOW);
  digitalWrite(PIN_LIGHT_A, LOW);
  digitalWrite(PIN_RING_C, HIGH);
  digitalWrite(PIN_RING_AB, HIGH);

  pinMode(PIN_LED_LIGHT_AB, OUTPUT);
  pinMode(PIN_LED_RING_C, OUTPUT);
  pinMode(PIN_LED_RING_AB, OUTPUT);
  pinMode(PIN_LED_LIGHT_C, OUTPUT);
  pinMode(PIN_LED_RX, OUTPUT);

  digitalWrite(PIN_LED_LIGHT_AB, LOW);
  digitalWrite(PIN_LED_RING_C, LOW);
  digitalWrite(PIN_LED_RING_AB, LOW);
  digitalWrite(PIN_LED_LIGHT_C, LOW);
  digitalWrite(PIN_LED_RX, LOW);
}

void loop() {
  if (Serial.available())
  {
    char inChar = Serial.read();

    if (!inits)
    {
      for (int i = 0; i < 4; i++)
      {
        buf[i] = buf[i + 1];
      }
      buf[4] = inChar;
      if ((buf[0] == 'Y') && (buf[1] == '-') && (buf[2] == '-') 
        && (buf[3] == '$') && (buf[4] == 'K'))
      {
        inits = true;
        watchDogEnabled = true;
      }
    }
    else
    {
      //Выключение звонка в основной школе
      if (inChar == 'q')
      {
        digitalWrite(PIN_RING_AB, HIGH);
        digitalWrite(PIN_LED_RING_AB, LOW);
        resetWatchDog();
      }
      //Включение звонка в основной школе
      if (inChar == 'Q')
      {
        digitalWrite(PIN_RING_AB, LOW);
        digitalWrite(PIN_LED_RING_AB, HIGH);
        resetWatchDog();
      }
      //Выключение звонка в начальной школе
      if (inChar == 'w')
      {
        digitalWrite(PIN_RING_C, HIGH);
        digitalWrite(PIN_LED_RING_C, LOW);
        resetWatchDog();
      }
      //Включение звонка в начальной школе
      if (inChar == 'W')
      {
        digitalWrite(PIN_RING_C, LOW);
        digitalWrite(PIN_LED_RING_C, HIGH);
        resetWatchDog();
      }
      //Включение освещения в основной школе
      if (inChar == 'E')
      {
        digitalWrite(PIN_LIGHT_A, HIGH);
        digitalWrite(PIN_LIGHT_B, HIGH);
        digitalWrite(PIN_LED_LIGHT_AB, HIGH);
        resetWatchDog();
      }
      //Выключение освещения в основной школе
      if (inChar == 'e')
      {
        digitalWrite(PIN_LIGHT_A, LOW);
        digitalWrite(PIN_LIGHT_B, LOW);
        digitalWrite(PIN_LED_LIGHT_AB, LOW);
        resetWatchDog();
      }
      //Включение освещения в начальной школе
      if (inChar == 'R')
      {
        digitalWrite(PIN_LIGHT_C, HIGH);
        digitalWrite(PIN_LED_LIGHT_C, HIGH);
        resetWatchDog();
      }
      //Выключение освещения в начальной школе
      if (inChar == 'r')
      {
        digitalWrite(PIN_LIGHT_C, LOW);
        digitalWrite(PIN_LED_LIGHT_C, LOW);
        resetWatchDog();
      }
    }
  }
  if (watchDogEnabled)
  {
    watchDog();
  }
}
