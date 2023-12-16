# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_light.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resourse

class Ui_MainWindow_Light(object):
    def setupUi(self, MainWindow_Light):
        if not MainWindow_Light.objectName():
            MainWindow_Light.setObjectName(u"MainWindow_Light")
        MainWindow_Light.resize(1114, 800)
        MainWindow_Light.setMinimumSize(QSize(800, 800))
        MainWindow_Light.setMaximumSize(QSize(1114, 828))
        self.styleSheet = QWidget(MainWindow_Light)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"/*176, 196, 222    */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QTableView {	\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	color: black;\n"
"}\n"
"QTableView::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableView::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #b5bfc6;\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border"
                        "-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableView::horizontalHeader {	\n"
"	background-color: #b5bfc6;\n"
"}\n"
"QTableView::verticalHeader {	\n"
"	background-color: #b5bfc6;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: #b5bfc6;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	border-left-color: #b5bfc6;\n"
"	color: black;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(201, 99, 75);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QPlainTe"
                        "xtEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #9fcbed;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #7b9cb5;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-ori"
                        "gin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #7b9cb5;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #9fcbed;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #7b9cb5;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcon"
                        "trol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #7b9cb5;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52,"
                        " 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/icons/down_black.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QA"
                        "bstractItemView {\n"
"	color: black;	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle"
                        ":vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"#bgApp {	\n"
