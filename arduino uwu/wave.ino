const int rLed1 = 2;
const int rLed2 = 6;
const int rLed3 = 5;
const int rLed4 = 4;
const int rLed5 = 3;

void setup() 
{       
      pinMode(rLed1, OUTPUT);  
      pinMode(rLed2, OUTPUT); 
      pinMode(rLed3, OUTPUT); 
      pinMode(rLed4, OUTPUT); 
      pinMode(rLed5, OUTPUT); 
}        

void loop() 
{
    digitalWrite(rLed1, HIGH);  0
    digitalWrite(rLed2, HIGH);
    delay(100);
    digitalWrite(rLed1, LOW);  
    digitalWrite(rLed3, HIGH);
    delay(100); 
    digitalWrite(rLed2, LOW); 
    digitalWrite(rLed4, HIGH);
    delay(100);
    digitalWrite(rLed3, LOW);
    digitalWrite(rLed5, HIGH);
    delay(100);
    digitalWrite(rLed4, LOW);
    digitalWrite(rLed5, LOW);
}
