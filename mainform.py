# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1149, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1149, 655))
        MainWindow.setMaximumSize(QtCore.QSize(1149, 655))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/alarm_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 1131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 369, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingsButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/settings_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon1)
        self.settingsButton.setIconSize(QtCore.QSize(24, 24))
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout.addWidget(self.settingsButton)
        self.aboutButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/info_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutButton.setIcon(icon2)
        self.aboutButton.setIconSize(QtCore.QSize(24, 24))
        self.aboutButton.setObjectName("aboutButton")
        self.horizontalLayout.addWidget(self.aboutButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(430, 0, 542, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.autoModeButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/flash_auto_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.autoModeButton.setIcon(icon3)
        self.autoModeButton.setIconSize(QtCore.QSize(24, 24))
        self.autoModeButton.setCheckable(True)
        self.autoModeButton.setChecked(True)
        self.autoModeButton.setObjectName("autoModeButton")
        self.horizontalLayout_2.addWidget(self.autoModeButton)
        self.manualModeButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/flash_off_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manualModeButton.setIcon(icon4)
        self.manualModeButton.setIconSize(QtCore.QSize(24, 24))
        self.manualModeButton.setCheckable(True)
        self.manualModeButton.setChecked(False)
        self.manualModeButton.setObjectName("manualModeButton")
        self.horizontalLayout_2.addWidget(self.manualModeButton)
        self.amModeButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/lightning_bolt_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.amModeButton.setIcon(icon5)
        self.amModeButton.setIconSize(QtCore.QSize(24, 24))
        self.amModeButton.setCheckable(True)
        self.amModeButton.setObjectName("amModeButton")
        self.horizontalLayout_2.addWidget(self.amModeButton)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 610, 311, 16))
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 100, 561, 511))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(370, 70, 181, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(190, 90, 181, 301))
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 181, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(370, 90, 181, 301))
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 181, 301))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 181, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 400, 251, 101))
        self.groupBox.setObjectName("groupBox")
        self.manualRingButton = QtWidgets.QPushButton(self.groupBox)
        self.manualRingButton.setGeometry(QtCore.QRect(10, 20, 231, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/alarm_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manualRingButton.setIcon(icon6)
        self.manualRingButton.setIconSize(QtCore.QSize(24, 24))
        self.manualRingButton.setObjectName("manualRingButton")
        self.manualLightButton = QtWidgets.QPushButton(self.groupBox)
        self.manualLightButton.setEnabled(False)
        self.manualLightButton.setGeometry(QtCore.QRect(10, 60, 231, 31))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/light_on_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manualLightButton.setIcon(icon7)
        self.manualLightButton.setIconSize(QtCore.QSize(24, 24))
        self.manualLightButton.setObjectName("manualLightButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 400, 101, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.statusR = QtWidgets.QLabel(self.groupBox_2)
        self.statusR.setGeometry(QtCore.QRect(50, 20, 32, 32))
        self.statusR.setMaximumSize(QtCore.QSize(32, 32))
        self.statusR.setObjectName("statusR")
        self.statusL = QtWidgets.QLabel(self.groupBox_2)
        self.statusL.setGeometry(QtCore.QRect(50, 60, 32, 32))
        self.statusL.setMaximumSize(QtCore.QSize(32, 32))
        self.statusL.setObjectName("statusL")
        self.iconRing = QtWidgets.QLabel(self.groupBox_2)
        self.iconRing.setGeometry(QtCore.QRect(10, 20, 32, 32))
        self.iconRing.setMaximumSize(QtCore.QSize(32, 32))
        self.iconRing.setText("")
        self.iconRing.setPixmap(QtGui.QPixmap("images/notification_32px.png"))
        self.iconRing.setObjectName("iconRing")
        self.iconLight = QtWidgets.QLabel(self.groupBox_2)
        self.iconLight.setGeometry(QtCore.QRect(10, 60, 32, 32))
        self.iconLight.setMaximumSize(QtCore.QSize(32, 32))
        self.iconLight.setText("")
        self.iconLight.setPixmap(QtGui.QPixmap("images/light_on_32px.png"))
        self.iconLight.setObjectName("iconLight")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(380, 400, 171, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(380, 440, 171, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.LightOnLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.LightOnLabel1.setGeometry(QtCore.QRect(380, 420, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LightOnLabel1.setFont(font)
        self.LightOnLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.LightOnLabel1.setObjectName("LightOnLabel1")
        self.LightOffLabel1 = QtWidgets.QLabel(self.groupBox_3)
        self.LightOffLabel1.setGeometry(QtCore.QRect(380, 460, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LightOffLabel1.setFont(font)
        self.LightOffLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.LightOffLabel1.setObjectName("LightOffLabel1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(580, 100, 561, 511))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(370, 70, 181, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_5.setGeometry(QtCore.QRect(190, 90, 181, 301))
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 181, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_6.setGeometry(QtCore.QRect(370, 90, 181, 301))
        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 90, 181, 301))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(190, 70, 181, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 400, 251, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.manualRingButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.manualRingButton_2.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.manualRingButton_2.setIcon(icon6)
        self.manualRingButton_2.setIconSize(QtCore.QSize(24, 24))
        self.manualRingButton_2.setObjectName("manualRingButton_2")
        self.manualLightButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.manualLightButton_2.setEnabled(False)
        self.manualLightButton_2.setGeometry(QtCore.QRect(10, 60, 231, 31))
        self.manualLightButton_2.setIcon(icon7)
        self.manualLightButton_2.setIconSize(QtCore.QSize(24, 24))
        self.manualLightButton_2.setObjectName("manualLightButton_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(270, 400, 101, 101))
        self.groupBox_6.setObjectName("groupBox_6")
        self.statusR_2 = QtWidgets.QLabel(self.groupBox_6)
        self.statusR_2.setGeometry(QtCore.QRect(50, 20, 32, 32))
        self.statusR_2.setMaximumSize(QtCore.QSize(32, 32))
        self.statusR_2.setObjectName("statusR_2")
        self.statusL_2 = QtWidgets.QLabel(self.groupBox_6)
        self.statusL_2.setGeometry(QtCore.QRect(50, 60, 32, 32))
        self.statusL_2.setMaximumSize(QtCore.QSize(32, 32))
        self.statusL_2.setObjectName("statusL_2")
        self.iconRing_2 = QtWidgets.QLabel(self.groupBox_6)
        self.iconRing_2.setGeometry(QtCore.QRect(10, 20, 32, 32))
        self.iconRing_2.setMaximumSize(QtCore.QSize(32, 32))
        self.iconRing_2.setText("")
        self.iconRing_2.setPixmap(QtGui.QPixmap("images/notification_32px.png"))
        self.iconRing_2.setObjectName("iconRing_2")
        self.iconLight_2 = QtWidgets.QLabel(self.groupBox_6)
        self.iconLight_2.setGeometry(QtCore.QRect(10, 60, 32, 32))
        self.iconLight_2.setMaximumSize(QtCore.QSize(32, 32))
        self.iconLight_2.setText("")
        self.iconLight_2.setPixmap(QtGui.QPixmap("images/light_on_32px.png"))
        self.iconLight_2.setObjectName("iconLight_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(380, 400, 171, 16))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.LightOffLabel2 = QtWidgets.QLabel(self.groupBox_4)
        self.LightOffLabel2.setGeometry(QtCore.QRect(380, 460, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LightOffLabel2.setFont(font)
        self.LightOffLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.LightOffLabel2.setObjectName("LightOffLabel2")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(380, 440, 171, 16))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.LightOnLabel2 = QtWidgets.QLabel(self.groupBox_4)
        self.LightOnLabel2.setGeometry(QtCore.QRect(380, 420, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LightOnLabel2.setFont(font)
        self.LightOnLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.LightOnLabel2.setObjectName("LightOnLabel2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1149, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bell Manager"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.settingsButton.setText(_translate("MainWindow", "Настройки"))
        self.aboutButton.setText(_translate("MainWindow", "О программе"))
        self.autoModeButton.setToolTip(_translate("MainWindow", "В автоматическом режиме система сама управляет звонками и освещением по заданному расписанию"))
        self.autoModeButton.setText(_translate("MainWindow", "Авто"))
        self.manualModeButton.setToolTip(_translate("MainWindow", "В ручном режиме звонок и освещение управляются только кнопками ручного управления"))
        self.manualModeButton.setText(_translate("MainWindow", "Ручной"))
        self.amModeButton.setToolTip(_translate("MainWindow", "В полуавтоматическом режиме звонки подаются по расписанию, освещение в ручном режиме"))
        self.amModeButton.setText(_translate("MainWindow", "Полуавтомат"))
        self.label_7.setToolTip(_translate("MainWindow", "Состояние подключения контроллера"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Основная школа"))
        self.label_5.setText(_translate("MainWindow", "Освещение"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.label_3.setText(_translate("MainWindow", "1 смена"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.label_4.setText(_translate("MainWindow", "2 смена"))
        self.groupBox.setTitle(_translate("MainWindow", "Ручное управление"))
        self.manualRingButton.setToolTip(_translate("MainWindow", "Ручная подача звонка"))
        self.manualRingButton.setText(_translate("MainWindow", "Включить звонок"))
        self.manualLightButton.setToolTip(_translate("MainWindow", "Ручное управление освещением"))
        self.manualLightButton.setText(_translate("MainWindow", "Включить/выключить освещение"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Текущий статус"))
        self.statusR.setText(_translate("MainWindow", "R"))
        self.statusL.setText(_translate("MainWindow", "L"))
        self.label_2.setText(_translate("MainWindow", "Текущее расписание:"))
        self.label_6.setText(_translate("MainWindow", "Режим энергосбережения"))
        self.label_13.setText(_translate("MainWindow", "Включение освещения утром"))
        self.label_14.setText(_translate("MainWindow", "Выключение освещения вечером"))
        self.LightOnLabel1.setText(_translate("MainWindow", "--:--"))
        self.LightOffLabel1.setText(_translate("MainWindow", "--:--"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Начальная школа"))
        self.label_8.setText(_translate("MainWindow", "Освещение"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.label_9.setText(_translate("MainWindow", "1 смена"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.label_10.setText(_translate("MainWindow", "2 смена"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Ручное управление"))
        self.manualRingButton_2.setToolTip(_translate("MainWindow", "Ручная подача звонка"))
        self.manualRingButton_2.setText(_translate("MainWindow", "Включить звонок"))
        self.manualLightButton_2.setToolTip(_translate("MainWindow", "Ручное управление освещением"))
        self.manualLightButton_2.setText(_translate("MainWindow", "Включить/выключить освещение"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Текущий статус"))
        self.statusR_2.setText(_translate("MainWindow", "R"))
        self.statusL_2.setText(_translate("MainWindow", "L"))
        self.label_11.setText(_translate("MainWindow", "Текущее расписание:"))
        self.label_12.setText(_translate("MainWindow", "Режим энергосбережения"))
        self.label_17.setText(_translate("MainWindow", "Включение освещения утром"))
        self.LightOffLabel2.setText(_translate("MainWindow", "--:--"))
        self.label_19.setText(_translate("MainWindow", "Выключение освещения вечером"))
        self.LightOnLabel2.setText(_translate("MainWindow", "--:--"))
