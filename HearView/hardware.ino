#include <LiquidCrystal.h>

// LCD pin setup
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  Serial.begin(9600);  // Start Serial Monitor
  lcd.begin(16, 2);    // Initialize the LCD
  lcd.print("Waiting...");
}

void loop() {
  if (Serial.available()) {
    lcd.clear();
    String input = Serial.readStringUntil('\n');  // Read input from Serial Monitor
    input.trim();  // Remove unnecessary spaces

    if (input.length() <= 16) {
      // If text fits in one row, display on first row
      lcd.setCursor(0, 0);
      lcd.print(input);
    } else {
      // Split text into two rows without breaking words
      int splitPos = 16;  // Start splitting at 16th character
      while (splitPos > 0 && input[splitPos] != ' ') {
        splitPos--;  // Move back to the last space
      }

      if (splitPos == 0) splitPos = 16;  // If no space found, force split

      // First row text
      lcd.setCursor(0, 0);
      lcd.print(input.substring(0, splitPos));

      // Second row text
      lcd.setCursor(0, 1);
      lcd.print(input.substring(splitPos + 1));  // Skip the space
    }
  }
}
