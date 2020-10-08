bool LightOn = false;
bool LightNachalkaOn = false;
bool inits = false;
bool watchDogEnabled = false;

unsigned long lastComm = 0;

char buf[5] = {' ', ' ', ' ', ' ', ' '};

void resetWatchDog()
{
  lastComm = millis();
  digitalWrite(19, HIGH);
}

void watchDog()
{
  if (millis() - lastComm > 5000)
  {
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);

    digitalWrite(14, LOW);
    digitalWrite(15, LOW);
    digitalWrite(17, LOW);
    digitalWrite(18, LOW);
    digitalWrite(19, LOW);
    watchDogEnabled = false;
  }
  if (millis() - lastComm > 100)
  {
    digitalWrite(19, LOW);
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);

  digitalWrite(7, LOW);
  digitalWrite(6, LOW);
  digitalWrite(5, LOW);
  digitalWrite(3, HIGH);
  digitalWrite(2, HIGH);

  pinMode(14, OUTPUT);
  pinMode(15, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);

  digitalWrite(14, LOW);
  digitalWrite(15, LOW);
  digitalWrite(17, LOW);
  digitalWrite(18, LOW);
  digitalWrite(19, LOW);

  /* 14 - 2
   *  15 - 3
   *  16 - 
   *  17 - 4
   *  18 - 1
   *  19 - 5
   */
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

      if (inChar == 'q')
      {
        digitalWrite(2, HIGH);
        digitalWrite(17, LOW);
        resetWatchDog();
      }
      if (inChar == 'Q')
      {
        digitalWrite(2, LOW);
        digitalWrite(17, HIGH);
        resetWatchDog();
      }
  
      if (inChar == 'w')
      {
        digitalWrite(3, HIGH);
        digitalWrite(15, LOW);
        resetWatchDog();
      }
      if (inChar == 'W')
      {
        digitalWrite(3, LOW);
        digitalWrite(15, HIGH);
        resetWatchDog();
      }
  
      if (inChar == 'E')
      {
        digitalWrite(5, HIGH);
        digitalWrite(6, HIGH);
        digitalWrite(14, HIGH);
        resetWatchDog();
      }
      if (inChar == 'e')
      {
        digitalWrite(5, LOW);
        digitalWrite(6, LOW);
        digitalWrite(14, LOW);
        resetWatchDog();
      }
  
      if (inChar == 'R')
      {
        digitalWrite(7, HIGH);
        digitalWrite(18, HIGH);
        resetWatchDog();
      }
      if (inChar == 'r')
      {
        digitalWrite(7, LOW);
        digitalWrite(18, LOW);
        resetWatchDog();
      }
    }
  }
  if (watchDogEnabled)
  {
    watchDog();
  }
}
