#include <LiquidCrystal.h>
#include <SoftwareSerial.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
//             (RS, En, D4, D5, D6, D7)

String msg = "";

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  msg = analogRead(A0);
  Serial.print("/");
  Serial.println(msg);
  delay(500);

  
}
