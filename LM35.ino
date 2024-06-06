#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
#define LM35_1 A0
#define LM35_2 A1
#define led 13
float tempCelsius1 ;//độ C
float preTempCelsius1 ;//độ C
float tempCelsius2 ;//độ C
float preTempCelsius2 ;//độ C
unsigned long elapsedTime;
void setup() {
 lcd.begin(16, 2);
 pinMode(led, OUTPUT);
 Serial.begin(9600);
}
void loop() {
 if (millis() - elapsedTime >= 100)
 {
 elapsedTime = millis();
 tempCelsius1 = (5.0*(float)analogRead(LM35_1)*100.0/1023.0);
 tempCelsius2 = (5.0*(float)analogRead(LM35_2)*100.0/1023.0);
 if ((tempCelsius1 > 30) || (tempCelsius2 > 30)){
  digitalWrite(led,1);
  }
 else{
  digitalWrite(led,0);
 }
 if (tempCelsius1!= preTempCelsius1)
 {
 lcd.setCursor(7, 0);
 lcd.print(" "); // In 9 khoảng trắng để xóa
 }
 if (tempCelsius2!= preTempCelsius2)
 {
 lcd.setCursor(7, 1);
 lcd.print(" "); // In 9 khoảng trắng để xóa
 }
lcd.setCursor(0, 0);
 lcd.print("TEMP ");
 lcd.print(char(223));
 lcd.print("C:");
 lcd.print(tempCelsius1);
 lcd.print(char(223));
 lcd.print("C");
 lcd.setCursor(0, 1);
 lcd.print("TEMP ");
 lcd.print(char(223));
 lcd.print("C:");
 lcd.print(tempCelsius2);
 lcd.print(char(223));
 lcd.print("C");
 Serial.print(tempCelsius1);
 Serial.print(" ");
 Serial.println(tempCelsius2);
 preTempCelsius1 = tempCelsius1;
 preTempCelsius2 = tempCelsius2;
 }
}
