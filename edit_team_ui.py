# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_team.ui'
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

class Ui_Edit_team(object):
    def setupUi(self, Edit_team):
        if not Edit_team.objectName():
            Edit_team.setObjectName(u"Edit_team")
        Edit_team.resize(459, 436)
        Edit_team.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.widget = QWidget(Edit_team)
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
        self.Title_Label_Pilot = QLabel(self.widget)
        self.Title_Label_Pilot.setObjectName(u"Title_Label_Pilot")
        self.Title_Label_Pilot.setGeometry(QRect(120, 0, 71, 21))
        self.Title_Label_Pilot.setAlignment(Qt.AlignCenter)
        self.id_pilot_label = QLabel(self.widget)
        self.id_pilot_label.setObjectName(u"id_pilot_label")
        self.id_pilot_label.setGeometry(QRect(10, 50, 101, 21))
        self.id_pilot_label.setAlignment(Qt.AlignCenter)
        self.comandir_label = QLabel(self.widget)
        self.comandir_label.setObjectName(u"comandir_label")
        self.comandir_label.setGeometry(QRect(10, 90, 111, 21))
        self.comandir_label.setAlignment(Qt.AlignCenter)
        self.help_commandir_label = QLabel(self.widget)
        self.help_commandir_label.setObjectName(u"help_commandir_label")
        self.help_commandir_label.setGeometry(QRect(10, 130, 171, 21))
        self.help_commandir_label.setAlignment(Qt.AlignCenter)
        self.count_team_label = QLabel(self.widget)
        self.count_team_label.setObjectName(u"count_team_label")
        self.count_team_label.setGeometry(QRect(10, 170, 121, 21))
        self.count_team_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_pilot_0 = QLineEdit(self.widget)
        self.lineEdit_id_pilot_0.setObjectName(u"lineEdit_id_pilot_0")
        self.lineEdit_id_pilot_0.setGeometry(QRect(200, 50, 113, 21))
        self.lineEdit_count_team_3 = QLineEdit(self.widget)
        self.lineEdit_count_team_3.setObjectName(u"lineEdit_count_team_3")
        self.lineEdit_count_team_3.setGeometry(QRect(200, 170, 113, 21))
        self.lineEdit_help_commandir_2 = QLineEdit(self.widget)
        self.lineEdit_help_commandir_2.setObjectName(u"lineEdit_help_commandir_2")
        self.lineEdit_help_commandir_2.setGeometry(QRect(200, 130, 113, 21))
        self.lineEdit_comandir_1 = QLineEdit(self.widget)
        self.lineEdit_comandir_1.setObjectName(u"lineEdit_comandir_1")
        self.lineEdit_comandir_1.setGeometry(QRect(200, 90, 113, 21))
        self.send_edit_team = QPushButton(self.widget)
        self.send_edit_team.setObjectName(u"send_edit_team")
        self.send_edit_team.setGeometry(QRect(110, 280, 171, 30))
        self.send_edit_team.setMinimumSize(QSize(0, 30))
        self.send_edit_team.setStyleSheet(u"background-image: url();")

        self.retranslateUi(Edit_team)

        QMetaObject.connectSlotsByName(Edit_team)
    # setupUi

    def retranslateUi(self, Edit_team):
        Edit_team.setWindowTitle(QCoreApplication.translate("Edit_team", u"Edit Info", None))
        self.Title_Label_Pilot.setText(QCoreApplication.translate("Edit_team", u"\u042d\u043a\u0438\u043f\u0430\u0436", None))
        self.id_pilot_label.setText(QCoreApplication.translate("Edit_team", u"id_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))
        self.comandir_label.setText(QCoreApplication.translate("Edit_team", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0438\u0440", None))
        self.help_commandir_label.setText(QCoreApplication.translate("Edit_team", u"\u041f\u043e\u043c\u043e\u0448\u043d\u0438\u043a_\u043a\u043e\u043c\u0430\u043d\u0434\u0438\u0440\u0430", None))
        self.count_team_label.setText(QCoreApplication.translate("Edit_team", u"\u041a\u043e\u043b\u0412\u043e_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))
        self.send_edit_team.setText(QCoreApplication.translate("Edit_team", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

