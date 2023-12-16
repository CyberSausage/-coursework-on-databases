# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_reis.ui'
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

class Ui_edit_reis(object):
    def setupUi(self, edit_reis):
        if not edit_reis.objectName():
            edit_reis.setObjectName(u"edit_reis")
        edit_reis.resize(459, 539)
        edit_reis.setMinimumSize(QSize(459, 539))
        edit_reis.setMaximumSize(QSize(459, 539))
        edit_reis.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        self.widget = QWidget(edit_reis)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 401, 481))
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
        self.Title_Label_Reis = QLabel(self.widget)
        self.Title_Label_Reis.setObjectName(u"Title_Label_Reis")
        self.Title_Label_Reis.setGeometry(QRect(120, 0, 71, 21))
        self.Title_Label_Reis.setAlignment(Qt.AlignCenter)
        self.id_reis_label = QLabel(self.widget)
        self.id_reis_label.setObjectName(u"id_reis_label")
        self.id_reis_label.setGeometry(QRect(10, 50, 101, 21))
        self.id_reis_label.setAlignment(Qt.AlignCenter)
        self.numder_reis_label = QLabel(self.widget)
        self.numder_reis_label.setObjectName(u"numder_reis_label")
        self.numder_reis_label.setGeometry(QRect(10, 90, 111, 21))
        self.numder_reis_label.setAlignment(Qt.AlignCenter)
        self.point_start_label = QLabel(self.widget)
        self.point_start_label.setObjectName(u"point_start_label")
        self.point_start_label.setGeometry(QRect(10, 130, 151, 21))
        self.point_start_label.setAlignment(Qt.AlignCenter)
        self.point_finish_label = QLabel(self.widget)
        self.point_finish_label.setObjectName(u"point_finish_label")
        self.point_finish_label.setGeometry(QRect(10, 170, 141, 21))
        self.point_finish_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_reis_0 = QLineEdit(self.widget)
        self.lineEdit_id_reis_0.setObjectName(u"lineEdit_id_reis_0")
        self.lineEdit_id_reis_0.setGeometry(QRect(200, 50, 113, 21))
        self.lineEdit_point_finish_3 = QLineEdit(self.widget)
        self.lineEdit_point_finish_3.setObjectName(u"lineEdit_point_finish_3")
        self.lineEdit_point_finish_3.setGeometry(QRect(200, 170, 113, 21))
        self.lineEdit_point_start_2 = QLineEdit(self.widget)
        self.lineEdit_point_start_2.setObjectName(u"lineEdit_point_start_2")
        self.lineEdit_point_start_2.setGeometry(QRect(200, 130, 113, 21))
        self.lineEdit_numder_reis_1 = QLineEdit(self.widget)
        self.lineEdit_numder_reis_1.setObjectName(u"lineEdit_numder_reis_1")
        self.lineEdit_numder_reis_1.setGeometry(QRect(200, 90, 113, 21))
        self.send_edit_team = QPushButton(self.widget)
        self.send_edit_team.setObjectName(u"send_edit_team")
        self.send_edit_team.setGeometry(QRect(110, 450, 171, 30))
        self.send_edit_team.setMinimumSize(QSize(0, 30))
        self.send_edit_team.setStyleSheet(u"background-image: url();")
        self.time_start_label = QLabel(self.widget)
        self.time_start_label.setObjectName(u"time_start_label")
        self.time_start_label.setGeometry(QRect(10, 210, 151, 21))
        self.time_start_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_time_start_4 = QLineEdit(self.widget)
        self.lineEdit_time_start_4.setObjectName(u"lineEdit_time_start_4")
        self.lineEdit_time_start_4.setGeometry(QRect(200, 210, 113, 21))
        self.time_finish_label = QLabel(self.widget)
        self.time_finish_label.setObjectName(u"time_finish_label")
        self.time_finish_label.setGeometry(QRect(10, 250, 141, 21))
        self.time_finish_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_time_finish_5 = QLineEdit(self.widget)
        self.lineEdit_time_finish_5.setObjectName(u"lineEdit_time_finish_5")
        self.lineEdit_time_finish_5.setGeometry(QRect(200, 250, 113, 21))
        self.count_place_label = QLabel(self.widget)
        self.count_place_label.setObjectName(u"count_place_label")
        self.count_place_label.setGeometry(QRect(10, 290, 141, 21))
        self.count_place_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_count_place_6 = QLineEdit(self.widget)
        self.lineEdit_count_place_6.setObjectName(u"lineEdit_count_place_6")
        self.lineEdit_count_place_6.setGeometry(QRect(200, 290, 113, 21))
        self.lineEdit_prise_tiket_7 = QLineEdit(self.widget)
        self.lineEdit_prise_tiket_7.setObjectName(u"lineEdit_prise_tiket_7")
        self.lineEdit_prise_tiket_7.setGeometry(QRect(200, 330, 113, 21))
        self.prise_tiket_label = QLabel(self.widget)
        self.prise_tiket_label.setObjectName(u"prise_tiket_label")
        self.prise_tiket_label.setGeometry(QRect(10, 330, 141, 21))
        self.prise_tiket_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_companu_8 = QLineEdit(self.widget)
        self.lineEdit_companu_8.setObjectName(u"lineEdit_companu_8")
        self.lineEdit_companu_8.setGeometry(QRect(200, 370, 113, 21))
        self.companu_label = QLabel(self.widget)
        self.companu_label.setObjectName(u"companu_label")
        self.companu_label.setGeometry(QRect(10, 370, 141, 21))
        self.companu_label.setAlignment(Qt.AlignCenter)
        self.lineEdit_id_team_9 = QLineEdit(self.widget)
        self.lineEdit_id_team_9.setObjectName(u"lineEdit_id_team_9")
        self.lineEdit_id_team_9.setGeometry(QRect(200, 410, 113, 21))
        self.id_team_label = QLabel(self.widget)
        self.id_team_label.setObjectName(u"id_team_label")
        self.id_team_label.setGeometry(QRect(10, 410, 141, 21))
        self.id_team_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(edit_reis)

        QMetaObject.connectSlotsByName(edit_reis)
    # setupUi

    def retranslateUi(self, edit_reis):
        edit_reis.setWindowTitle(QCoreApplication.translate("edit_reis", u"Edit Info", None))
        self.Title_Label_Reis.setText(QCoreApplication.translate("edit_reis", u"\u0420\u0435\u0439\u0441\u044b", None))
        self.id_reis_label.setText(QCoreApplication.translate("edit_reis", u"id_\u0440\u0435\u0439\u0441\u0430", None))
        self.numder_reis_label.setText(QCoreApplication.translate("edit_reis", u"\u041d\u043e\u043c\u0435\u0440_\u0440\u0435\u0439\u0441\u0430", None))
        self.point_start_label.setText(QCoreApplication.translate("edit_reis", u"\u041f\u0443\u043d\u043a\u0442\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.point_finish_label.setText(QCoreApplication.translate("edit_reis", u"\u041f\u0443\u043d\u043a\u0442\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.send_edit_team.setText(QCoreApplication.translate("edit_reis", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.time_start_label.setText(QCoreApplication.translate("edit_reis", u"\u0412\u0440\u0435\u043c\u044f\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.lineEdit_time_start_4.setPlaceholderText(QCoreApplication.translate("edit_reis", u"00.00.0000", None))
        self.time_finish_label.setText(QCoreApplication.translate("edit_reis", u"\u0412\u0440\u0435\u043c\u044f\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.lineEdit_time_finish_5.setPlaceholderText(QCoreApplication.translate("edit_reis", u"00.00.0000", None))
        self.count_place_label.setText(QCoreApplication.translate("edit_reis", u"\u041a\u043e\u043b\u0412\u043e_\u043c\u0435\u0441\u0442", None))
        self.prise_tiket_label.setText(QCoreApplication.translate("edit_reis", u"\u0426\u0435\u043d\u0430_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.companu_label.setText(QCoreApplication.translate("edit_reis", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a", None))
        self.id_team_label.setText(QCoreApplication.translate("edit_reis", u"id_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))
    # retranslateUi

