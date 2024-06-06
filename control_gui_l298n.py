# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BAITAP5EOqFaZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import serial.tools.list_ports
from threading import Thread
from datetime import datetime
from serial import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(927, 1137)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 30, 851, 101))
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(70, 40, 731, 51))
        self.splitter.setOrientation(Qt.Horizontal)
        self.port_select = QComboBox(self.splitter)
        self.port_select.setObjectName(u"port_select")
        self.splitter.addWidget(self.port_select)
        self.Connect = QPushButton(self.splitter)
        self.Connect.setObjectName(u"Connect")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(12)
        self.Connect.setFont(font1)
        self.splitter.addWidget(self.Connect)
        self.Disconnect = QPushButton(self.splitter)
        self.Disconnect.setObjectName(u"Disconnect")
        self.Disconnect.setFont(font)
        self.splitter.addWidget(self.Disconnect)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 140, 851, 261))
        self.groupBox_2.setFont(font)
        self.splitter_2 = QSplitter(self.groupBox_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(70, 50, 381, 51))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.splitter_2.addWidget(self.label)
        self.pwm_in = QTextEdit(self.splitter_2)
        self.pwm_in.setObjectName(u"pwm_in")
        self.pwm_in.setEnabled(True)
        self.pwm_in.setReadOnly(False)
        self.splitter_2.addWidget(self.pwm_in)
        self.splitter_3 = QSplitter(self.groupBox_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(70, 190, 381, 51))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.pushButton = QPushButton(self.splitter_3)
        self.pushButton.setObjectName(u"pushButton")
        self.splitter_3.addWidget(self.pushButton)
        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(70, 140, 381, 22))
        self.horizontalSlider.setMinimum(-255)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(509, 49, 311, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DC1 = QCheckBox(self.horizontalLayoutWidget)
        self.DC1.setObjectName(u"DC1")

        self.horizontalLayout.addWidget(self.DC1)

        self.DC2 = QCheckBox(self.horizontalLayoutWidget)
        self.DC2.setObjectName(u"DC2")

        self.horizontalLayout.addWidget(self.DC2)

        self.output_console = QListView(self.centralwidget)
        self.output_console.setObjectName(u"output_console")
        self.output_console.setGeometry(QRect(10, 430, 851, 161))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 927, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Connection Terminal", None))
        self.port_select.setPlaceholderText("")
        self.Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.Disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"DATA TRANSMITTER TERMINAL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PWM", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Pluse", None))
        self.DC1.setText(QCoreApplication.translate("MainWindow", u"DC1", None))
        self.DC2.setText(QCoreApplication.translate("MainWindow", u"DC2", None))
    # retranslateUi

class ConsoleMainWindow(QMainWindow):
    def __init__(self):
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.ui.output_console.setModel(self.model)
        self.ui.Connect.clicked.connect(self.connect_button_clicked)
        self.ui.Disconnect.clicked.connect(self.disconnect_button_clicked)
        self.ui.pushButton.clicked.connect(self.write_to_serial)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_changed)
        self.update_port_list()
    def slider_value_changed(self, value):
        self.ui.pwm_in.setText(str(value))
    def update_port_list(self):
        # Xóa các mục cũ trong port_select trước khi cập nhật danh sách cổng COM mới
        self.ui.port_select.clear()
        # Lấy danh sách các cổng COM hiện có
        ports = serial.tools.list_ports.comports()
        print(ports)
        # Thêm các cổng COM vào port_select
        for port in ports:
            self.ui.port_select.addItem(port.device)
    def connect_button_clicked(self):
        # Lấy cổng COM được chọn từ port_select
        selected_port = self.ui.port_select.currentText()
        if selected_port:
            self.update_status(f"Đang thiết lập kết nối đến cổng: {selected_port}")
            self.connect_to_com_port(com_port=selected_port)
        else:
            self.update_status("Không có cổng COM nào được chọn.")
    def disconnect_button_clicked(self):
        # Lấy cổng COM được chọn từ port_select
        selected_port = self.ui.port_select.currentText()
        if selected_port:
            self.update_status(f"Đang ngắt kết nối đến cổng: {selected_port}")
            self.disconnect_to_com_port(comport=selected_port)
        else:
            self.update_status("Không có cổng COM nào được chọn.")
    def connect_to_com_port(self, com_port):
        global ser
        try:
            # Mở kết nối đến cổng COM được chỉ định
            ser = serial.Serial(com_port, baudrate=115200)
            # Kiểm tra nếu kết nối thành công
            if ser.is_open:
                self.update_status(f"Đã kết nối thành công đến cổng {com_port}")
                # Thực hiện các thao tác khác tại đây nếu cần
                self.read_thread = Thread(target=self.read_from_serial, args=(com_port,))
                self.read_thread.start()
            else:
                self.update_status("Không thể kết nối đến cổng COM.")
                return False, None
        except serial.SerialException as e:
            self.update_status(f"Lỗi khi kết nối đến cổng COM: {e}")
            return False, None
    def read_from_serial(self,comport):
        try:
            while ser.is_open:
                # Đọc dữ liệu từ cổng serial
                data = ser.readline().decode('utf-8').rstrip()
                if data:
                    self.update_status(f"Dữ liệu nhận được: {data}")     
        except serial.SerialException as e:
            print(f"Không thể kết nối tới cổng {comport}: {e}")
    def write_to_serial(self):
        try:
            if ser.is_open:
                buffer = self.ui.pwm_in.toPlainText().strip()
                try:
                    value = int(buffer)
                    if self.ui.DC1.isChecked() == True:
                        en1 = '1'
                    else:
                        en1 = '0'
                    if self.ui.DC2.isChecked() == True:
                        en2 = '1'
                    else:
                        en2 = '0'
                    if -255 <= value <= 255:
                        data = en1+en2+buffer
                        self.update_status(f"du lieu gui: {data}")
                        ser.write(data.encode())
                        self.update_status(f"Đã gửi thành công {len(data)} byte")
                    else:
                        self.update_status(f"Dữ liệu không hợp lệ: {data}. Vui lòng nhập giá trị trong khoảng -255 đến 255.")
                except ValueError:
                    self.update_status("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")
        except serial.SerialException as e:
            self.update_status(f"Không thể kết nối, lỗi: {e}")
    def disconnect_to_com_port(self, comport):
        try:
            if comport is not None:
                ser.close()
                self.update_status(f"Đã ngắt kết nối đến cổng COM: {comport}")
            else:
                self.update_status("Không có kết nối COM nào để ngắt.")
        except serial.SerialException as e:
            self.update_status(f"Lỗi khi ngắt kết nối đến cổng COM: {e}")
    def update_status(self, message):
        now = datetime.now()
        current = now.strftime("%H:%M:%S")
        message = f"[{current}]: {message}"
        item =  QStandardItem(message)
        self.model.insertRow(0, item)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = ConsoleMainWindow()
    mainwin.show()
    sys.exit(app.exec_())