# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_people.ui'
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

class Ui_edit_people(object):
    def setupUi(self, edit_people):
        if not edit_people.objectName():
            edit_people.setObjectName(u"edit_people")
        edit_people.resize(459, 436)
        edit_people.setMinimumSize(QSize(459, 436))
        edit_people.setMaximumSize(QSize(459, 436))
        edit_people.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.widget = QWidget(edit_people)
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
        self.Title_Label_People = QLabel(self.widget)
        self.Title_Label_People.setObjectName(u"Title_Label_People")
        self.Title_Label_People.setGeometry(QRect(70, 0, 121, 21))
        self.Title_Label_People.setAlignment(Qt.AlignCenter)
        self.id_people_label = QLabel(self.widget)
        self.id_people_label.setObjectName(u"id_people_label")
        self.id_people_label.setGeometry(QRect(10, 50, 111, 21))
        self.id_people_label.setAlignment(Qt.AlignCenter)
        self.familuia_label = QLabel(self.widget)
        self.familuia_label.setObjectName(u"familuia_label")
        self.familuia_label.setGeometry(QRect(10, 90, 111, 21))
        self.familuia_label.setAlignment(Qt.AlignCenter)
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 130, 111, 21))
        self.name_label.setAlignment(Qt.AlignCenter)
        self.status_label = QLabel(self.widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(10, 170, 111, 21))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_people_0 = QLineEdit(self.widget)
        self.lineEdit_id_people_0.setObjectName(u"lineEdit_id_people_0")
        self.lineEdit_id_people_0.setGeometry(QRect(150, 50, 113, 21))
        self.lineEdit_status_3 = QLineEdit(self.widget)
        self.lineEdit_status_3.setObjectName(u"lineEdit_status_3")
        self.lineEdit_status_3.setGeometry(QRect(150, 170, 113, 21))
        self.lineEdit_name_2 = QLineEdit(self.widget)
        self.lineEdit_name_2.setObjectName(u"lineEdit_name_2")
        self.lineEdit_name_2.setGeometry(QRect(150, 130, 113, 21))
        self.lineEdit_familuia_1 = QLineEdit(self.widget)
        self.lineEdit_familuia_1.setObjectName(u"lineEdit_familuia_1")
        self.lineEdit_familuia_1.setGeometry(QRect(150, 90, 113, 21))
        self.send_edit_tiket = QPushButton(self.widget)
        self.send_edit_tiket.setObjectName(u"send_edit_tiket")
        self.send_edit_tiket.setGeometry(QRect(110, 280, 171, 30))
        self.send_edit_tiket.setMinimumSize(QSize(0, 30))
        self.send_edit_tiket.setStyleSheet(u"background-image: url();")

        self.retranslateUi(edit_people)

        QMetaObject.connectSlotsByName(edit_people)
    # setupUi

    def retranslateUi(self, edit_people):
        edit_people.setWindowTitle(QCoreApplication.translate("edit_people", u"Edit Info", None))
        self.Title_Label_People.setText(QCoreApplication.translate("edit_people", u"\u041f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u044b", None))
        self.id_people_label.setText(QCoreApplication.translate("edit_people", u"id_\u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430", None))
        self.familuia_label.setText(QCoreApplication.translate("edit_people", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.name_label.setText(QCoreApplication.translate("edit_people", u"\u0418\u043c\u044f", None))
        self.status_label.setText(QCoreApplication.translate("edit_people", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.send_edit_tiket.setText(QCoreApplication.translate("edit_people", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

