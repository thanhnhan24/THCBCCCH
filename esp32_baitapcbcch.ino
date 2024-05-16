void setup() {
  // Khởi động Serial để giao tiếp với máy tính
  Serial.begin(115200);
  while (!Serial) {
    // Chờ cho cổng Serial khởi động
  }
  Serial.println("ESP32 ready to receive commands.");
}

void loop() {
  // Kiểm tra xem có dữ liệu từ cổng Serial không
  if (Serial.available()) {
    // Đọc chuỗi dữ liệu từ cổng Serial
    String input = Serial.readStringUntil('\n');

    // Loại bỏ ký tự xuống dòng (nếu có)
    input.trim();

    // Kiểm tra định dạng của chuỗi dữ liệu
    if (input.length() == 5 && input[2] == '-') {
      // Tách chuỗi thành hai phần: XX và YY
      String pinStr = input.substring(0, 2);
      String stateStr = input.substring(3, 5);

      // Chuyển đổi XX và YY thành số nguyên
      int pin = pinStr.toInt();
      int state = stateStr.toInt();

      // Kiểm tra xem chân có hợp lệ không (giả sử dùng các chân từ 0 đến 39 của ESP32)
      if (pin >= 0 && pin <= 39) {
        // Thiết lập chế độ chân là OUTPUT
        pinMode(pin, OUTPUT);

        // Cập nhật trạng thái của chân
        if (state == 1) {
          digitalWrite(pin, HIGH);
          Serial.println("Pin " + String(pin) + " set to HIGH");
        } else if (state == 0) {
          digitalWrite(pin, LOW);
          Serial.println("Pin " + String(pin) + " set to LOW");
        } else {
          Serial.println("Invalid state: " + stateStr);
        }
      } else {
        Serial.println("Invalid pin number: " + pinStr);
      }
    } else {
      Serial.println("Invalid input format. Expected format: XX-YY");
    }
  }
}