"	background-color: #eff2f9;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"#leftMenuBg {	\n"
"	background-color: #b5bfc6;\n"
"}")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Normal)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"#titleLeftApp {\n"
"	 font: 63 12pt \"Segoe UI Semibold\"; \n"
"}")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"#titleLeftDescription {\n"
"	 font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249);\n"
"}")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"#topMenu .QPushButton,\n"
"#futter_menu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover,\n"
"#futter_menu .QPushButton:hover,\n"
"#toggleBox.QPushButton:hover  {\n"
"	background-color: #9ba7b0;\n"
"}\n"
"#topMenu .QPushButton:pressed,\n"
"#futter_menu .QPushButton:pressed,\n"
"#toggleBox.QPushButton:pressed {	\n"
"	background-color: #5085ad;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setStyleSheet(u"#btn_start_aktive {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #99a2a8; \n"
"	color: rgb(113, 126, 149);\n"
"}")
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_start_aktive = QPushButton(self.toggleBox)
        self.btn_start_aktive.setObjectName(u"btn_start_aktive")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start_aktive.sizePolicy().hasHeightForWidth())
        self.btn_start_aktive.setSizePolicy(sizePolicy)
        self.btn_start_aktive.setMinimumSize(QSize(0, 45))
        self.btn_start_aktive.setFont(font)
        self.btn_start_aktive.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_aktive.setLayoutDirection(Qt.LeftToRight)
        self.btn_start_aktive.setStyleSheet(u"background-image: url(:/icons/icons/airplane_ticket_black.png);")

        self.verticalLayout_4.addWidget(self.btn_start_aktive)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_pilot = QPushButton(self.topMenu)
        self.btn_pilot.setObjectName(u"btn_pilot")
        sizePolicy.setHeightForWidth(self.btn_pilot.sizePolicy().hasHeightForWidth())
        self.btn_pilot.setSizePolicy(sizePolicy)
        self.btn_pilot.setMinimumSize(QSize(0, 45))
        self.btn_pilot.setFont(font)
        self.btn_pilot.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pilot.setLayoutDirection(Qt.LeftToRight)
        self.btn_pilot.setStyleSheet(u"background-image: url(:/icons/icons/badge_black.png);")

        self.verticalLayout_8.addWidget(self.btn_pilot)

        self.btn_people = QPushButton(self.topMenu)
        self.btn_people.setObjectName(u"btn_people")
        sizePolicy.setHeightForWidth(self.btn_people.sizePolicy().hasHeightForWidth())
        self.btn_people.setSizePolicy(sizePolicy)
        self.btn_people.setMinimumSize(QSize(0, 45))
        self.btn_people.setFont(font)
        self.btn_people.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_people.setLayoutDirection(Qt.LeftToRight)
        self.btn_people.setStyleSheet(u"background-image: url(:/icons/icons/person_search_black.png);")

        self.verticalLayout_8.addWidget(self.btn_people)

        self.btn_reis = QPushButton(self.topMenu)
        self.btn_reis.setObjectName(u"btn_reis")
        sizePolicy.setHeightForWidth(self.btn_reis.sizePolicy().hasHeightForWidth())
        self.btn_reis.setSizePolicy(sizePolicy)
        self.btn_reis.setMinimumSize(QSize(0, 45))
        self.btn_reis.setFont(font)
        self.btn_reis.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reis.setLayoutDirection(Qt.LeftToRight)
        self.btn_reis.setStyleSheet(u"background-image: url(:/icons/icons/flight_takeoff_black.png);")

        self.verticalLayout_8.addWidget(self.btn_reis)

        self.btn_reis_stop = QPushButton(self.topMenu)
        self.btn_reis_stop.setObjectName(u"btn_reis_stop")
        sizePolicy.setHeightForWidth(self.btn_reis_stop.sizePolicy().hasHeightForWidth())
        self.btn_reis_stop.setSizePolicy(sizePolicy)
        self.btn_reis_stop.setMinimumSize(QSize(0, 45))
        self.btn_reis_stop.setFont(font)
        self.btn_reis_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reis_stop.setLayoutDirection(Qt.LeftToRight)
        self.btn_reis_stop.setStyleSheet(u"background-image: url(:/icons/icons/lock_clock_black.png)")

        self.verticalLayout_8.addWidget(self.btn_reis_stop)

        self.btn_qwery = QPushButton(self.topMenu)
        self.btn_qwery.setObjectName(u"btn_qwery")
        sizePolicy.setHeightForWidth(self.btn_qwery.sizePolicy().hasHeightForWidth())
        self.btn_qwery.setSizePolicy(sizePolicy)
        self.btn_qwery.setMinimumSize(QSize(0, 45))
        self.btn_qwery.setFont(font)
        self.btn_qwery.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_qwery.setLayoutDirection(Qt.LeftToRight)
        self.btn_qwery.setStyleSheet(u"background-image: url(:/icons/icons/subject_black.png);")

        self.verticalLayout_8.addWidget(self.btn_qwery)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.futter_menu = QFrame(self.leftMenuFrame)
        self.futter_menu.setObjectName(u"futter_menu")
        self.futter_menu.setStyleSheet(u"#futter_menu .QPushButton {	\n"
"	border-left: 20px solid transparent;\n"
"}\n"
"")
        self.futter_menu.setFrameShape(QFrame.NoFrame)
        self.futter_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.futter_menu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.theme_mod = QPushButton(self.futter_menu)
        self.theme_mod.setObjectName(u"theme_mod")
        sizePolicy.setHeightForWidth(self.theme_mod.sizePolicy().hasHeightForWidth())
        self.theme_mod.setSizePolicy(sizePolicy)
        self.theme_mod.setMinimumSize(QSize(0, 45))
        self.theme_mod.setFont(font)
        self.theme_mod.setCursor(QCursor(Qt.PointingHandCursor))
        self.theme_mod.setLayoutDirection(Qt.LeftToRight)
        self.theme_mod.setStyleSheet(u"background-image: url(:/icons/icons/dark_mode.png);")

        self.verticalLayout_9.addWidget(self.theme_mod)


        self.verticalMenuLayout.addWidget(self.futter_menu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setGeometry(QRect(0, 0, 1031, 50))
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color: #b5bfc6;\n"
"color: black;\n"
"padding-left: 10px; \n"
"font-size: 12pt;\n"
"\n"
"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentTopBg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.leftBox.setFont(font3)
        self.leftBox.setStyleSheet(u"")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setGeometry(QRect(0, 0, 1021, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"color: black;")
        self.titleRightInfo.setTextFormat(Qt.AutoText)
        self.titleRightInfo.setAlignment(Qt.AlignCenter)
        self.titleRightInfo.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_2.addWidget(self.leftBox)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setGeometry(QRect(0, 50, 1032, 771))
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 1032, 791))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setGeometry(QRect(0, 0, 1032, 761))
        self.pagesContainer.setStyleSheet(u"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1012, 671))
        self.stackedWidget.setStyleSheet(u"QstackedWidget,\n"
"QWidget,\n"
"QTableWidget{\n"
"	background: transparent;\n"
"}\n"
"#search_tiket_btn,\n"
"#search_pilot_btn,\n"
"#search_people_btn,\n"
"#search_reis_btn,\n"
"#search_reis_block_btn { \n"
"	font-size: 13px; \n"
"	color: black; \n"
"	padding-left: 35px;	\n"
"	padding-bottom: 2px;\n"
"    background-repeat: no-repeat;\n"
"	background-color: #b5bfc6;\n"
"	background-image: url(:/icons/icons/search_black.png);\n"
"	background-position: left;\n"
"	border: 25px;\n"
"	border-style: none solid none solid;\n"
"	border-color: #b5bfc6;\n"
"	border-radius: 7px;\n"
"	text-align: left;\n"
"}\n"
"#search_tiket_btn:hover,\n"
"#search_pilot_btn:hover,\n"
"#search_people_btn:hover,\n"
"#search_reis_btn:hover,\n"
"#search_reis_block_btn:hover {\n"
"	background-color: #9ba7b0;\n"
"	border-color: #9ba7b0;\n"
"}\n"
"#search_tiket_btn:pressed,\n"
"#search_pilot_btn:pressed,\n"
"#search_people_btn:pressed,\n"
"#search_reis_btn:pressed,\n"
"#search_reis_block_btn:pressed {	\n"
"	background-color: #5085ad;\n"
"	bord"
                        "er-color: #5085ad;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: #b5bfc6;\n"
"	color: black; \n"
"	font-size: 15px; \n"
"	border: 1px;\n"
"	border-color: rgb(52, 59, 72);\n"
"}\n"
"QLineEdit,\n"
"QComboBox{\n"
"	background-color: #b5bfc6;\n"
"	color: black;\n"
"}")
        self.start_widget = QWidget()
        self.start_widget.setObjectName(u"start_widget")
        self.start_widget.setStyleSheet(u"")
        self.table_tikets = QTableView(self.start_widget)
        self.table_tikets.setObjectName(u"table_tikets")
        self.table_tikets.setGeometry(QRect(10, 300, 990, 371))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_tikets.sizePolicy().hasHeightForWidth())
        self.table_tikets.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_tikets.setPalette(palette)
        self.table_tikets.setFrameShape(QFrame.NoFrame)
        self.table_tikets.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_tikets.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_tikets.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_tikets.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_tikets.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_tikets.setShowGrid(True)
        self.table_tikets.setGridStyle(Qt.SolidLine)
        self.table_tikets.setSortingEnabled(False)
        self.table_tikets.verticalHeader().setVisible(False)
        self.table_tikets.verticalHeader().setCascadingSectionResizes(True)
        self.table_tikets.verticalHeader().setHighlightSections(False)
        self.horizontalLayoutWidget = QWidget(self.start_widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 831, 36))
        self.tiket_searchlLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.tiket_searchlLayout.setObjectName(u"tiket_searchlLayout")
        self.tiket_searchlLayout.setContentsMargins(0, 0, 0, 0)
        self.tiket_comboBox = QComboBox(self.horizontalLayoutWidget)
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.addItem("")
        self.tiket_comboBox.setObjectName(u"tiket_comboBox")
        self.tiket_comboBox.setMinimumSize(QSize(200, 0))
        self.tiket_comboBox.setMaximumSize(QSize(200, 16777215))
        self.tiket_comboBox.setFont(font)
        self.tiket_comboBox.setToolTipDuration(-1)
        self.tiket_comboBox.setAutoFillBackground(False)
        self.tiket_comboBox.setStyleSheet(u"")
        self.tiket_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.tiket_comboBox.setIconSize(QSize(16, 16))
        self.tiket_comboBox.setFrame(True)

        self.tiket_searchlLayout.addWidget(self.tiket_comboBox)

        self.tiket_edit = QLineEdit(self.horizontalLayoutWidget)
        self.tiket_edit.setObjectName(u"tiket_edit")
        self.tiket_edit.setMinimumSize(QSize(250, 30))
        self.tiket_edit.setMaximumSize(QSize(250, 16777215))
        self.tiket_edit.setStyleSheet(u"")

        self.tiket_searchlLayout.addWidget(self.tiket_edit)

        self.search_tiket_btn = QPushButton(self.horizontalLayoutWidget)
        self.search_tiket_btn.setObjectName(u"search_tiket_btn")
        self.search_tiket_btn.setMinimumSize(QSize(200, 30))
        self.search_tiket_btn.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.search_tiket_btn.setFont(font4)
        self.search_tiket_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_tiket_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_tiket_btn.setIcon(icon)

        self.tiket_searchlLayout.addWidget(self.search_tiket_btn)

        self.title_label_tiket = QLabel(self.start_widget)
        self.title_label_tiket.setObjectName(u"title_label_tiket")
        self.title_label_tiket.setGeometry(QRect(310, 20, 311, 31))
        self.title_label_tiket.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.start_widget)
        self.pilot_widget = QWidget()
        self.pilot_widget.setObjectName(u"pilot_widget")
        self.table_pilots = QTableView(self.pilot_widget)
        self.table_pilots.setObjectName(u"table_pilots")
        self.table_pilots.setGeometry(QRect(10, 300, 990, 371))
        sizePolicy3.setHeightForWidth(self.table_pilots.sizePolicy().hasHeightForWidth())
        self.table_pilots.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_pilots.setPalette(palette1)
        self.table_pilots.setFrameShape(QFrame.NoFrame)
        self.table_pilots.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_pilots.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_pilots.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_pilots.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_pilots.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_pilots.setShowGrid(True)
        self.table_pilots.setGridStyle(Qt.SolidLine)
        self.table_pilots.setSortingEnabled(False)
        self.table_pilots.horizontalHeader().setMinimumSectionSize(230)
        self.table_pilots.horizontalHeader().setDefaultSectionSize(230)
        self.table_pilots.horizontalHeader().setHighlightSections(True)
        self.table_pilots.verticalHeader().setVisible(False)
        self.table_pilots.verticalHeader().setCascadingSectionResizes(True)
        self.table_pilots.verticalHeader().setDefaultSectionSize(24)
        self.table_pilots.verticalHeader().setHighlightSections(False)
        self.table_pilots.verticalHeader().setProperty("showSortIndicator", False)
        self.horizontalLayoutWidget_2 = QWidget(self.pilot_widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 80, 831, 36))
        self.pilot_searchlLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.pilot_searchlLayout.setObjectName(u"pilot_searchlLayout")
        self.pilot_searchlLayout.setContentsMargins(0, 0, 0, 0)
        self.pilot_comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.pilot_comboBox.addItem("")
        self.pilot_comboBox.addItem("")
        self.pilot_comboBox.addItem("")
        self.pilot_comboBox.addItem("")
        self.pilot_comboBox.addItem("")
        self.pilot_comboBox.setObjectName(u"pilot_comboBox")
        self.pilot_comboBox.setMinimumSize(QSize(200, 0))
        self.pilot_comboBox.setMaximumSize(QSize(200, 16777215))
        self.pilot_comboBox.setFont(font)
        self.pilot_comboBox.setToolTipDuration(-1)
        self.pilot_comboBox.setAutoFillBackground(False)
        self.pilot_comboBox.setStyleSheet(u"")
        self.pilot_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.pilot_comboBox.setIconSize(QSize(16, 16))
        self.pilot_comboBox.setFrame(True)

        self.pilot_searchlLayout.addWidget(self.pilot_comboBox)

        self.pilot_edit = QLineEdit(self.horizontalLayoutWidget_2)
        self.pilot_edit.setObjectName(u"pilot_edit")
        self.pilot_edit.setMinimumSize(QSize(250, 30))
        self.pilot_edit.setMaximumSize(QSize(250, 16777215))
        self.pilot_edit.setStyleSheet(u"")

        self.pilot_searchlLayout.addWidget(self.pilot_edit)

        self.search_pilot_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.search_pilot_btn.setObjectName(u"search_pilot_btn")
        self.search_pilot_btn.setMinimumSize(QSize(200, 30))
        self.search_pilot_btn.setMaximumSize(QSize(200, 16777215))
        self.search_pilot_btn.setFont(font4)
        self.search_pilot_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_pilot_btn.setStyleSheet(u"")
        self.search_pilot_btn.setIcon(icon)

        self.pilot_searchlLayout.addWidget(self.search_pilot_btn)

        self.title_label_pilots = QLabel(self.pilot_widget)
        self.title_label_pilots.setObjectName(u"title_label_pilots")
        self.title_label_pilots.setGeometry(QRect(310, 20, 311, 31))
        self.title_label_pilots.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pilot_widget)
        self.people_widget = QWidget()
        self.people_widget.setObjectName(u"people_widget")
        self.table_people = QTableView(self.people_widget)
        self.table_people.setObjectName(u"table_people")
        self.table_people.setGeometry(QRect(10, 300, 990, 371))
        sizePolicy3.setHeightForWidth(self.table_people.sizePolicy().hasHeightForWidth())
        self.table_people.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_people.setPalette(palette2)
        self.table_people.setFrameShape(QFrame.NoFrame)
        self.table_people.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_people.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_people.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_people.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_people.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_people.setShowGrid(True)
        self.table_people.setGridStyle(Qt.SolidLine)
        self.table_people.setSortingEnabled(False)
        self.table_people.horizontalHeader().setMinimumSectionSize(210)
        self.table_people.horizontalHeader().setDefaultSectionSize(210)
        self.table_people.horizontalHeader().setHighlightSections(True)
        self.table_people.verticalHeader().setVisible(False)
        self.table_people.verticalHeader().setCascadingSectionResizes(True)
        self.table_people.verticalHeader().setDefaultSectionSize(24)
        self.table_people.verticalHeader().setHighlightSections(False)
        self.table_people.verticalHeader().setProperty("showSortIndicator", False)
        self.horizontalLayoutWidget_3 = QWidget(self.people_widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 80, 831, 36))
        self.people_searchlLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.people_searchlLayout.setObjectName(u"people_searchlLayout")
        self.people_searchlLayout.setContentsMargins(0, 0, 0, 0)
        self.people_comboBox = QComboBox(self.horizontalLayoutWidget_3)
        self.people_comboBox.addItem("")
        self.people_comboBox.addItem("")
        self.people_comboBox.addItem("")
        self.people_comboBox.addItem("")
        self.people_comboBox.addItem("")
        self.people_comboBox.setObjectName(u"people_comboBox")
        self.people_comboBox.setMinimumSize(QSize(200, 0))
        self.people_comboBox.setMaximumSize(QSize(200, 16777215))
        self.people_comboBox.setFont(font)
        self.people_comboBox.setToolTipDuration(-1)
        self.people_comboBox.setAutoFillBackground(False)
        self.people_comboBox.setStyleSheet(u"")
        self.people_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.people_comboBox.setIconSize(QSize(16, 16))
        self.people_comboBox.setFrame(True)

        self.people_searchlLayout.addWidget(self.people_comboBox)

        self.people_edit = QLineEdit(self.horizontalLayoutWidget_3)
        self.people_edit.setObjectName(u"people_edit")
        self.people_edit.setMinimumSize(QSize(250, 30))
        self.people_edit.setMaximumSize(QSize(250, 16777215))
        self.people_edit.setStyleSheet(u"")

        self.people_searchlLayout.addWidget(self.people_edit)

        self.search_people_btn = QPushButton(self.horizontalLayoutWidget_3)
        self.search_people_btn.setObjectName(u"search_people_btn")
        self.search_people_btn.setMinimumSize(QSize(200, 30))
        self.search_people_btn.setMaximumSize(QSize(200, 16777215))
        self.search_people_btn.setFont(font4)
        self.search_people_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_people_btn.setStyleSheet(u"")
        self.search_people_btn.setIcon(icon)

        self.people_searchlLayout.addWidget(self.search_people_btn)

        self.title_label_people = QLabel(self.people_widget)
        self.title_label_people.setObjectName(u"title_label_people")
        self.title_label_people.setGeometry(QRect(320, 20, 311, 31))
        self.title_label_people.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.people_widget)
        self.reis_widget = QWidget()
        self.reis_widget.setObjectName(u"reis_widget")
        self.table_reis = QTableView(self.reis_widget)
        self.table_reis.setObjectName(u"table_reis")
        self.table_reis.setGeometry(QRect(9, 300, 991, 371))
        sizePolicy3.setHeightForWidth(self.table_reis.sizePolicy().hasHeightForWidth())
        self.table_reis.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_reis.setPalette(palette3)
        self.table_reis.setFrameShape(QFrame.NoFrame)
        self.table_reis.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_reis.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_reis.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_reis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_reis.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_reis.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_reis.setShowGrid(True)
        self.table_reis.setGridStyle(Qt.SolidLine)
        self.table_reis.setSortingEnabled(False)
        self.table_reis.horizontalHeader().setMinimumSectionSize(110)
        self.table_reis.horizontalHeader().setDefaultSectionSize(110)
        self.table_reis.horizontalHeader().setHighlightSections(True)
        self.table_reis.verticalHeader().setVisible(False)
        self.table_reis.verticalHeader().setCascadingSectionResizes(True)
        self.table_reis.verticalHeader().setDefaultSectionSize(24)
        self.table_reis.verticalHeader().setHighlightSections(False)
        self.table_reis.verticalHeader().setProperty("showSortIndicator", False)
        self.horizontalLayoutWidget_4 = QWidget(self.reis_widget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 80, 831, 36))
        self.reis_searchlLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.reis_searchlLayout.setObjectName(u"reis_searchlLayout")
        self.reis_searchlLayout.setContentsMargins(0, 0, 0, 0)
        self.reis_comboBox = QComboBox(self.horizontalLayoutWidget_4)
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.addItem("")
        self.reis_comboBox.setObjectName(u"reis_comboBox")
        self.reis_comboBox.setMinimumSize(QSize(200, 0))
        self.reis_comboBox.setMaximumSize(QSize(200, 16777215))
        self.reis_comboBox.setFont(font)
        self.reis_comboBox.setToolTipDuration(-1)
        self.reis_comboBox.setAutoFillBackground(False)
        self.reis_comboBox.setStyleSheet(u"")
        self.reis_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.reis_comboBox.setIconSize(QSize(16, 16))
        self.reis_comboBox.setFrame(True)

        self.reis_searchlLayout.addWidget(self.reis_comboBox)

        self.reis_edit = QLineEdit(self.horizontalLayoutWidget_4)
        self.reis_edit.setObjectName(u"reis_edit")
        self.reis_edit.setMinimumSize(QSize(250, 30))
        self.reis_edit.setMaximumSize(QSize(250, 16777215))
        self.reis_edit.setStyleSheet(u"")

        self.reis_searchlLayout.addWidget(self.reis_edit)

        self.search_reis_btn = QPushButton(self.horizontalLayoutWidget_4)
        self.search_reis_btn.setObjectName(u"search_reis_btn")
        self.search_reis_btn.setMinimumSize(QSize(200, 30))
        self.search_reis_btn.setMaximumSize(QSize(200, 16777215))
        self.search_reis_btn.setFont(font4)
        self.search_reis_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_reis_btn.setStyleSheet(u"")
        self.search_reis_btn.setIcon(icon)

        self.reis_searchlLayout.addWidget(self.search_reis_btn)

        self.title_label_reis = QLabel(self.reis_widget)
        self.title_label_reis.setObjectName(u"title_label_reis")
        self.title_label_reis.setGeometry(QRect(330, 20, 311, 31))
        self.title_label_reis.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.reis_widget)
        self.reis_block_widget = QWidget()
        self.reis_block_widget.setObjectName(u"reis_block_widget")
        self.table_reis_block = QTableView(self.reis_block_widget)
        self.table_reis_block.setObjectName(u"table_reis_block")
        self.table_reis_block.setGeometry(QRect(10, 300, 990, 371))
        sizePolicy3.setHeightForWidth(self.table_reis_block.sizePolicy().hasHeightForWidth())
        self.table_reis_block.setSizePolicy(sizePolicy3)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_reis_block.setPalette(palette4)
        self.table_reis_block.setFrameShape(QFrame.NoFrame)
        self.table_reis_block.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_reis_block.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_reis_block.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_reis_block.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_reis_block.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_reis_block.setShowGrid(True)
        self.table_reis_block.setGridStyle(Qt.SolidLine)
        self.table_reis_block.setSortingEnabled(False)
        self.table_reis_block.horizontalHeader().setVisible(True)
        self.table_reis_block.horizontalHeader().setMinimumSectionSize(100)
        self.table_reis_block.horizontalHeader().setDefaultSectionSize(500)
        self.table_reis_block.horizontalHeader().setHighlightSections(True)
        self.table_reis_block.verticalHeader().setVisible(False)
        self.table_reis_block.verticalHeader().setCascadingSectionResizes(True)
        self.table_reis_block.verticalHeader().setDefaultSectionSize(24)
        self.table_reis_block.verticalHeader().setHighlightSections(False)
        self.table_reis_block.verticalHeader().setProperty("showSortIndicator", False)
        self.horizontalLayoutWidget_5 = QWidget(self.reis_block_widget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 80, 831, 36))
        self.reis_block_searchlLayout = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.reis_block_searchlLayout.setObjectName(u"reis_block_searchlLayout")
        self.reis_block_searchlLayout.setContentsMargins(0, 0, 0, 0)
        self.reis_block_comboBox = QComboBox(self.horizontalLayoutWidget_5)
        self.reis_block_comboBox.addItem("")
        self.reis_block_comboBox.addItem("")
        self.reis_block_comboBox.addItem("")
        self.reis_block_comboBox.addItem("")
        self.reis_block_comboBox.setObjectName(u"reis_block_comboBox")
        self.reis_block_comboBox.setMinimumSize(QSize(200, 0))
        self.reis_block_comboBox.setMaximumSize(QSize(200, 16777215))
        self.reis_block_comboBox.setFont(font)
        self.reis_block_comboBox.setToolTipDuration(-1)
        self.reis_block_comboBox.setAutoFillBackground(False)
        self.reis_block_comboBox.setStyleSheet(u"")
        self.reis_block_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.reis_block_comboBox.setIconSize(QSize(16, 16))
        self.reis_block_comboBox.setFrame(True)

        self.reis_block_searchlLayout.addWidget(self.reis_block_comboBox)

        self.reis_block_edit = QLineEdit(self.horizontalLayoutWidget_5)
        self.reis_block_edit.setObjectName(u"reis_block_edit")
        self.reis_block_edit.setMinimumSize(QSize(250, 30))
        self.reis_block_edit.setMaximumSize(QSize(250, 16777215))
        self.reis_block_edit.setStyleSheet(u"")

        self.reis_block_searchlLayout.addWidget(self.reis_block_edit)

        self.search_reis_block_btn = QPushButton(self.horizontalLayoutWidget_5)
        self.search_reis_block_btn.setObjectName(u"search_reis_block_btn")
        self.search_reis_block_btn.setMinimumSize(QSize(200, 30))
        self.search_reis_block_btn.setMaximumSize(QSize(200, 16777215))
        self.search_reis_block_btn.setFont(font4)
        self.search_reis_block_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_reis_block_btn.setStyleSheet(u"background-image: url(:/icons/icons/search_black.png);")
        self.search_reis_block_btn.setIcon(icon)

        self.reis_block_searchlLayout.addWidget(self.search_reis_block_btn)

        self.title_label_reis_block = QLabel(self.reis_block_widget)
        self.title_label_reis_block.setObjectName(u"title_label_reis_block")
        self.title_label_reis_block.setGeometry(QRect(320, 20, 311, 31))
        self.title_label_reis_block.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.reis_block_widget)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font4)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette5)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.bottomBar = QFrame(self.pagesContainer)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setGeometry(QRect(0, 680, 1033, 50))
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 50))
        self.bottomBar.setStyleSheet(u"#bottomBar { \n"
"	height: 40px;\n"
"	background-color: #b5bfc6;\n"
"}\n"
"#add_row,\n"
"#update_row,\n"
"#delete_row,\n"
"#clean_filtr { \n"
"	font-size: 13px; \n"
"	color: black; \n"
"	padding-left: 40px;	\n"
"	padding-bottom: 2px;\n"
"    background-repeat: no-repeat;\n"
"	background-color: #e4ebf1;\n"
"	background-position: left;\n"
"	border: 25px;\n"
"	border-style: none solid none solid;\n"
"	border-color: #e4ebf1;\n"
"	border-radius: 7px;\n"
"	text-align: left;\n"
"}\n"
"#add_row:hover,\n"
"#update_row:hover,\n"
"#delete_row:hover,\n"
"#clean_filtr:hover {\n"
"	background-color: #9ba7b0;\n"
"	border-color: #9ba7b0;\n"
"}\n"
"#add_row:pressed,\n"
"#update_row:pressed,\n"
"#delete_row:pressed,\n"
"#clean_filtr:pressed {	\n"
"	background-color: #5085ad;\n"
"	border-color: #5085ad;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.bottomBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 0, 971, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.clean_filtr = QPushButton(self.layoutWidget)
        self.clean_filtr.setObjectName(u"clean_filtr")
        self.clean_filtr.setMinimumSize(QSize(0, 30))
        self.clean_filtr.setStyleSheet(u"background-image: url();")

        self.horizontalLayout.addWidget(self.clean_filtr)

        self.add_row = QPushButton(self.layoutWidget)
        self.add_row.setObjectName(u"add_row")
        self.add_row.setMinimumSize(QSize(0, 30))
        self.add_row.setStyleSheet(u"background-image: url(:/icons/icons/post_add_black.png);\n"
"")

        self.horizontalLayout.addWidget(self.add_row)

        self.update_row = QPushButton(self.layoutWidget)
        self.update_row.setObjectName(u"update_row")
        self.update_row.setMinimumSize(QSize(0, 30))
        self.update_row.setStyleSheet(u"background-image: url(:/icons/icons/edit_note_black.png);\n"
"")

        self.horizontalLayout.addWidget(self.update_row)

        self.delete_row = QPushButton(self.layoutWidget)
        self.delete_row.setObjectName(u"delete_row")
        self.delete_row.setMinimumSize(QSize(0, 30))
        self.delete_row.setStyleSheet(u"background-image: url(:/icons/icons/delete_black.png);\n"
"")

        self.horizontalLayout.addWidget(self.delete_row)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow_Light.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow_Light)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow_Light)
    # setupUi

    def retranslateUi(self, MainWindow_Light):
        MainWindow_Light.setWindowTitle(QCoreApplication.translate("MainWindow_Light", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow_Light", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow_Light", u"Modern GUI / Flat Style", None))
        self.btn_start_aktive.setText("")
        self.btn_pilot.setText("")
        self.btn_people.setText(QCoreApplication.translate("MainWindow_Light", u"Widgets", None))
        self.btn_reis.setText(QCoreApplication.translate("MainWindow_Light", u"New", None))
        self.btn_reis_stop.setText(QCoreApplication.translate("MainWindow_Light", u"Save", None))
        self.btn_qwery.setText(QCoreApplication.translate("MainWindow_Light", u"Exit", None))
        self.theme_mod.setText(QCoreApplication.translate("MainWindow_Light", u"Left Box", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow_Light", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u0430\u044d\u0440\u043e\u043f\u043e\u0440\u0442\u0430", None))
        self.tiket_comboBox.setItemText(0, "")
        self.tiket_comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"id_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.tiket_comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"\u041d\u043e\u043c\u0435\u0440_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.tiket_comboBox.setItemText(3, QCoreApplication.translate("MainWindow_Light", u"\u0426\u0435\u043d\u0430_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.tiket_comboBox.setItemText(4, QCoreApplication.translate("MainWindow_Light", u"id_\u0440\u0435\u0439\u0441\u0430", None))
        self.tiket_comboBox.setItemText(5, QCoreApplication.translate("MainWindow_Light", u"id_\u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430", None))

        self.tiket_edit.setText("")
        self.tiket_edit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.search_tiket_btn.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.title_label_tiket.setText(QCoreApplication.translate("MainWindow_Light", u"\u0411\u0438\u043b\u0435\u0442\u044b", None))
        self.pilot_comboBox.setItemText(0, "")
        self.pilot_comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"id_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))
        self.pilot_comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0438\u0440", None))
        self.pilot_comboBox.setItemText(3, QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u043c\u043e\u0448\u043d\u0438\u043a_\u043a\u043e\u043c\u0430\u043d\u0434\u0438\u0440\u0430", None))
        self.pilot_comboBox.setItemText(4, QCoreApplication.translate("MainWindow_Light", u"\u041a\u043e\u043b\u0412\u043e_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))

        self.pilot_edit.setText("")
        self.pilot_edit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.search_pilot_btn.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.title_label_pilots.setText(QCoreApplication.translate("MainWindow_Light", u"\u042d\u043a\u0438\u043f\u0430\u0436", None))
        self.people_comboBox.setItemText(0, "")
        self.people_comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"id_\u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0430", None))
        self.people_comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.people_comboBox.setItemText(3, QCoreApplication.translate("MainWindow_Light", u"\u0418\u043c\u044f", None))
        self.people_comboBox.setItemText(4, QCoreApplication.translate("MainWindow_Light", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))

        self.people_edit.setText("")
        self.people_edit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.search_people_btn.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.title_label_people.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u044b", None))
        self.reis_comboBox.setItemText(0, "")
        self.reis_comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"id_\u0440\u0435\u0439\u0441\u0430", None))
        self.reis_comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"\u041d\u043e\u043c\u0435\u0440_\u0440\u0435\u0439\u0441\u0430", None))
        self.reis_comboBox.setItemText(3, QCoreApplication.translate("MainWindow_Light", u"\u041f\u0443\u043d\u043a\u0442\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.reis_comboBox.setItemText(4, QCoreApplication.translate("MainWindow_Light", u"\u041f\u0443\u043d\u043a\u0442\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.reis_comboBox.setItemText(5, QCoreApplication.translate("MainWindow_Light", u"\u0412\u0440\u0435\u043c\u044f\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.reis_comboBox.setItemText(6, QCoreApplication.translate("MainWindow_Light", u"\u0412\u0440\u0435\u043c\u044f\u041f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.reis_comboBox.setItemText(7, QCoreApplication.translate("MainWindow_Light", u"\u041a\u043e\u043b\u0412\u043e_\u043c\u0435\u0441\u0442", None))
        self.reis_comboBox.setItemText(8, QCoreApplication.translate("MainWindow_Light", u"\u0426\u0435\u043d\u0430_\u0431\u0438\u043b\u0435\u0442\u0430", None))
        self.reis_comboBox.setItemText(9, QCoreApplication.translate("MainWindow_Light", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a", None))
        self.reis_comboBox.setItemText(10, QCoreApplication.translate("MainWindow_Light", u"id_\u044d\u043a\u0438\u043f\u0430\u0436\u0430", None))

        self.reis_comboBox.setCurrentText("")
        self.reis_edit.setText("")
        self.reis_edit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.search_reis_btn.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.title_label_reis.setText(QCoreApplication.translate("MainWindow_Light", u"\u0420\u0435\u0439\u0441\u044b", None))
        self.reis_block_comboBox.setItemText(0, "")
        self.reis_block_comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"id_\u0440\u0435\u0439\u0441\u0430", None))
        self.reis_block_comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430", None))
        self.reis_block_comboBox.setItemText(3, QCoreApplication.translate("MainWindow_Light", u"\u0412\u0440\u0435\u043c\u044f", None))

        self.reis_block_edit.setText("")
        self.reis_block_edit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.search_reis_block_btn.setText(QCoreApplication.translate("MainWindow_Light", u"\u041f\u043e\u0438\u0441\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.title_label_reis_block.setText(QCoreApplication.translate("MainWindow_Light", u"\u0417\u0430\u0434\u0435\u0440\u0436\u0430\u043d\u043d\u044b\u0435 \u0440\u0435\u0439\u0441\u044b", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow_Light", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow_Light", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow_Light", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow_Light", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow_Light", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow_Light", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow_Light", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow_Light", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow_Light", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow_Light", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow_Light", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow_Light", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow_Light", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow_Light", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow_Light", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow_Light", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow_Light", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow_Light", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow_Light", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow_Light", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.clean_filtr.setText(QCoreApplication.translate("MainWindow_Light", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440", None))
        self.add_row.setText(QCoreApplication.translate("MainWindow_Light", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.update_row.setText(QCoreApplication.translate("MainWindow_Light", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.delete_row.setText(QCoreApplication.translate("MainWindow_Light", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

