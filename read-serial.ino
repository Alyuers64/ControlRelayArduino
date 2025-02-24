#define RELAY1 7 
#define RELAY2 8  
#define RELAY3 9  

void setup() {
  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(RELAY3, OUTPUT);
  digitalWrite(RELAY1, HIGH);
  digitalWrite(RELAY2, HIGH);
  digitalWrite(RELAY3, HIGH);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    Serial.println(data);

    switch (data) {
      case '0': 
        digitalWrite(RELAY1, HIGH);
        digitalWrite(RELAY2, HIGH);
        digitalWrite(RELAY3, HIGH);
        break;

      case '1': 
        digitalWrite(RELAY1, LOW);
        digitalWrite(RELAY2, HIGH);
        digitalWrite(RELAY3, HIGH);
        break;

      case '2': 
        digitalWrite(RELAY1, LOW);
        digitalWrite(RELAY2, LOW);
        digitalWrite(RELAY3, HIGH);
        break;

      case '3':
        digitalWrite(RELAY1, LOW);
        digitalWrite(RELAY2, LOW);
        digitalWrite(RELAY3, LOW);
        break;

      case '5': 
        digitalWrite(RELAY1, LOW);
        digitalWrite(RELAY2, LOW);
        digitalWrite(RELAY3, LOW);
        break;

      default:
        break;
    }
  }
}
