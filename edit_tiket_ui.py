# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_tiket.ui'
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

class Ui_Edit_tiket(object):
    def setupUi(self, Edit_tiket):
        if not Edit_tiket.objectName():
            Edit_tiket.setObjectName(u"Edit_tiket")
        Edit_tiket.resize(459, 436)
        Edit_tiket.setMinimumSize(QSize(459, 436))
        Edit_tiket.setMaximumSize(QSize(459, 436))
        Edit_tiket.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.widget = QWidget(Edit_tiket)
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
        self.Title_Label_Tiket = QLabel(self.widget)
        self.Title_Label_Tiket.setObjectName(u"Title_Label_Tiket")
        self.Title_Label_Tiket.setGeometry(QRect(90, 0, 71, 21))
        self.Title_Label_Tiket.setAlignment(Qt.AlignCenter)
        self.id_tiket_label = QLabel(self.widget)
        self.id_tiket_label.setObjectName(u"id_tiket_label")
        self.id_tiket_label.setGeometry(QRect(10, 50, 91, 21))
        self.id_tiket_label.setAlignment(Qt.AlignCenter)
        self.number_tiket_label = QLabel(self.widget)
        self.number_tiket_label.setObjectName(u"number_tiket_label")
        self.number_tiket_label.setGeometry(QRect(10, 90, 111, 21))
        self.number_tiket_label.setAlignment(Qt.AlignCenter)
        self.prise_tiket_label = QLabel(self.widget)
        self.prise_tiket_label.setObjectName(u"prise_tiket_label")
        self.prise_tiket_label.setGeometry(QRect(10, 130, 101, 21))
        self.prise_tiket_label.setAlignment(Qt.AlignCenter)
        self.id_reis_label = QLabel(self.widget)
        self.id_reis_label.setObjectName(u"id_reis_label")
        self.id_reis_label.setGeometry(QRect(10, 170, 91, 21))
        self.id_reis_label.setAlignment(Qt.AlignCenter)
        self.id_people_label = QLabel(self.widget)
        self.id_people_label.setObjectName(u"id_people_label")
        self.id_people_label.setGeometry(QRect(10, 210, 101, 21))
        self.id_people_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_tiket_0 = QLineEdit(self.widget)
        self.lineEdit_id_tiket_0.setObjectName(u"lineEdit_id_tiket_0")
        self.lineEdit_id_tiket_0.setGeometry(QRect(150, 50, 113, 21))
        self.lineEdit_id_reis_3 = QLineEdit(self.widget)
        self.lineEdit_id_reis_3.setObjectName(u"lineEdit_id_reis_3")
        self.lineEdit_id_reis_3.setGeometry(QRect(150, 170, 113, 21))
        self.lineEdit_prise_tiket_2 = QLineEdit(self.widget)
        self.lineEdit_prise_tiket_2.setObjectName(u"lineEdit_prise_tiket_2")
        self.lineEdit_prise_tiket_2.setGeometry(QRect(150, 130, 113, 21))
        self.lineEdit_number_tiket_1 = QLineEdit(self.widget)
        self.lineEdit_number_tiket_1.setObjectName(u"lineEdit_number_tiket_1")
        self.lineEdit_number_tiket_1.setGeometry(QRect(150, 90, 113, 21))
        self.lineEdit_id_people_4 = QLineEdit(self.widget)
        self.lineEdit_id_people_4.setObjectName(u"lineEdit_id_people_4")
        self.lineEdit_id_people_4.setGeometry(QRect(150, 210, 113, 21))
        self.send_edit_tiket = QPushButton(self.widget)
        self.send_edit_tiket.setObjectName(u"send_edit_tiket")
        self.send_edit_tiket.setGeometry(QRect(110, 280, 171, 30))
        self.send_edit_tiket.setMinimumSize(QSize(0, 30))
        self.send_edit_tiket.setStyleSheet(u"background-image: url();")

        self.retranslateUi(Edit_tiket)

        QMetaObject.connectSlotsByName(Edit_tiket)
    # setupUi

    def retranslateUi(self, Edit_tiket):
        Edit_tiket.setWindowTitle(QCoreApplication.translate("Edit_tiket", u"Edit Info", None))
        self.Title_Label_Tiket.setText(QCoreApplication.translate("Edit_tiket", u"\u0411\u0438\u043b\u0435\u0442\u044b", None))
        self.id_tiket_label.setText(QCoreApplication.translate("Edit_tiket", u"id_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.number_tiket_label.setText(QCoreApplication.translate("Edit_tiket", u"\u041d\u043e\u043c\u0435\u0440_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.prise_tiket_label.setText(QCoreApplication.translate("Edit_tiket", u"\u0426\u0435\u043d\u0430_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.id_reis_label.setText(QCoreApplication.translate("Edit_tiket", u"id_\u0440\u0435\u0439\u0441\u0430", None))
        self.id_people_label.setText(QCoreApplication.translate("Edit_tiket", u"id_\u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430", None))
        self.send_edit_tiket.setText(QCoreApplication.translate("Edit_tiket", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

