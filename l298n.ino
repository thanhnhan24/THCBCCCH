// Định nghĩa số chân để điều khiển động cơ
#define IN1 13 // Chân để điều khiển hướng động cơ
#define IN2 12 // Chân để điều khiển hướng động cơ
#define ENA 6 // Chân để điều khiển tốc độ động cơ (PWM)
#define IN3 8  // Chân để điều khiển hướng động cơ
#define IN4 9 // Chân để điều khiển hướng động cơ
#define ENB 10 // Chân để điều khiển tốc độ động cơ (PWM)
int PWM;
// Hàm setup, chạy một lần khi khởi động
void setup() {
  pinMode(IN1, OUTPUT); // Đặt chân IN1 là đầu ra
  pinMode(IN2, OUTPUT); // Đặt chân IN2 là đầu ra
  pinMode(ENA, OUTPUT); // Đặt chân ENA là đầu ra
  pinMode(IN3, OUTPUT); // Đặt chân IN1 là đầu ra
  pinMode(IN4, OUTPUT); // Đặt chân IN2 là đầu ra
  pinMode(ENB, OUTPUT); // Đặt chân ENA là đầu ra
  Serial.begin(9600);
  Serial.println("Serial begin 9600");
}
// Hàm loop, chạy liên tục
void loop() {
  if (Serial.available() > 0) {
    // Đọc dữ liệu từ Serial Monitor
    String input = Serial.readString();

    // Loại bỏ ký tự xuống dòng
    input.trim();

    // Kiểm tra xem chuỗi nhập vào có đủ độ dài để lấy 2 ký tự đầu và phần còn lại là số không
    if (input.length() > 2) {
      // Lưu 2 ký tự đầu vào biến en1 và en2
      char en1 = input.charAt(0);
      char en2 = input.charAt(1);

      // Kiểm tra ký tự thứ 3 và các ký tự còn lại xem có phải là số không
      String numberPart = input.substring(2);
      bool isNumber = true;

      // Kiểm tra chuỗi từ ký tự thứ 3 có nằm trong khoảng -255 đến 255 không
      int startIndex = 0;
      if (numberPart.charAt(0) == '-') {
          startIndex = 1;
      }

      for (int i = startIndex; i < numberPart.length(); i++) {
        if (!isDigit(numberPart.charAt(i))) {
          isNumber = false;
          break;
        }
      }

      if (isNumber) {
        // Chuyển đổi dữ liệu từ chuỗi sang số nguyên
        int PWM = numberPart.toInt();

        // Kiểm tra giá trị trong khoảng -255 đến 255
        if (PWM >= -255 && PWM <= 255) {
            // Xuất số đó ra lại Serial Monitor
            Serial.print("You entered the number: ");
            Serial.println(PWM);
            // Thực hiện hành động với giá trị PWM hợp lệ
            if (en1 == '1'){
              Serial.print("Motor 1 now running at: ");
              Serial.println(PWM);
              Motor1(PWM);
              }
              if (en2 == '0' && PWM == 0){
              Serial.print("Motor 1 now stop ");
              Motor1(0);
                }
            if (en2 == '1'){
              Serial.print("Motor 2 now running at: ");
              Serial.println(PWM);
              Motor2(PWM);
              }
             if (en2 == '0' && PWM == 0){
              Serial.print("Motor 2 now stop ");
              Motor2(0);
                }
        } else {
            Serial.println("Please enter a number between -255 and 255.");
        }
      } else {
        Serial.println("Please enter a valid number.");
      }
    } else {
      Serial.println("Invalid input. Please make sure the input has at least 3 characters.");
    }
  }
}
// Hàm để điều khiển tốc độ và hướng động cơ
void Motor1(int PWM) {
  if (PWM > 0) {
    digitalWrite(IN1, HIGH); // Đặt chân IN1 cao để động cơ tiến tới
    digitalWrite(IN2, LOW); // Đặt chân IN2 thấp
    analogWrite(ENA, PWM); // Đặt tốc độ bằng cách sử dụng PWM
  } else {
    digitalWrite(IN1, LOW); // Đặt chân IN1 thấp
    digitalWrite(IN2, HIGH); // Đặt chân IN2 cao để động cơ lùi lại
    analogWrite(ENA, -PWM); // Đặt tốc độ bằng cách sử dụng PWM (giá trị tuyệt đối)
  }
}
void Motor2(int PWM) {
  if (PWM > 0) {
    digitalWrite(IN3, HIGH); // Đặt chân IN1 cao để động cơ tiến tới
    digitalWrite(IN4, LOW); // Đặt chân IN2 thấp
    analogWrite(ENB, PWM); // Đặt tốc độ bằng cách sử dụng PWM
  } else {
    digitalWrite(IN3, LOW); // Đặt chân IN1 thấp
    digitalWrite(IN4, HIGH); // Đặt chân IN2 cao để động cơ lùi lại
    analogWrite(ENB, -PWM); // Đặt tốc độ bằng cách sử dụng PWM (giá trị tuyệt đối)
  }
}
