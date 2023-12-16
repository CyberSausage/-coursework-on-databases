# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_reis_stop.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Edit_reis_stop(object):
    def setupUi(self, Edit_reis_stop):
        if not Edit_reis_stop.objectName():
            Edit_reis_stop.setObjectName(u"Edit_reis_stop")
        Edit_reis_stop.resize(459, 410)
        Edit_reis_stop.setMinimumSize(QSize(459, 400))
        Edit_reis_stop.setMaximumSize(QSize(459, 436))
        Edit_reis_stop.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.widget = QWidget(Edit_reis_stop)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 401, 381))
        self.widget.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(44, 49, 58);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"	color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLabel{\n"
"	background-color: rgb(44, 49, 58);\n"
"	color: white; \n"
"	font-size: 15px; \n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	text-align: center;\n"
"}\n"
"QPushButton{\n"
"	background-color:  rgb(52, 59, 72);\n"
"	color: white; \n"
"	font-size: 15px; \n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	text-align: center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 25"
                        "5, 255);\n"
"}")
        self.Title_Label_Reis_Stop = QLabel(self.widget)
        self.Title_Label_Reis_Stop.setObjectName(u"Title_Label_Reis_Stop")
        self.Title_Label_Reis_Stop.setGeometry(QRect(60, 20, 181, 21))
        self.Title_Label_Reis_Stop.setAlignment(Qt.AlignCenter)
        self.why_label = QLabel(self.widget)
        self.why_label.setObjectName(u"why_label")
        self.why_label.setGeometry(QRect(10, 110, 91, 21))
        self.why_label.setAlignment(Qt.AlignCenter)
        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(10, 150, 91, 21))
        self.time_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_time_2 = QLineEdit(self.widget)
        self.lineEdit_time_2.setObjectName(u"lineEdit_time_2")
        self.lineEdit_time_2.setGeometry(QRect(150, 150, 113, 21))
        self.lineEdit_why_1 = QLineEdit(self.widget)
        self.lineEdit_why_1.setObjectName(u"lineEdit_why_1")
        self.lineEdit_why_1.setGeometry(QRect(150, 110, 113, 21))
        self.send_edit_tiket = QPushButton(self.widget)
        self.send_edit_tiket.setObjectName(u"send_edit_tiket")
        self.send_edit_tiket.setGeometry(QRect(80, 230, 171, 30))
        self.send_edit_tiket.setMinimumSize(QSize(0, 30))
        self.send_edit_tiket.setStyleSheet(u"background-image: url();")
        self.id_reis_label = QLabel(self.widget)
        self.id_reis_label.setObjectName(u"id_reis_label")
        self.id_reis_label.setGeometry(QRect(10, 70, 91, 21))
        self.id_reis_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_reis_0 = QLineEdit(self.widget)
        self.lineEdit_id_reis_0.setObjectName(u"lineEdit_id_reis_0")
        self.lineEdit_id_reis_0.setGeometry(QRect(150, 70, 113, 21))

        self.retranslateUi(Edit_reis_stop)

        QMetaObject.connectSlotsByName(Edit_reis_stop)
    # setupUi

    def retranslateUi(self, Edit_reis_stop):
        Edit_reis_stop.setWindowTitle(QCoreApplication.translate("Edit_reis_stop", u"Edit Info", None))
        self.Title_Label_Reis_Stop.setText(QCoreApplication.translate("Edit_reis_stop", u"\u0417\u0430\u0434\u0435\u0440\u0436\u0430\u043d\u043d\u044b\u0435_\u0440\u0435\u0439\u0441\u044b", None))
        self.why_label.setText(QCoreApplication.translate("Edit_reis_stop", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430", None))
        self.time_label.setText(QCoreApplication.translate("Edit_reis_stop", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.send_edit_tiket.setText(QCoreApplication.translate("Edit_reis_stop", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.id_reis_label.setText(QCoreApplication.translate("Edit_reis_stop", u"id_\u0440\u0435\u0439\u0441\u0430", None))
    # retranslateUi

