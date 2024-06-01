void setup() {
  Serial.begin(9600);
  for (int i=1;i <= 50;i++){
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    int d = Serial.parseInt();
    digitalWrite(d, !digitalRead(d));
    // Use the received data to control LED and buzzer
  }
  delay(100);
}
