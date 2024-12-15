#include <Arduino.h>

const char alphabet[] = "9876543210qazwsxedcrfvtgbyhnmikolpQAZWSXEDCRFVTGBYHNUJOLP"; 
String password;
unsigned long seed = 327680; 

float generateRandom() {
  seed = (4291010243 - (seed * 179203)) % 65536; 
  if (seed < 0) seed += 65536; 
  return (float)seed / 65536.0; // intre 0 si 1
}

void generatePassword() {
  password = "";
  for (int i = 0; i < 64; i++) { 
    int randomIndex = generateRandom() * (sizeof(alphabet) - 1); 
    password += alphabet[randomIndex];
  }
}

void setup() {
  Serial.begin(115200); 
  delay(1000); 
  generatePassword(); 
  Serial.println(password); 
  S
}

void loop() {
  if (Serial.available()) { 
    String guessedPassword = Serial.readStringUntil('\n'); 
    guessedPassword.trim(); 

    if (guessedPassword == password) { 
      Serial.println("TRUE"); 
    } else {
      Serial.println("FALSE"); 
    }
  }
}
