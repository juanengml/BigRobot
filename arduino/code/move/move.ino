char letra;

int pin1 = 9; // motor A 
int pin2 = 8; // MOtor A 


int pin3 = 11;
int pin4 = 10;

void setup() {
 Serial.begin(9600);
 pinMode(pin1,OUTPUT);
 pinMode(pin2,OUTPUT);
 pinMode(pin3,OUTPUT);
 pinMode(pin4,OUTPUT);
 Serial.println("BigRobot RUNNING...");
}

void loop() {
  letra = Serial.read();
  switch(letra){
    case 'w':
    Serial.println("MOTOR A and B RUN ");
    digitalWrite(pin1,HIGH);       // Motor A 
    digitalWrite(pin2,LOW);       // Motor A 
    digitalWrite(pin3,HIGH);
    digitalWrite(pin4,LOW);
    break;
    case 's':
    Serial.println("MOTOR A and B  BACK ");   
    digitalWrite(pin1,LOW);  // Motor A 
    digitalWrite(pin2,HIGH);  // Motor A
    digitalWrite(pin3,LOW);   // MOtor B
    digitalWrite(pin4,HIGH);    // MOtor B
    break;
    case 'p':
    Serial.println("MOTOR A and B STOP ");
    digitalWrite(pin1,LOW); // Motor A 
    digitalWrite(pin2,LOW); // Motor A 
    digitalWrite(pin3,LOW); // MOtor B 
    digitalWrite(pin4,LOW);  // MOtor B
    break;

    case 'd':

        Serial.println("MOTOR 3 DIRECAO: (DIREITA)");
        digitalWrite(pin1,LOW);
        digitalWrite(pin2,HIGH);
        digitalWrite(pin3,LOW);
        digitalWrite(pin4,LOW);

    break;
    case 'a':
     Serial.println("MOTOR 3 DIRECAO: (ESQUERDA");
     digitalWrite(pin1,HIGH);
     digitalWrite(pin2,LOW);
     digitalWrite(pin3,LOW);
     digitalWrite(pin4,LOW);

    break;

    
  }

}
