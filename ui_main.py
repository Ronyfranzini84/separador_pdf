# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'separador.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 448)
        MainWindow.setMinimumSize(QSize(500, 448))
        MainWindow.setMaximumSize(QSize(500, 448))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0852273 rgba(93, 0, 0, 243), stop:0.335227 rgba(170, 0, 0, 255), stop:0.545455 rgba(193, 0, 0, 243), stop:0.715909 rgba(200, 16, 16, 255), stop:0.914773 rgba(210, 62, 62, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0852273 rgba(93, 0, 0, 243), stop:0.335227 rgba(170, 0, 0, 255), stop:0.545455 rgba(193, 0, 0, 243), stop:0.715909 rgba(200, 16, 16, 255), stop:0.914773 rgba(210, 62, 62, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbl_tittle = QLabel(self.frame)
        self.lbl_tittle.setObjectName(u"lbl_tittle")
        self.lbl_tittle.setMaximumSize(QSize(156, 106))
        font = QFont()
        font.setKerning(True)
        self.lbl_tittle.setFont(font)
        self.lbl_tittle.setStyleSheet(u"alternate-background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.lbl_tittle.setTextFormat(Qt.AutoText)
        self.lbl_tittle.setPixmap(QPixmap(u"baianinho.png"))
        self.lbl_tittle.setScaledContents(True)
        self.lbl_tittle.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.lbl_tittle.setWordWrap(False)

        self.verticalLayout.addWidget(self.lbl_tittle, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0852273 rgba(93, 0, 0, 243), stop:0.335227 rgba(170, 0, 0, 255), stop:0.545455 rgba(193, 0, 0, 243), stop:0.715909 rgba(200, 16, 16, 255), stop:0.914773 rgba(210, 62, 62, 255));")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_path = QLineEdit(self.frame_2)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.txt_path.setFont(font1)
        self.txt_path.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_path.setAlignment(Qt.AlignCenter)
        self.txt_path.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 30))
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"    background-color:#c3c3c3;\n"
"    color:black; border: solid 0px;\n"
"    font: bold 14px \"Segoe UI\";\n"
"    border-top-right-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(227, 24, 54);\n"
"    color:#fff\n"
"}")

        self.horizontalLayout.addWidget(self.btn_open)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 30))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"    background-color:#c3c3c3;\n"
"    color:black;\n"
"    border: solid 0px;\n"
"    font: bold 14px \"Segoe UI\";\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(227, 24, 54);\n"
"    color:#fff\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.lbl_name = QLabel(self.frame)
        self.lbl_name.setObjectName(u"lbl_name")
        font2 = QFont()
        font2.setFamilies([u"MV Boli"])
        font2.setPointSize(16)
        self.lbl_name.setFont(font2)

        self.verticalLayout.addWidget(self.lbl_name)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_tittle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">DIVISOR DE PDF</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SELECIONE O PDF -->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"DIVISOR", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">Rony Franzini </span></p></body></html>", None))
    # retranslateUi

