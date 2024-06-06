# BAI TAP THUC HANH CAM BIEN VA CO CAU CHAP HANH
# BAI LM35
# PHIEN BAN: 10
# NGUYEN THANH NHAN-2286301149

import os
import sys
import serial.tools.list_ports
import random
import csv
import numpy as np
import matplotlib.pyplot as plt
from threading import Thread
from datetime import datetime
from serial import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 865)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 1011, 161))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 40, 961, 42))
        self.splitter.setOrientation(Qt.Horizontal)
        self.comport_select = QComboBox(self.splitter)
        self.comport_select.setObjectName(u"comport_select")
        self.splitter.addWidget(self.comport_select)
        self.connect_button = QPushButton(self.splitter)
        self.connect_button.setObjectName(u"connect_button")
        self.splitter.addWidget(self.connect_button)
        self.disconnect_button = QPushButton(self.splitter)
        self.disconnect_button.setObjectName(u"disconnect_button")
        self.splitter.addWidget(self.disconnect_button)
        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(20, 100, 961, 41))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.path_file = QPlainTextEdit(self.splitter_2)
        self.path_file.setObjectName(u"path_file")
        self.splitter_2.addWidget(self.path_file)
        self.write_button = QPushButton(self.splitter_2)
        self.write_button.setObjectName(u"write_button")
        self.splitter_2.addWidget(self.write_button)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 190, 751, 121))
        self.groupBox_2.setFont(font)
        self.pin13ledlabel = QLabel(self.groupBox_2)
        self.pin13ledlabel.setObjectName(u"pin13ledlabel")
        self.pin13ledlabel.setGeometry(QRect(10, 70, 161, 31))
        self.pin13ledlabel.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 50, 71, 71))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 70, 241, 41))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 751, 121))
        self.groupBox_3.setFont(font)
        self.pin13ledlabel_2 = QLabel(self.groupBox_3)
        self.pin13ledlabel_2.setObjectName(u"pin13ledlabel_2")
        self.pin13ledlabel_2.setGeometry(QRect(10, 70, 161, 31))
        self.pin13ledlabel_2.setAlignment(Qt.AlignCenter)
        self.led_pixmap = QLabel(self.groupBox_3)
        self.led_pixmap.setObjectName(u"led_pixmap")
        self.led_pixmap.setGeometry(QRect(190, 50, 71, 71))
        self.led_pixmap.setPixmap(QPixmap(u"F:/Code/GUI/Python/768px-Red_Light_Icon.svg.png"))
        self.led_pixmap.setScaledContents(True)
        self.led_pixmap.setAlignment(Qt.AlignCenter)
        self.convert_button = QPushButton(self.groupBox_3)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setGeometry(QRect(340, 70, 241, 41))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 460, 1011, 351))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.status_monitor = QListView(self.tab)
        self.status_monitor.setObjectName(u"status_monitor")
        self.status_monitor.setGeometry(QRect(0, 10, 1001, 301))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 1001, 321))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 330, 1011, 121))
        self.groupBox_4.setFont(font)
        self.splitter_3 = QSplitter(self.groupBox_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(30, 50, 941, 51))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.celcius_label = QLabel(self.splitter_3)
        self.celcius_label.setObjectName(u"celcius_label")
        self.splitter_3.addWidget(self.celcius_label)
        self.celcius_text = QTextEdit(self.splitter_3)
        self.celcius_text.setObjectName(u"celcius_text")
        self.celcius_text.setReadOnly(True)
        self.splitter_3.addWidget(self.celcius_text)
        self.celcius_label_sensor2 = QLabel(self.splitter_3)
        self.celcius_label_sensor2.setObjectName(u"celcius_label_sensor2")
        self.splitter_3.addWidget(self.celcius_label_sensor2)
        self.celcius_text_sensor2 = QTextEdit(self.splitter_3)
        self.celcius_text_sensor2.setObjectName(u"celcius_text_sensor2")
        self.celcius_text_sensor2.setReadOnly(True)
        self.splitter_3.addWidget(self.celcius_text_sensor2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1052, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CONNECTION AND DATA STORAGE TERMINAL", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.disconnect_button.setText(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
        self.write_button.setText(QCoreApplication.translate("MainWindow", u"SAVE FILE", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"LED PREFERENCE AND TOGGLE BUTTON TERMINAL", None))
        self.pin13ledlabel.setText(QCoreApplication.translate("MainWindow", u"PIN 13 LED", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert to F", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"LED PREFERENCE AND TOGGLE BUTTON TERMINAL", None))
        self.pin13ledlabel_2.setText(QCoreApplication.translate("MainWindow", u"PIN 13 LED", None))
        self.led_pixmap.setText("")
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert to F", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"TERMINAL MONITOR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"GRAPH PLOT", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"DATA RECEIVE TERMINAL", None))
        self.celcius_label.setText(QCoreApplication.translate("MainWindow", u"SEN1 °C DEGREE", None))
        self.celcius_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.celcius_label_sensor2.setText(QCoreApplication.translate("MainWindow", u"SEN2 °C DEGREE", None))
    # retranslateUi


class ConsoleMainWindow(QMainWindow):
    global arr1, arr2, timeline
    arr1 = []
    arr2 = []
    timeline = []
    data_received = Signal(str)
    def __init__(self):
        global img_on_path, img_off_path, toggle, en_write
        toggle = False
        en_write = False
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # thiet lap trang thai ban dau cua led tren gui
        img_on_path = "F://Code//GUI//Python//led-green-black.png"
        img_off_path = "F://Code//GUI//Python//768px-Red_Light_Icon.svg.png"
        self.ui.led_pixmap.setPixmap(QPixmap(img_off_path))
        self.hopthoai = QStandardItemModel()
        self.ui.status_monitor.setModel(self.hopthoai)
        self.ui.connect_button.clicked.connect(self.connect_button_clicked)
        self.ui.disconnect_button.clicked.connect(self.disconnect_button_clicked)
        self.ui.write_button.clicked.connect(self.save_button_clicked)
        self.ui.convert_button.clicked.connect(self.toggle_celcius)
        self.data_received.connect(self.update_text)
        self.update_port_list()
        self.create_file_data()
        # Create a figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        # Add canvas to layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.ui.label_5.setLayout(layout)
    def toggle_celcius(self):
        global toggle
        if toggle == True:
            toggle = False
            self.ui.celcius_label.setText(QCoreApplication.translate("MainWindow", u"SEN1 °C DEGREE", None))
            self.ui.celcius_label_sensor2.setText(QCoreApplication.translate("MainWindow", u"SEN2 °C DEGREE", None))
            self.ui.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert to °F ", None))
        else:
            toggle = True
            self.ui.celcius_label.setText(QCoreApplication.translate("MainWindow", u"SEN1 °F DEGREE", None))
            self.ui.celcius_label_sensor2.setText(QCoreApplication.translate("MainWindow", u"SEN2 °F DEGREE", None))
            self.ui.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert to °C ", None))
    def led_status(self, status):
        # dieu khien trang thai led tren gui khi nhan duoc tin hieu
        if status == True:
            self.ui.led_pixmap.setPixmap(QPixmap(img_on_path))
        elif status == False:
            self.ui.led_pixmap.setPixmap(QPixmap(img_off_path))
    def update_status(self, message,direction):
        # gui tin nhan len hop thoai
        now = datetime.now()
        current = now.strftime("%H:%M:%S")
        message = f"[{current}] [{direction}]: {message}"
        item = QStandardItem(message)
        self.hopthoai.insertRow(0, item)
    def update_port_list(self):
        # hien thi cac cong COM dang hoat dong
        self.ui.comport_select.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.comport_select.addItem(port.device)
    def connect_button_clicked(self):
        select_port = self.ui.comport_select.currentText()
        if select_port:
            self.update_status(f"Dang thiet lap ket noi den {select_port}.", "SYSTEM")
            self.connect_to_com_port(com_port=select_port)
        else:
            self.update_status("Không có cổng COM nào được chọn.", "SYSTEM")
    def disconnect_button_clicked(self):
        # Lấy cổng COM được chọn từ port_select
        selected_port = self.ui.comport_select.currentText()
        if selected_port:
            self.update_status(f"Đang ngắt kết nối đến cổng: {selected_port}", "SYSTEM")
            self.disconnect_to_com_port(comport=selected_port)
        else:
            self.update_status("Không có cổng COM nào được chọn.", "SYSTEM")
        if os.path.exists(file_path):
            self.update_status(f"Ghi file thành công, file {file_name}", "SYSTEM")
        else:
            self.update_status(f"Không có file nào được ghi", "SYSTEM")
    def disconnect_to_com_port(self, comport):
        try:
            if comport is not None:
                ser.close()
                self.update_status(f"Đã ngắt kết nối đến cổng COM: {comport}", "SYSTEM")
                self.ui.celcius_text.clear()
                self.ui.celcius_text_sensor2.clear()
            else:
                self.update_status("Không có kết nối COM nào để ngắt.", "SYSTEM")
        except serial.SerialException as e:
            self.update_status(f"Lỗi khi ngắt kết nối đến cổng COM: {e}", "SYSTEM")
    def connect_to_com_port(self, com_port):
        global ser
        try:
            # Mở kết nối đến cổng COM được chỉ định
            ser = serial.Serial(com_port, baudrate=115200)
            # Kiểm tra nếu kết nối thành công
            if ser.is_open:
                self.update_status(f"Đã kết nối thành công đến cổng {com_port}", "SYSTEM")
                # Thực hiện các thao tác khác tại đây nếu cần
                self.read_thread = Thread(target=self.read_from_serial, args=(com_port,))
                self.read_thread.start()
            else:
                self.update_status("Không thể kết nối đến cổng COM.")
                return False, None
        except serial.SerialException as e:
            self.update_status(f"Lỗi khi kết nối đến cổng COM: {e}", "SYSTEM")
            return False, None
    def read_from_serial(self,com_port):
        try:
            while ser.is_open:
                # Đọc dữ liệu từ cổng serial
                data = ser.readline().decode('utf-8')
                self.data_received.emit(data)
                if data:
                    pass 
                else:
                    self.update_status("Không có dữ liệu gửi đến","SYSTEM")
        except serial.SerialException as e:
            self.update_status(f"Không thể kết nối tới cổng {com_port}: {e}", "SYSTEM")
    def update_text(self, data):
        data = data.split(" ")
        if toggle == False:
            self.ui.celcius_text.setPlainText(str(data[0]))
            self.ui.celcius_text_sensor2.setPlainText(str(data[1]))
            self.plot_graph(data[0], data[1])
        else:
            self.ui.celcius_text.setPlainText(str(round((float(data[0])*9/5+32), 2)))
            self.ui.celcius_text_sensor2.setPlainText(str(round((float(data[1])*9/5+32), 2)))
            data1 = round(float(data[0])*9/5+32,2)
            data2 = round(float(data[1])*9/5+32,2)
            self.plot_graph(data1, data2)
        if (float(data[0]) > 30.0 or float(data[1]) > 30.0):
            self.led_status(True)
        else:
            self.led_status(False)
    def create_file_data(self):
        global file_path, file_name
        path = "F://Code//GUI//Python//lm35_data//"
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d-%H-%M-")
        file_name = f"data-{str(current_date) + str(random.randint(0,999))}.csv"
        file_path = path+file_name
        font2 = QFont()
        font2.setBold(False)
        font2.setPointSize(12)
        self.ui.path_file.setFont(font2)
        self.ui.path_file.setPlainText(file_name)
    def save_button_clicked(self):
        global en_write
        self.update_status(f"Bắt đầu ghi dữ liệu vào file {file_name}", "SYSTEM")
        en_write = True
    def writefle(self,timeline, data1, data2):
        try:
            if data1 is not None and data2 is not None:
                with(open(file_path, "+a") as file):
                    writer = csv.writer(file)
                    writer.writerow([timeline,data1,data2])
                    file.close
            else:
                self.update_status("Không có dữ liệu để ghi", "SYSTEM")
        except TypeError as e:
            self.update_status(f"Lỗi: {e}", "SYSTEM")
    def plot_graph(self, data1, data2):
        now = datetime.now()
        time = now.strftime("%M:%S")
        timeline.append(time)
        if en_write == True:
            if time != prev_time:
                self.writefle(time, data1, data2)
            prev_time = time
        arr1.append(data1)
        arr2.append(data2)
        if len(arr1) > 50:
            timeline.pop(0)
            arr1.pop(0)
            arr2.pop(0)
        self.ax.clear()
        self.ax.plot(timeline, arr1, marker=',', linestyle='-', color='tab:blue', label="LM35 Sensor No.1")
        self.ax.plot(timeline, arr2, marker=',', linestyle='-', color='tab:orange', label="LM35 Sensor No.2")
        self.ax.set_xlabel('Time (seconds)')
        self.ax.legend(loc="lower right")
        self.canvas.draw()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = ConsoleMainWindow()
    mainwin.show()
    sys.exit(app.exec_())