# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BAOCAOTHTZDgsr.ui'
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
        MainWindow.resize(977, 623)
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
        self.groupBox_2.setGeometry(QRect(10, 140, 851, 231))
        self.groupBox_2.setFont(font)
        self.splitter_2 = QSplitter(self.groupBox_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(30, 40, 291, 71))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.LED1_on = QPushButton(self.splitter_2)
        self.LED1_on.setObjectName(u"LED1_on")
        self.LED1_on.setFont(font)
        self.splitter_2.addWidget(self.LED1_on)
        self.LED1_off = QPushButton(self.splitter_2)
        self.LED1_off.setObjectName(u"LED1_off")
        self.LED1_off.setFont(font)
        self.splitter_2.addWidget(self.LED1_off)
        self.splitter_3 = QSplitter(self.groupBox_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(30, 120, 291, 71))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.LED2_on = QPushButton(self.splitter_3)
        self.LED2_on.setObjectName(u"LED2_on")
        self.LED2_on.setFont(font)
        self.splitter_3.addWidget(self.LED2_on)
        self.LED2_off = QPushButton(self.splitter_3)
        self.LED2_off.setObjectName(u"LED2_off")
        self.LED2_off.setFont(font)
        self.splitter_3.addWidget(self.LED2_off)
        self.LED1 = QLabel(self.groupBox_2)
        self.LED1.setObjectName(u"LED1")
        self.LED1.setGeometry(QRect(360, 40, 71, 71))
        self.LED2 = QLabel(self.groupBox_2)
        self.LED2.setObjectName(u"LED2")
        self.LED2.setGeometry(QRect(360, 120, 71, 71))
        self.output_console = QListView(self.centralwidget)
        self.output_console.setObjectName(u"listView")
        self.output_console.setGeometry(QRect(10, 380, 851, 161))
        self.output_console.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 977, 26))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"LED Status", None))
        self.LED1_on.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.LED1_off.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.LED2_on.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.LED2_off.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.LED1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LED2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

class ConsoleMainWindow(QMainWindow):
    def __init__(self):
        global img_on_pixmap, img_off_pixmap
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LED1_on.clicked.connect(self.led1_status_on)
        self.ui.LED1_off.clicked.connect(self.led1_status_off)
        self.ui.LED2_on.clicked.connect(self.led2_status_on)
        self.ui.LED2_off.clicked.connect(self.led2_status_off)
        self.ui.Connect.clicked.connect(self.connect_button_clicked)
        self.ui.Disconnect.clicked.connect(self.disconnect_button_clicked)
        img_on_path = "F://Code//GUI//Python//led-green-black.png"
        img_off_path = "F://Code//GUI//Python//768px-Red_Light_Icon.svg.png"
        img_on_pixmap = QPixmap(img_on_path).scaled(self.ui.LED1.size(), Qt.KeepAspectRatio)
        img_off_pixmap = QPixmap(img_off_path).scaled(self.ui.LED2.size(), Qt.KeepAspectRatio)
        self.ui.LED1.setPixmap(img_off_pixmap)
        self.ui.LED2.setPixmap(img_off_pixmap)
        self.model = QStandardItemModel()
        self.ui.output_console.setModel(self.model)
        self.update_port_list()
    def led1_status_on(self):
        print('led 1 turning on')
        ser.write("02-01".encode('utf-8'))
        self.ui.LED1.setPixmap(img_on_pixmap)
    def led1_status_off(self):
        print('led 1 turning off')
        ser.write("02-00".encode('utf-8'))
        self.ui.LED1.setPixmap(img_off_pixmap)
    def led2_status_on(self):
        print('led 2 turning on')
        ser.write("32-01".encode('utf-8'))
        self.ui.LED2.setPixmap(img_on_pixmap)
    def led2_status_off(self):
        print('led 2 turning off')
        ser.write("32-00".encode('utf-8'))
        self.ui.LED2.setPixmap(img_off_pixmap)
    def update_status(self, message):
        now = datetime.now()
        current = now.strftime("%H:%M:%S")
        message = f"[{current}]: {message}"
        item =  QStandardItem(message)
        self.model.insertRow(0, item)
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
    def read_from_serial(self,com_port):
        try:
            while ser.is_open:
                # Đọc dữ liệu từ cổng serial
                data = ser.readline().decode('utf-8').rstrip()
                if data:
                    self.update_status(f"Dữ liệu nhận được: {data}")     
        except serial.SerialException as e:
            print(f"Không thể kết nối tới cổng {com_port}: {e}")
    def disconnect_to_com_port(self, comport):
        try:
            if comport is not None:
                ser.close()
                self.update_status(f"Đã ngắt kết nối đến cổng COM: {comport}")
            else:
                self.update_status("Không có kết nối COM nào để ngắt.")
        except serial.SerialException as e:
            self.update_status(f"Lỗi khi ngắt kết nối đến cổng COM: {e}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = ConsoleMainWindow()
    mainwin.show()
    sys.exit(app.exec_())
