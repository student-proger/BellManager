/*******************************************************************************
* Author:         Gladyshev Dmitriy (2020-2021)
*
* Design Name:    BellManager
* Target Devices: Arduino
* Tool versions:  Arduino 1.8.13
* Description:    Контроллер управления освещением и звонками в школе
* Version:        2.0
* 
*******************************************************************************/

#define PIN_RING_AB 3
#define PIN_RING_C  2
#define PIN_LIGHT_A 4
#define PIN_LIGHT_B 5
#define PIN_LIGHT_C 6

#define PIN_LED_RX       13

#define PIN_CONTROL_L1  A0
#define PIN_CONTROL_L2  A1
#define PIN_CONTROL_L3  A2

unsigned long timeL1 = 0;
unsigned long timeL2 = 0;
unsigned long timeL3 = 0;
bool enL1 = false;
bool enL2 = false;
bool enL3 = false;

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
    digitalWrite(PIN_RING_C, LOW);
    digitalWrite(PIN_RING_AB, LOW);

    enL1 = false;
    enL2 = false;
    enL3 = false;

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

  pinMode(PIN_CONTROL_L1, INPUT);
  pinMode(PIN_CONTROL_L2, INPUT);
  pinMode(PIN_CONTROL_L3, INPUT);

  digitalWrite(PIN_LIGHT_C, LOW);
  digitalWrite(PIN_LIGHT_B, LOW);
  digitalWrite(PIN_LIGHT_A, LOW);
  digitalWrite(PIN_RING_C, LOW);
  digitalWrite(PIN_RING_AB, LOW);

  pinMode(PIN_LED_RX, OUTPUT);

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
        digitalWrite(PIN_RING_AB, LOW);
        resetWatchDog();
      }
      //Включение звонка в основной школе
      if (inChar == 'Q')
      {
        digitalWrite(PIN_RING_AB, HIGH);
        resetWatchDog();
      }
      //Выключение звонка в начальной школе
      if (inChar == 'w')
      {
        digitalWrite(PIN_RING_C, LOW);
        resetWatchDog();
      }
      //Включение звонка в начальной школе
      if (inChar == 'W')
      {
        digitalWrite(PIN_RING_C, HIGH);
        resetWatchDog();
      }

      //Включение освещения в основной школе
      if (inChar == 'E')
      {
        digitalWrite(PIN_LIGHT_A, HIGH);
        digitalWrite(PIN_LIGHT_B, HIGH);
        timeL1 = millis();
        timeL2 = millis();
        enL1 = true;
        enL2 = true;
        resetWatchDog();
      }
      //Выключение освещения в основной школе
      if (inChar == 'e')
      {
        digitalWrite(PIN_LIGHT_A, LOW);
        digitalWrite(PIN_LIGHT_B, LOW);
        enL1 = false;
        enL2 = false;
        resetWatchDog();
      }
      //Включение освещения в начальной школе
      if (inChar == 'R')
      {
        digitalWrite(PIN_LIGHT_C, HIGH);
        timeL3 = millis();
        enL3 = true;
        resetWatchDog();
      }
      //Выключение освещения в начальной школе
      if (inChar == 'r')
      {
        digitalWrite(PIN_LIGHT_C, LOW);
        enL3 = false;
        resetWatchDog();
      }
    }
  }
  if (watchDogEnabled)
  {
    watchDog();
  }

  //Контроль обрыва линий
  if (enL1 && (millis() - timeL1 >= 500) && !digitalRead(PIN_CONTROL_L1))
  {
    timeL1 = millis();
    digitalWrite(PIN_LIGHT_A, !digitalRead(PIN_LIGHT_A));
  }
  if (enL2 && (millis() - timeL2 >= 500) && !digitalRead(PIN_CONTROL_L2))
  {
    timeL2 = millis();
    digitalWrite(PIN_LIGHT_B, !digitalRead(PIN_LIGHT_B));
  }
  if (enL3 && (millis() - timeL3 >= 500) && !digitalRead(PIN_CONTROL_L3))
  {
    timeL3 = millis();
    digitalWrite(PIN_LIGHT_C, !digitalRead(PIN_LIGHT_C));
  }
}
