# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1059, 442)
        Dialog.setMinimumSize(QtCore.QSize(1059, 442))
        Dialog.setMaximumSize(QtCore.QSize(1059, 442))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/settings_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonCancel = QtWidgets.QPushButton(Dialog)
        self.buttonCancel.setGeometry(QtCore.QRect(970, 410, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonOK = QtWidgets.QPushButton(Dialog)
        self.buttonOK.setGeometry(QtCore.QRect(880, 410, 75, 23))
        self.buttonOK.setAutoDefault(False)
        self.buttonOK.setObjectName("buttonOK")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1041, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(110, 30, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 60, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 90, 141, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 120, 141, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 150, 141, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_6.setGeometry(QtCore.QRect(110, 180, 141, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_19.setObjectName("label_19")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_8.setGeometry(QtCore.QRect(110, 210, 141, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_9.setGeometry(QtCore.QRect(260, 120, 141, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_10.setGeometry(QtCore.QRect(260, 30, 141, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_11.setGeometry(QtCore.QRect(260, 90, 141, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_12 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_12.setGeometry(QtCore.QRect(260, 150, 141, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_13 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_13.setGeometry(QtCore.QRect(260, 210, 141, 22))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_14.setGeometry(QtCore.QRect(260, 60, 141, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_15 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_15.setGeometry(QtCore.QRect(260, 180, 141, 22))
        self.comboBox_15.setObjectName("comboBox_15")
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(110, 10, 121, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(260, 10, 121, 16))
        self.label_28.setObjectName("label_28")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 191, 281))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(460, 0, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 51, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(210, 20, 251, 251))
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(460, 20, 251, 251))
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_4.setGeometry(QtCore.QRect(710, 20, 311, 251))
        self.tableWidget_4.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(710, 0, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(780, 310, 141, 16))
        self.label_11.setObjectName("label_11")
        self.LightOnTime = QtWidgets.QTimeEdit(self.tab)
        self.LightOnTime.setGeometry(QtCore.QRect(940, 310, 71, 22))
        self.LightOnTime.setObjectName("LightOnTime")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(780, 330, 161, 16))
        self.label_12.setObjectName("label_12")
        self.LightOffTime = QtWidgets.QTimeEdit(self.tab)
        self.LightOffTime.setGeometry(QtCore.QRect(940, 330, 71, 22))
        self.LightOffTime.setObjectName("LightOffTime")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(220, 310, 481, 51))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.addNewRaspButton = QtWidgets.QCommandLinkButton(self.tab)
        self.addNewRaspButton.setGeometry(QtCore.QRect(10, 300, 41, 41))
        self.addNewRaspButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/plus_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewRaspButton.setIcon(icon1)
        self.addNewRaspButton.setIconSize(QtCore.QSize(24, 24))
        self.addNewRaspButton.setObjectName("addNewRaspButton")
        self.deleteRaspButton = QtWidgets.QCommandLinkButton(self.tab)
        self.deleteRaspButton.setGeometry(QtCore.QRect(90, 300, 41, 41))
        self.deleteRaspButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/remove_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteRaspButton.setIcon(icon2)
        self.deleteRaspButton.setIconSize(QtCore.QSize(24, 24))
        self.deleteRaspButton.setObjectName("deleteRaspButton")
        self.addLesson1Button = QtWidgets.QCommandLinkButton(self.tab)
        self.addLesson1Button.setGeometry(QtCore.QRect(210, 270, 41, 41))
        self.addLesson1Button.setText("")
        self.addLesson1Button.setIcon(icon1)
        self.addLesson1Button.setIconSize(QtCore.QSize(24, 24))
        self.addLesson1Button.setObjectName("addLesson1Button")
        self.deleteLesson1Button = QtWidgets.QCommandLinkButton(self.tab)
        self.deleteLesson1Button.setGeometry(QtCore.QRect(250, 270, 41, 41))
        self.deleteLesson1Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/delete_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteLesson1Button.setIcon(icon3)
        self.deleteLesson1Button.setIconSize(QtCore.QSize(24, 24))
        self.deleteLesson1Button.setObjectName("deleteLesson1Button")
        self.deleteLesson2Button = QtWidgets.QCommandLinkButton(self.tab)
        self.deleteLesson2Button.setGeometry(QtCore.QRect(500, 270, 41, 41))
        self.deleteLesson2Button.setText("")
        self.deleteLesson2Button.setIcon(icon3)
        self.deleteLesson2Button.setIconSize(QtCore.QSize(24, 24))
        self.deleteLesson2Button.setObjectName("deleteLesson2Button")
        self.addLesson2Button = QtWidgets.QCommandLinkButton(self.tab)
        self.addLesson2Button.setGeometry(QtCore.QRect(460, 270, 41, 41))
        self.addLesson2Button.setText("")
        self.addLesson2Button.setIcon(icon1)
        self.addLesson2Button.setIconSize(QtCore.QSize(24, 24))
        self.addLesson2Button.setObjectName("addLesson2Button")
        self.deleteLightButton = QtWidgets.QCommandLinkButton(self.tab)
        self.deleteLightButton.setGeometry(QtCore.QRect(750, 270, 41, 41))
        self.deleteLightButton.setText("")
        self.deleteLightButton.setIcon(icon3)
        self.deleteLightButton.setIconSize(QtCore.QSize(24, 24))
        self.deleteLightButton.setObjectName("deleteLightButton")
        self.addLightButton = QtWidgets.QCommandLinkButton(self.tab)
        self.addLightButton.setGeometry(QtCore.QRect(710, 270, 41, 41))
        self.addLightButton.setText("")
        self.addLightButton.setIcon(icon1)
        self.addLightButton.setIconSize(QtCore.QSize(24, 24))
        self.addLightButton.setObjectName("addLightButton")
        self.renameRaspButton = QtWidgets.QCommandLinkButton(self.tab)
        self.renameRaspButton.setGeometry(QtCore.QRect(50, 300, 41, 41))
        self.renameRaspButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/edit_property_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renameRaspButton.setIcon(icon4)
        self.renameRaspButton.setIconSize(QtCore.QSize(24, 24))
        self.renameRaspButton.setObjectName("renameRaspButton")
        self.listWidget.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.tableWidget_2.raise_()
        self.tableWidget_4.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.LightOffTime.raise_()
        self.LightOnTime.raise_()
        self.label_17.raise_()
        self.addNewRaspButton.raise_()
        self.deleteRaspButton.raise_()
        self.addLesson1Button.raise_()
        self.deleteLesson1Button.raise_()
        self.deleteLesson2Button.raise_()
        self.addLesson2Button.raise_()
        self.deleteLightButton.raise_()
        self.addLightButton.raise_()
        self.renameRaspButton.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 40, 321, 221))
        self.calendarWidget.setObjectName("calendarWidget")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_7.setGeometry(QtCore.QRect(130, 270, 201, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.addSpecialDayButton = QtWidgets.QCommandLinkButton(self.tab_4)
        self.addSpecialDayButton.setGeometry(QtCore.QRect(340, 40, 131, 41))
        self.addSpecialDayButton.setObjectName("addSpecialDayButton")
        self.deleteSpecialDayButton = QtWidgets.QCommandLinkButton(self.tab_4)
        self.deleteSpecialDayButton.setGeometry(QtCore.QRect(340, 90, 131, 41))
        self.deleteSpecialDayButton.setIcon(icon3)
        self.deleteSpecialDayButton.setIconSize(QtCore.QSize(24, 24))
        self.deleteSpecialDayButton.setObjectName("deleteSpecialDayButton")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_2.setGeometry(QtCore.QRect(480, 40, 471, 301))
        self.listWidget_2.setObjectName("listWidget_2")
        self.comboBox_16 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_16.setGeometry(QtCore.QRect(130, 300, 201, 22))
        self.comboBox_16.setObjectName("comboBox_16")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(10, 270, 111, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(10, 300, 111, 16))
        self.label_26.setObjectName("label_26")
        self.label_29 = QtWidgets.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 631, 16))
        self.label_29.setObjectName("label_29")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 921, 16))
        self.label_14.setObjectName("label_14")
        self.addSpecialRingButton = QtWidgets.QCommandLinkButton(self.tab_5)
        self.addSpecialRingButton.setGeometry(QtCore.QRect(340, 40, 131, 41))
        self.addSpecialRingButton.setObjectName("addSpecialRingButton")
        self.deleteSpecialRingButton = QtWidgets.QCommandLinkButton(self.tab_5)
        self.deleteSpecialRingButton.setGeometry(QtCore.QRect(340, 90, 131, 41))
        self.deleteSpecialRingButton.setIcon(icon3)
        self.deleteSpecialRingButton.setIconSize(QtCore.QSize(24, 24))
        self.deleteSpecialRingButton.setObjectName("deleteSpecialRingButton")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_5)
        self.calendarWidget_2.setGeometry(QtCore.QRect(10, 40, 321, 221))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_3.setGeometry(QtCore.QRect(480, 40, 401, 281))
        self.listWidget_3.setObjectName("listWidget_3")
        self.specialRingTime = QtWidgets.QTimeEdit(self.tab_5)
        self.specialRingTime.setGeometry(QtCore.QRect(60, 270, 81, 22))
        self.specialRingTime.setObjectName("specialRingTime")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.label_16.setObjectName("label_16")
        self.specialRingDuration = QtWidgets.QSpinBox(self.tab_5)
        self.specialRingDuration.setGeometry(QtCore.QRect(310, 270, 51, 22))
        self.specialRingDuration.setMinimum(1)
        self.specialRingDuration.setProperty("value", 5)
        self.specialRingDuration.setObjectName("specialRingDuration")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(150, 270, 161, 16))
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(260, 10, 51, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 50, 51, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(30)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 251, 16))
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_13.setObjectName("label_13")
        self.autoStartCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.autoStartCheckbox.setGeometry(QtCore.QRect(390, 10, 201, 17))
        self.autoStartCheckbox.setObjectName("autoStartCheckbox")
        self.autoOnNewDayCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.autoOnNewDayCheckbox.setGeometry(QtCore.QRect(390, 40, 371, 17))
        self.autoOnNewDayCheckbox.setObjectName("autoOnNewDayCheckbox")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 281, 121))
        self.groupBox.setObjectName("groupBox")
        self.portComboBox = QtWidgets.QComboBox(self.groupBox)
        self.portComboBox.setGeometry(QtCore.QRect(130, 20, 131, 22))
        self.portComboBox.setObjectName("portComboBox")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_21.setObjectName("label_21")
        self.portLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.portLineEdit.setGeometry(QtCore.QRect(130, 50, 131, 20))
        self.portLineEdit.setObjectName("portLineEdit")
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_22.setObjectName("label_22")
        self.portSpeed = QtWidgets.QComboBox(self.groupBox)
        self.portSpeed.setGeometry(QtCore.QRect(130, 80, 131, 22))
        self.portSpeed.setObjectName("portSpeed")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.portSpeed.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 120, 321, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 301, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 100, 301, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(40, 40, 261, 41))
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(40, 120, 261, 41))
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.logCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.logCheckBox.setGeometry(QtCore.QRect(390, 70, 211, 17))
        self.logCheckBox.setObjectName("logCheckBox")
        self.notifyBeforeRing = QtWidgets.QCheckBox(self.tab_2)
        self.notifyBeforeRing.setGeometry(QtCore.QRect(10, 230, 301, 17))
        self.notifyBeforeRing.setObjectName("notifyBeforeRing")
        self.notify1 = QtWidgets.QLineEdit(self.tab_2)
        self.notify1.setGeometry(QtCore.QRect(70, 260, 201, 20))
        self.notify1.setObjectName("notify1")
        self.notify5 = QtWidgets.QLineEdit(self.tab_2)
        self.notify5.setGeometry(QtCore.QRect(70, 290, 201, 20))
        self.notify5.setObjectName("notify5")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(10, 300, 47, 13))
        self.label_31.setObjectName("label_31")
        self.browseNotifyFile1 = QtWidgets.QPushButton(self.tab_2)
        self.browseNotifyFile1.setGeometry(QtCore.QRect(270, 260, 41, 20))
        self.browseNotifyFile1.setObjectName("browseNotifyFile1")
        self.browseNotifyFile5 = QtWidgets.QPushButton(self.tab_2)
        self.browseNotifyFile5.setGeometry(QtCore.QRect(270, 290, 41, 20))
        self.browseNotifyFile5.setObjectName("browseNotifyFile5")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.buttonCancel.setText(_translate("Dialog", "Отмена"))
        self.buttonOK.setText(_translate("Dialog", "OK"))
        self.comboBox.setWhatsThis(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "Понедельник"))
        self.label_5.setText(_translate("Dialog", "Вторник"))
        self.comboBox_2.setWhatsThis(_translate("Dialog", "1"))
        self.comboBox_3.setWhatsThis(_translate("Dialog", "2"))
        self.comboBox_4.setWhatsThis(_translate("Dialog", "3"))
        self.comboBox_5.setWhatsThis(_translate("Dialog", "4"))
        self.comboBox_6.setWhatsThis(_translate("Dialog", "5"))
        self.label_6.setText(_translate("Dialog", "Среда"))
        self.label_7.setText(_translate("Dialog", "Четверг"))
        self.label_8.setText(_translate("Dialog", "Пятница"))
        self.label_9.setText(_translate("Dialog", "Суббота"))
        self.label_19.setText(_translate("Dialog", "Воскресенье"))
        self.comboBox_8.setWhatsThis(_translate("Dialog", "6"))
        self.comboBox_9.setWhatsThis(_translate("Dialog", "10"))
        self.comboBox_10.setWhatsThis(_translate("Dialog", "7"))
        self.comboBox_11.setWhatsThis(_translate("Dialog", "9"))
        self.comboBox_12.setWhatsThis(_translate("Dialog", "11"))
        self.comboBox_13.setWhatsThis(_translate("Dialog", "13"))
        self.comboBox_14.setWhatsThis(_translate("Dialog", "8"))
        self.comboBox_15.setWhatsThis(_translate("Dialog", "12"))
        self.label_27.setText(_translate("Dialog", "Основная школа"))
        self.label_28.setText(_translate("Dialog", "Начальная школа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Менеджер расписаний"))
        self.label_3.setText(_translate("Dialog", "2 смена"))
        self.label.setText(_translate("Dialog", "Расписание"))
        self.label_2.setText(_translate("Dialog", "1 смена"))
        self.tableWidget.setWhatsThis(_translate("Dialog", "Times"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Урок"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Начало"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Конец"))
        self.tableWidget_2.setWhatsThis(_translate("Dialog", "Times2"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Урок"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Начало"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Конец"))
        self.tableWidget_4.setWhatsThis(_translate("Dialog", "Light"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "№"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Начало"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Конец"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Состояние"))
        self.label_10.setText(_translate("Dialog", "Освещение"))
        self.label_11.setText(_translate("Dialog", "Утром свет включается в"))
        self.LightOnTime.setToolTip(_translate("Dialog", "Время включения света утром"))
        self.LightOnTime.setWhatsThis(_translate("Dialog", "LightOn"))
        self.label_12.setText(_translate("Dialog", "Вечером свет выключается в"))
        self.LightOffTime.setToolTip(_translate("Dialog", "Время выключения света вечером"))
        self.LightOffTime.setWhatsThis(_translate("Dialog", "LightOff"))
        self.label_17.setText(_translate("Dialog", "По-умолчанию свет работает синхронно со звонками. В правой таблице можно добавить дополнительные промежутки, когда свет должен быть принудительно включен или выключен"))
        self.addNewRaspButton.setToolTip(_translate("Dialog", "Добавить новое расписание"))
        self.deleteRaspButton.setToolTip(_translate("Dialog", "Удалить расписание"))
        self.addLesson1Button.setToolTip(_translate("Dialog", "Добавить урок"))
        self.deleteLesson1Button.setToolTip(_translate("Dialog", "Удалить урок"))
        self.deleteLesson2Button.setToolTip(_translate("Dialog", "Удалить урок"))
        self.addLesson2Button.setToolTip(_translate("Dialog", "Добавить урок"))
        self.deleteLightButton.setToolTip(_translate("Dialog", "Удалить урок"))
        self.addLightButton.setToolTip(_translate("Dialog", "Добавить урок"))
        self.renameRaspButton.setToolTip(_translate("Dialog", "Переименовать расписание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Расписание уроков"))
        self.addSpecialDayButton.setText(_translate("Dialog", "Добавить"))
        self.deleteSpecialDayButton.setText(_translate("Dialog", "Удалить"))
        self.label_25.setText(_translate("Dialog", "Основная школа"))
        self.label_26.setText(_translate("Dialog", "Начальная школа"))
        self.label_29.setText(_translate("Dialog", "Здесь можно добавить исключения для определённых дат. Например: праздники, каникулы и т.д."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Особенные дни"))
        self.label_14.setText(_translate("Dialog", "Данная опция позволяет включить звонок  в требуемый день и время с требумой продолжительностью. Например, при проведении праздников, учебной тревоги и т.д."))
        self.addSpecialRingButton.setText(_translate("Dialog", "Добавить"))
        self.deleteSpecialRingButton.setText(_translate("Dialog", "Удалить"))
        self.label_16.setText(_translate("Dialog", "Время:"))
        self.label_18.setText(_translate("Dialog", "Продолжительность, секунд:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Особый звонок"))
        self.label_15.setText(_translate("Dialog", "Задержка выключения света на уроке, минут"))
        self.label_13.setText(_translate("Dialog", "Длительность звонка, секунд"))
        self.autoStartCheckbox.setText(_translate("Dialog", "Автозапуск при старте Windows"))
        self.autoOnNewDayCheckbox.setText(_translate("Dialog", "Переключаться в автоматический режим при начале нового дня"))
        self.groupBox.setTitle(_translate("Dialog", "COM-порт"))
        self.label_20.setText(_translate("Dialog", "Windows"))
        self.label_21.setText(_translate("Dialog", "Linux"))
        self.label_22.setText(_translate("Dialog", "Скорость"))
        self.portSpeed.setItemText(0, _translate("Dialog", "600"))
        self.portSpeed.setItemText(1, _translate("Dialog", "1200"))
        self.portSpeed.setItemText(2, _translate("Dialog", "2400"))
        self.portSpeed.setItemText(3, _translate("Dialog", "4800"))
        self.portSpeed.setItemText(4, _translate("Dialog", "9600"))
        self.portSpeed.setItemText(5, _translate("Dialog", "14400"))
        self.portSpeed.setItemText(6, _translate("Dialog", "19200"))
        self.portSpeed.setItemText(7, _translate("Dialog", "28800"))
        self.portSpeed.setItemText(8, _translate("Dialog", "38400"))
        self.portSpeed.setItemText(9, _translate("Dialog", "56000"))
        self.portSpeed.setItemText(10, _translate("Dialog", "57600"))
        self.portSpeed.setItemText(11, _translate("Dialog", "115200"))
        self.groupBox_2.setTitle(_translate("Dialog", "Режим работы"))
        self.radioButton.setText(_translate("Dialog", "Разное расписание для основной и начальной школы"))
        self.radioButton_2.setText(_translate("Dialog", "Одно расписание для всей школы"))
        self.label_23.setText(_translate("Dialog", "Для основной и начальной школы действует индивидуальное расписание звонков и освещения."))
        self.label_24.setText(_translate("Dialog", "Расписание и элементы управления начальной школы игнорируются. Основное расписание применяется для всей школы."))
        self.logCheckBox.setText(_translate("Dialog", "Включить ведение логов"))
        self.notifyBeforeRing.setText(_translate("Dialog", "Звуковые уведомления перед началом урока"))
        self.label_30.setText(_translate("Dialog", "1 минута"))
        self.label_31.setText(_translate("Dialog", "5 минут"))
        self.browseNotifyFile1.setText(_translate("Dialog", "..."))
        self.browseNotifyFile5.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Общие настройки"))
