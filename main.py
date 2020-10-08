#!/usr/bin/python3

'''
TO DO:
* Чистить старые SpecialDays и SpecialRings

'''

VER = "1.0"

import os

def isWindows():
    if os.name == "nt":
        return True
    else:
        return False

import sys  # sys нужен для передачи argv в QApplication
from datetime import datetime
import time
import json
if isWindows():
    print("OS: Windows")
    #print("Import windll module... ", end="")
    #from ctypes import windll
    #print("OK")
else:
    print("OS: Linux")

import serial #pyserial
#Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QLabel, QTimeEdit, QInputDialog, QComboBox
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
#design
import mainform
import settingsform
import aboutform


RusDays = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

'''
Mode:
    0 - автомат
    1 - ручной
    2 - полуавтомат
'''
settings = {
    "Port": {
        "Win": "COM10",
        "Linux": "/dev/ttyACM0",
        "Speed": 9600
    },
    "RingDuration": 5,
    "LightDelay": 2,
    "AutoOnNewDay": True,
    "Mode": 0,
    "IndexesRasp": [1, 1, 1, 1, 2, 1, 0],
    "RaspList": {
        "0": "Выходной",
        "1": "Обычное", 
        "2": "Классный час"
    },
    "Rasp": {
        "1": {
            "LightOn": "7:00",
            "LightOff": "21:00",
            "Times": [
                ["Урок 1", "8:00", "8:40"],
                ["Урок 2", "8:50", "9:30"]
            ],
            "Times2": [
                ["Урок 1", "14:00", "14:40"],
                ["Урок 2", "14:50", "15:30"]
            ],
            "Light": [
                [1, "14:00", "14:40"],
                [0, "8:00", "8:40"]
            ]
        },
        "2": {
            "LightOn": "7:00",
            "LightOff": "21:00",
            "Times": [
                ["Урок 0", "8:00", "8:30"],
                ["Урок 1", "8:35", "9:20"],
                ["Урок 2", "8:35", "9:20"]
            ],
            "Times2": [
                ["Урок 1", "14:00", "14:30"],
                ["Урок 2", "14:35", "15:20"],
                ["Урок 3", "15:35", "16:20"]
            ],
            "Light": [
                [1, "14:00", "14:40"],
                [0, "8:00", "8:40"]
            ]
        }
    },
    "SpecialDays": {
        "24/9/2020": 0,
        "25/9/2020": 2
    },
    "SpecialRings": [
        ["24/9/2020", "13:56", 5],
        ["25/9/2020", "12:00", 5]
    ]
}

#Флаг блокировки изменений в виджетах. Ставить True при загрузке данных на форму
blockChange = False
#Флаг блокировки многократного логирования ошибки порта
lastErrorPort = False

#if isWindows():
#    print("Loading inpout32.dll... ", end="")
#    p = windll.LoadLibrary("inpout32/inpout32.dll")
#    print("OK")
#p.Out32(890, 9)

def logger(msg):
    now = datetime.now()
    s = datetime.strftime(datetime.now(), "%d.%m.%Y  %H:%M:%S")
    s = s + " > " + msg
    f = open("log.txt", "at")
    f.write(s + "\n")
    print(s)
    f.close()

def saveSettings():
    logger("Saving settings.")
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def loadSettings():
    global settings
    logger("Loading settings.")
    with open('settings.json') as f:
        settings = json.load(f)

def openPort():
    global ser
    global lastErrorPort
    speed = settings["Port"]["Speed"]
    ok = True
    if isWindows():
        port = settings["Port"]["Win"]
    else:
        port = settings["Port"]["Linux"]
    try:
        ser = serial.Serial(port, speed)
    except:
        ok = False
    if ok:
        logger("Opened COM-port: " + ser.name)
        lastErrorPort = False
        time.sleep(2)
        writePort(b'Y')
        writePort(b'-')
        writePort(b'-')
        writePort(b'$')
        writePort(b'K')
    else:
        if lastErrorPort == False:
            logger("FAIL: Opening COM-port.")
            lastErrorPort = True
    return ok

def closePort():
    global ser
    try:
        ser.close()
    except:
        pass

def writePort(msg):
    global ser
    global lastErrorPort
    try:
        ser.write(msg)
    except:
        if lastErrorPort == False:
            logger("FAIL: Writing to COM-port.")
            lastErrorPort = True
        closePort()
        openPort()


class SchoolRingerApp(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainform.py
        super().__init__()
        #Флаги включения звонка и освещения
        self.RingOn = False
        self.LightOn = False
        #ID текущего установленного расписания
        self.idr = -1
        #Флаг блокировки повторного автоматического включения звонка в течении минуты после срабатывания
        self.blockRing = False
        #Для обнаружения изменения состояния освещения
        self.lastLightState = False
        #Ручной режим освещения
        self.manualLightOn = False

        self.needLight = False

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.settingsButton.clicked.connect(self.openSettings)
        self.manualRingButton.pressed.connect(self.manualRingPress)
        self.manualRingButton.released.connect(self.manualRingRelease)
        self.manualLightButton.clicked.connect(self.manualLightClick)
        self.manualModeButton.clicked.connect(self.manualModeButtonClick)
        self.autoModeButton.clicked.connect(self.autoModeButtonClick)
        self.amModeButton.clicked.connect(self.amModeButtonClick)

        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_3.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label.setText("")

        self.setWindowTitle("BellManager v" + VER)
        #Читаем настройки
        loadSettings()
        #Запускаем таймер
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(1000)

        self.pixmapRed = QPixmap("images/red.png")
        self.pixmapGreen = QPixmap("images/green.png")
        self.statusR.setPixmap(self.pixmapRed)
        self.statusL.setPixmap(self.pixmapRed)

        openPort()

    #Главный таймер
    def on_timer(self):
        global lastErrorPort
        now = datetime.now()
        s = RusDays[int(datetime.strftime(datetime.now(), "%w"))]
        s = s + datetime.strftime(datetime.now(), "  %d.%m.%Y  %H:%M:%S")

        self.label.setText(s)

        if lastErrorPort:
            self.label_7.setText("Ошибка связи с контроллером!")
        else:
            self.label_7.setText("Контроллер подключен.")

        newidr = self.TodayRasp()
        if newidr != self.idr:
            #Расписание изменилось
            self.idr = newidr
            self.label_2.setText("Текущее расписание: " + settings["RaspList"][str(self.idr)])
            logger("Setting timetable: " + settings["RaspList"][str(self.idr)])
            self.fillTimeTables()
            if self.idr != 0:
                self.crasp = settings["Rasp"][str(self.idr)]

        nowLesson = False

        if self.idr != 0:
            #Проверка совпадений в расписании уроков
            h = int(datetime.strftime(datetime.now(), "%H"))
            m = int(datetime.strftime(datetime.now(), "%M"))
            day = int(datetime.strftime(datetime.now(), "%d"))
            month = int(datetime.strftime(datetime.now(), "%m"))
            year = int(datetime.strftime(datetime.now(), "%Y"))
            mtime = h * 60 + m
            needRing = False
            self.needLight = True
            for item in self.crasp["Times"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson = True
            for item in self.crasp["Times2"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson = True

            if nowLesson:
                self.label_6.setText("Сейчас идёт урок")
            else:
                self.label_6.setText("Сейчас перемена")

            #Проверяем режим энергосбережения утром и вечером
            Lon = list(map(int, self.crasp["LightOn"].split(":")))
            Loff = list(map(int, self.crasp["LightOff"].split(":")))
            timeon = Lon[0] * 60 + Lon[1]
            timeoff = Loff[0] * 60 + Loff[1]
            if (mtime < timeon) or (mtime >= timeoff):
                self.needLight = False
                self.label_6.setText("Режим энергосбережения")

            #Проверяем исключения по освещению
            if len(self.crasp["Light"]) != 0:
                for item in self.crasp["Light"]:
                    ts = list(map(int, item[1].split(":")))
                    te = list(map(int, item[2].split(":")))
                    stime = ts[0] * 60 + ts[1]
                    etime = te[0] * 60 + te[1]
                    if (mtime >= stime) and (mtime < etime):
                        if item[0] == 1:
                            self.needLight = True
                        else:
                            self.needLight = False

            #Проверяем дополнительные звонки
            if len(settings["SpecialRings"]) != 0:
                for item in settings["SpecialRings"]:
                    sday = list(map(int, item[0].split("/")))
                    ts = list(map(int, item[1].split(":")))
                    stime = ts[0] * 60 + ts[1]
                    duration = item[2]
                    if (sday[0] == day) and (sday[1] == month) and (sday[2] == year):
                        if mtime == stime:
                            self.startRing(duration)

        else:
            self.label_6.setText("Режим энергосбережения - выходной")
            needRing = False
            self.needLight = False

        #КОНЕЦ ПРОВЕРОК, передаём управление
        if settings["Mode"] != 1:
            if needRing:
                if self.blockRing == False:
                    self.startRing(settings["RingDuration"])
                #блокируем звонки при следующих итерациях таймера
                self.blockRing = True
            else:
                self.blockRing = False
        if settings["Mode"] == 0:
            self.LightOn = self.needLight
        else:
            self.LightOn = self.manualLightOn;
        if self.LightOn:
            self.LightEnable()
        else:
            self.LightDisable()
        self.UpdateStatus()

    #Обновляем пиктограммы статуса
    def UpdateStatus(self):
        if self.RingOn == True:
            self.statusR.setPixmap(self.pixmapGreen)
        else:
            self.statusR.setPixmap(self.pixmapRed)
        if self.LightOn:
            self.statusL.setPixmap(self.pixmapGreen)
        else:
            self.statusL.setPixmap(self.pixmapRed)

    #Возвращает индекс текущего действующего расписания
    def TodayRasp(self):
        wday = int(datetime.strftime(datetime.now(), "%w"))
        if wday == 0:
            wday = 7
        wday -= 1
        idr = settings["IndexesRasp"][wday]

        #Проверяем особенные дни
        day = int(datetime.strftime(datetime.now(), "%d"))
        month = int(datetime.strftime(datetime.now(), "%m"))
        year = int(datetime.strftime(datetime.now(), "%Y"))
        if len(settings["SpecialDays"]) != 0:
            for item in settings["SpecialDays"]:
                sday = list(map(int, item.split("/")))
                if (day == sday[0]) and (month == sday[1]) and (year == sday[2]):
                    idr = settings["SpecialDays"][item]
                    break

        return idr

    #Заполнение таблиц расписания на главной форме
    def fillTimeTables(self):
        #Заполняем время уроков
        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_3.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_2.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_3.setHorizontalHeaderLabels(["Начало", "Конец"])
        if self.idr == 0:
            self.tableWidget.setRowCount(0)
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_3.setRowCount(0)
            return

        row = 0
        vh = []
        self.tableWidget.setRowCount(len(settings["Rasp"][str(self.idr)]["Times"]))
        for item in settings["Rasp"][str(self.idr)]["Times"]:
            vh.append(item[0])
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[2]))
            row += 1
        self.tableWidget.setVerticalHeaderLabels(vh)

        row = 0
        vh = []
        self.tableWidget_2.setRowCount(len(settings["Rasp"][str(self.idr)]["Times2"]))
        for item in settings["Rasp"][str(self.idr)]["Times2"]:
            vh.append(item[0])
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(item[1]))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(item[2]))
            row += 1
        self.tableWidget_2.setVerticalHeaderLabels(vh)

        row = 0
        vh = []
        self.tableWidget_3.setRowCount(len(settings["Rasp"][str(self.idr)]["Light"]))
        for item in settings["Rasp"][str(self.idr)]["Light"]:
            if item[0] == 1:
                vh.append("Вкл")
            else:
                vh.append("Выкл")
            self.tableWidget_3.setItem(row, 0, QTableWidgetItem(item[1]))
            self.tableWidget_3.setItem(row, 1, QTableWidgetItem(item[2]))
            row += 1
        self.tableWidget_3.setVerticalHeaderLabels(vh)

    def startRing(self, duration):
        if duration != 0:
            self.ringtimer = QtCore.QTimer()
            self.ringtimer.timeout.connect(self.stopRing)
            self.ringtimer.start(duration * 1000)
        logger("Ring start.")
        self.RingOn = True
        writePort(b'Q')
        writePort(b'W')
        self.UpdateStatus()

    def stopRing(self):
        try:
            self.ringtimer.stop()
        except AttributeError:
            pass
        logger("Ring stop.")
        self.RingOn = False
        writePort(b'q')
        writePort(b'w')
        self.UpdateStatus()

    def LightEnable(self):
        if self.lastLightState == False:
            self.lastLightState = True
            logger("Enable light.")
        writePort(b'E')
        writePort(b'R')

    def LightDisable(self):
        if self.lastLightState == True:
            self.lastLightState = False
            logger("Disable light.")
        writePort(b'e')
        writePort(b'r')


    def openSettings(self):
        global blockChange
        logger("Open settings.")
        blockChange = True
        swindow.comboBox.clear()
        swindow.comboBox_2.clear()
        swindow.comboBox_3.clear()
        swindow.comboBox_4.clear()
        swindow.comboBox_5.clear()
        swindow.comboBox_6.clear()
        swindow.comboBox_7.clear()
        swindow.comboBox_8.clear()
        swindow.listWidget.clear()
        swindow.comboBox.addItem("Выходной")
        swindow.comboBox_2.addItem("Выходной")
        swindow.comboBox_3.addItem("Выходной")
        swindow.comboBox_4.addItem("Выходной")
        swindow.comboBox_5.addItem("Выходной")
        swindow.comboBox_6.addItem("Выходной")
        swindow.comboBox_7.addItem("Выходной")
        swindow.comboBox_8.addItem("Выходной")
        for item in settings["RaspList"]:
            if item == "0":
                continue
            swindow.comboBox.addItem(settings["RaspList"][item])
            swindow.comboBox_2.addItem(settings["RaspList"][item])
            swindow.comboBox_3.addItem(settings["RaspList"][item])
            swindow.comboBox_4.addItem(settings["RaspList"][item])
            swindow.comboBox_5.addItem(settings["RaspList"][item])
            swindow.comboBox_6.addItem(settings["RaspList"][item])
            swindow.comboBox_7.addItem(settings["RaspList"][item])
            swindow.comboBox_8.addItem(settings["RaspList"][item])
            swindow.listWidget.addItem(settings["RaspList"][item])
        swindow.spinBox.setValue(settings["RingDuration"])
        swindow.spinBox_2.setValue(settings["LightDelay"])
        swindow.autoOnNewDayCheckbox.setChecked(settings["AutoOnNewDay"])

        swindow.comboBox.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][0])])
        swindow.comboBox_2.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][1])])
        swindow.comboBox_3.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][2])])
        swindow.comboBox_4.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][3])])
        swindow.comboBox_5.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][4])])
        swindow.comboBox_6.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][5])])
        swindow.comboBox_8.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][6])])

        swindow.tableWidget.clear()
        swindow.tableWidget_2.clear()
        swindow.tableWidget_4.clear()
        swindow.tableWidget.setRowCount(0)
        swindow.tableWidget_2.setRowCount(0)
        swindow.tableWidget_4.setRowCount(0)
        swindow.tableWidget.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        swindow.tableWidget_2.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        swindow.tableWidget_4.setHorizontalHeaderLabels(["№", "Начало", "Конец", "Состояние"])

        swindow.specdays = []
        swindow.listWidget_2.clear()
        for item in settings["SpecialDays"]:
            ids = settings["SpecialDays"][item]
            tdate = item.split("/")
            s = str(tdate[0]) + "/"
            if int(tdate[1]) < 10:
                s = s + "0"
            s = s + tdate[1] + "/" + tdate[2] + " - " + settings["RaspList"][str(ids)]
            swindow.listWidget_2.addItem(s)
            swindow.specdays.append(s)

        swindow.listWidget_3.clear()
        row = 0
        for item in settings["SpecialRings"]:
            tdate = list(map(int, item[0].split("/")))
            ttime = list(map(int, item[1].split(":")))
            s = str(row) + " > " + str(tdate[0]) + "/"
            if tdate[1] < 10:
                s = s + "0"
            s = s + str(tdate[1]) + "/" + str(tdate[2]) + "  "
            s = s + str(ttime[0]) + ":"
            if ttime[1] < 10:
                s = s + "0"
            s = s + str(ttime[1]) + " - " + str(item[2]) + ' с.'
            swindow.listWidget_3.addItem(s)
            row += 1

        blockChange = False

        try:
            del(self.CurrentIds)
        except:
            pass
        try:
            del(self.currentSpecialDay)
        except:
            pass
        try:
            del(self.currentSpecialRing)
        except:
            pass

        #Костыль для копирования параметров.
        swindow.sett = json.loads(json.dumps(settings))

        swindow.exec_() #exec_ делает форму модальной

    def autoModeButtonClick(self):
        logger("Auto mode enabled.")
        self.manualModeButton.setChecked(False)
        self.autoModeButton.setChecked(True)
        self.amModeButton.setChecked(False)
        if settings["Mode"] != 0:
            settings["Mode"] = 0
            self.manualLightButton.setEnabled(False)
            saveSettings()

    def manualModeButtonClick(self):
        logger("Manual mode enabled.")
        self.manualModeButton.setChecked(True)
        self.autoModeButton.setChecked(False)
        self.amModeButton.setChecked(False)
        if settings["Mode"] != 1:
            settings["Mode"] = 1
            self.manualLightOn = self.needLight
            self.manualLightButton.setEnabled(True)
            saveSettings()

    def amModeButtonClick(self):
        logger("A/m mode enabled.")
        self.manualModeButton.setChecked(False)
        self.autoModeButton.setChecked(False)
        self.amModeButton.setChecked(True)
        if settings["Mode"] != 2:
            settings["Mode"] = 2
            self.manualLightOn = self.needLight
            self.manualLightButton.setEnabled(True)
            saveSettings()

    def manualRingPress(self):
        logger("Manual ring pressed.")
        self.startRing(0)

    def manualRingRelease(self):
        logger("Manual ring released.")
        self.stopRing()

    def manualLightClick(self):
        self.manualLightOn = not self.manualLightOn
        if self.manualLightOn:
            logger("Manual light enabled.")
        else:
            logger("Manual light disabled.")
        self.UpdateStatus()


class SettingsApp(QtWidgets.QDialog, settingsform.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainform.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.listWidget.itemClicked.connect(self.listRaspClick)
        self.listWidget_2.itemClicked.connect(self.listSpecialDaysClick)
        self.listWidget_3.itemClicked.connect(self.listSpecialRingsClick)
        self.addNewRaspButton.clicked.connect(self.addNewRaspButtonClick)
        self.deleteRaspButton.clicked.connect(self.deleteRaspButtonClick)
        self.renameRaspButton.clicked.connect(self.renameRaspButtonClick)
        self.buttonCancel.clicked.connect(self.buttonCancelClick)
        self.buttonOK.clicked.connect(self.buttonOKClick)
        self.addLesson1Button.clicked.connect(self.addLesson1ButtonClick)
        self.addLesson2Button.clicked.connect(self.addLesson2ButtonClick)
        self.addLightButton.clicked.connect(self.addLightButtonClick)
        self.deleteLesson1Button.clicked.connect(self.deleteLesson1ButtonClick)
        self.deleteLesson2Button.clicked.connect(self.deleteLesson2ButtonClick)
        self.deleteLightButton.clicked.connect(self.deleteLightButtonClick)
        self.tableWidget.cellChanged.connect(self.lessonNameChangeEvent)
        self.tableWidget_2.cellChanged.connect(self.lessonNameChangeEvent)
        self.LightOnTime.timeChanged.connect(self.timeChangeEvent)
        self.LightOffTime.timeChanged.connect(self.timeChangeEvent)
        self.comboBox.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_2.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_3.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_4.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_5.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_6.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_8.currentTextChanged.connect(self.raspDayChanged)
        self.addSpecialDayButton.clicked.connect(self.addSpecialDayButtonClick)
        self.deleteSpecialDayButton.clicked.connect(self.deleteSpecialDayButtonClick)
        self.addSpecialRingButton.clicked.connect(self.addSpecialRingButtonClick)
        self.deleteSpecialRingButton.clicked.connect(self.deleteSpecialRingButtonClick)

    #Обновление списков после изменений в списках расписаний
    def updateLists(self):
        global blockChange
        try:
            del(self.CurrentIds)
        except:
            pass
        try:
            del(self.currentSpecialDay)
        except:
            pass
        try:
            del(self.currentSpecialRing)
        except:
            pass
        blockChange = True
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        self.comboBox_5.clear()
        self.comboBox_6.clear()
        self.comboBox_7.clear()
        self.comboBox_8.clear()
        self.listWidget.clear()
        self.comboBox.addItem("Выходной")
        self.comboBox_2.addItem("Выходной")
        self.comboBox_3.addItem("Выходной")
        self.comboBox_4.addItem("Выходной")
        self.comboBox_5.addItem("Выходной")
        self.comboBox_6.addItem("Выходной")
        self.comboBox_7.addItem("Выходной")
        self.comboBox_8.addItem("Выходной")
        for item in self.sett["RaspList"]:
            if item == "0":
                continue
            self.comboBox.addItem(self.sett["RaspList"][item])
            self.comboBox_2.addItem(self.sett["RaspList"][item])
            self.comboBox_3.addItem(self.sett["RaspList"][item])
            self.comboBox_4.addItem(self.sett["RaspList"][item])
            self.comboBox_5.addItem(self.sett["RaspList"][item])
            self.comboBox_6.addItem(self.sett["RaspList"][item])
            self.comboBox_7.addItem(self.sett["RaspList"][item])
            self.comboBox_8.addItem(self.sett["RaspList"][item])
            self.listWidget.addItem(self.sett["RaspList"][item])

        self.comboBox.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][0])])
        self.comboBox_2.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][1])])
        self.comboBox_3.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][2])])
        self.comboBox_4.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][3])])
        self.comboBox_5.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][4])])
        self.comboBox_6.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][5])])
        self.comboBox_8.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][6])])

        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_4.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        self.tableWidget_2.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        self.tableWidget_4.setHorizontalHeaderLabels(["№", "Начало", "Конец", "Состояние"])

        self.specdays = []
        self.listWidget_2.clear()
        for item in self.sett["SpecialDays"]:
            ids = self.sett["SpecialDays"][item]
            tdate = item.split("/")
            s = str(tdate[0]) + "/"
            if int(tdate[1]) < 10:
                s = s + "0"
            s = s + tdate[1] + "/" + tdate[2] + " - " + self.sett["RaspList"][str(ids)]
            self.listWidget_2.addItem(s)
            self.specdays.append(s)

        self.listWidget_3.clear()
        row = 0
        for item in self.sett["SpecialRings"]:
            tdate = list(map(int, item[0].split("/")))
            ttime = list(map(int, item[1].split(":")))
            s = str(row) + " > " + str(tdate[0]) + "/"
            if tdate[1] < 10:
                s = s + "0"
            s = s + str(tdate[1]) + "/" + str(tdate[2]) + "  "
            s = s + str(ttime[0]) + ":"
            if ttime[1] < 10:
                s = s + "0"
            s = s + str(ttime[1]) + " - " + str(item[2]) + ' с.'
            self.listWidget_3.addItem(s)
            row += 1

        blockChange = False

    #Проверяет существование расписания по его имени
    def raspExistByName(self, name):
        for item in self.sett["RaspList"]:
            if self.sett["RaspList"][item].upper() == name.upper():
                return True
        return False

    #Изменение значений на вкладке "Менеджер расписаний"
    def raspDayChanged(self):
        global blockChange
        if blockChange:
            return

        sender = self.sender()
        try:
            d = int(sender.whatsThis())
        except ValueError:
            return
        s = sender.currentText()
        for item in self.sett["RaspList"]:
            if self.sett["RaspList"][item] == s:
                ids = int(item)
                break

        self.sett["IndexesRasp"][d] = ids

    #Выбор расписания в списке
    def listRaspClick(self, item):
        #print(item.text())
        s = item.text()
        for item in self.sett["RaspList"]:
            if self.sett["RaspList"][item] == s:
                ids = str(item)
                self.CurrentIds = ids #Номер текущего редактируемого расписания
                break

        t = self.sett["Rasp"][ids]["LightOn"].split(":")
        self.LightOnTime.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
        t = self.sett["Rasp"][ids]["LightOff"].split(":")
        self.LightOffTime.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
        
        #Заполняем время уроков
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget.setRowCount(len(self.sett["Rasp"][ids]["Times"]))
        for item in self.sett["Rasp"][ids]["Times"]:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("1" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("2" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget.resizeColumnsToContents()

        self.tableWidget_2.clear()
        self.tableWidget_2.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget_2.setRowCount(len(self.sett["Rasp"][ids]["Times2"]))
        for item in self.sett["Rasp"][ids]["Times2"]:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("3" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("4" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_2.resizeColumnsToContents()

        self.tableWidget_4.clear()
        self.tableWidget_4.setHorizontalHeaderLabels(["№", "Начало", "Конец", "Состояние"])
        row = 0
        self.tableWidget_4.setRowCount(len(self.sett["Rasp"][ids]["Light"]))
        for item in self.sett["Rasp"][ids]["Light"]:
            cb = QComboBox()
            cb.addItems(["Выключить", "Включить"])
            if item[0] == 0:
                cb.setCurrentText("Выключить")
            else:
                cb.setCurrentText("Включить")
            cb.whatsThis = str(row)
            cb.currentTextChanged.connect(self.lightStateChangeEvent)
            self.tableWidget_4.setCellWidget(row, 3, cb)
            self.tableWidget_4.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("5" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("6" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_4.resizeColumnsToContents()

    #Кнопка добавления нового расписания
    def addNewRaspButtonClick(self):
        rcopy = False
        try:
            ids = self.CurrentIds
        except AttributeError:
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Создать копию выделенного расписания вместо создания чистого?")
            msg.setInformativeText(self.sett["RaspList"][str(ids)])
            msg.setWindowTitle("Вопрос")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg.exec_() == QMessageBox.Ok:
                rcopy = True

        while True:
            text, ok = QInputDialog.getText(self, 'Новое расписание', 'Введите название расписания:')
            if ok:
                if not self.raspExistByName(text):
                    self.listWidget.addItem(text)
                    #подбираем ID к новому расписанию
                    newid = 0
                    for item in self.sett["RaspList"]:
                        newid = max(newid, int(item))
                    newid += 1

                    if rcopy:
                        self.sett["RaspList"][str(newid)] = text
                        self.sett["Rasp"][str(newid)] = {}
                        self.sett["Rasp"][str(newid)] = json.loads(json.dumps(self.sett["Rasp"][str(ids)]))
                    else:
                        self.sett["RaspList"][str(newid)] = text
                        self.sett["Rasp"][str(newid)] = {}
                        self.sett["Rasp"][str(newid)]["LightOn"] = "7:00"
                        self.sett["Rasp"][str(newid)]["LightOff"] = "21:00"
                        self.sett["Rasp"][str(newid)]["Times"] = []
                        self.sett["Rasp"][str(newid)]["Times2"] = []
                        self.sett["Rasp"][str(newid)]["Light"] = []

                    self.updateLists()
                    break
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Расписание с таким именем уже существует")
                    #msg.setInformativeText("This is additional information")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
            else:
                break


    #Кнопка удаления расписания
    def deleteRaspButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        if int(ids) in self.sett["IndexesRasp"]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Нельзя удалить расписание, так как оно назначено на один из дней недели.")
            #msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
            return

        for item in self.sett["SpecialDays"]:
            if self.sett["SpecialDays"][item] == ids:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Нельзя удалить расписание, так как оно назначено на один из дней календаря.")
                #msg.setInformativeText("This is additional information")
                msg.setWindowTitle("Ошибка")
                msg.exec_()
                return

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите удалить расписание?")
        msg.setInformativeText(self.sett["RaspList"][str(ids)])
        msg.setWindowTitle("Вопрос")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            self.sett["RaspList"].pop(str(ids))
            self.updateLists()


    #Кнопка переименования расписания
    def renameRaspButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        while True:
            text, ok = QInputDialog.getText(self, 'Переименование', 'Введите новое название расписания:')
            if ok:
                if not self.raspExistByName(text):
                    self.sett["RaspList"][ids] = text
                    self.updateLists()
                    break
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Расписание с таким именем уже существует")
                    #msg.setInformativeText("This is additional information")
                    msg.setWindowTitle("Ошибка")
                    msg.exec_()
            else:
                break


    #Кнопка добавления особенного дня
    def addSpecialDayButtonClick(self):
        date = self.calendarWidget.selectedDate()
        day = date.day()
        month = date.month()
        year = date.year()

        for item in self.sett["RaspList"]:
            if self.sett["RaspList"][item] == self.comboBox_7.currentText():
                ids = int(item)
                break
        
        s = str(day) + "/" + str(month) + "/" + str(year)
        self.sett["SpecialDays"][s] = ids

        self.updateLists()


    #Кнопка удаления особенного дня
    def deleteSpecialDayButtonClick(self):
        try:
            csd = self.currentSpecialDay
        except AttributeError:
            return
        self.sett["SpecialDays"].pop(csd)
        self.updateLists()


    #Клик по списку особенных дней
    def listSpecialDaysClick(self, item):
        s = item.text()
        k = s.split("-")[0].strip()
        t = list(map(int, k.split("/")))
        u = list(map(str, t))
        self.currentSpecialDay = '/'.join(u)
        #print(self.currentSpecialDay)


    #Кнопка добавления особенного звонка
    def addSpecialRingButtonClick(self):
        date = self.calendarWidget_2.selectedDate()
        day = date.day()
        month = date.month()
        year = date.year()
        date = list(map(str, [day, month, year]))
        time = self.specialRingTime.time()
        hour = time.hour()
        minute = time.minute()
        time = list(map(str, [hour, minute]))

        w = ["", "", 0]
        w[0] = '/'.join(date)
        w[1] = ':'.join(time)
        w[2] = self.specialRingDuration.value()
        
        self.sett["SpecialRings"].append(w)
        self.updateLists()


    #Кнопка удаления особенного звонка
    def deleteSpecialRingButtonClick(self):
        try:
            csr = self.currentSpecialRing
        except AttributeError:
            return
        self.sett["SpecialRings"].pop(csr)
        self.updateLists()


    #Клик по списку особенных звонков
    def listSpecialRingsClick(self, item):
        s = item.text()
        self.currentSpecialRing = int(s.split(">")[0].strip())
        #print(self.currentSpecialRing)


    #Событие вызывается при изменении времени в любом timeEdit в таблицах расписания
    def timeChangeEvent(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        sender = self.sender()
        stime = str(sender.time().hour()) + ":" + str(sender.time().minute())

        if sender.whatsThis() == "LightOn":
            self.sett["Rasp"][ids]["LightOn"] = stime
        elif sender.whatsThis() == "LightOff":
            self.sett["Rasp"][ids]["LightOff"] = stime
        else:
            t = sender.whatsThis().split("_")
            row = int(t[1])
            tag = int(t[0])
            if tag <= 2:
                s = "Times"
            elif tag <= 4:
                s = "Times2"
                tag -= 2
            else:
                s = "Light"
                tag -= 4

            self.sett["Rasp"][ids][s][row][tag] = stime
        #print(row,tag)
        #print(self.sett["Rasp"][ids][s])


    #Событие вызывается при смене названия урока
    def lessonNameChangeEvent(self, row, column):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        sender = self.sender()
        s = sender.whatsThis()
        name = sender.item(row, column).text()
        self.sett["Rasp"][ids][s][row][0] = name
        #print(self.sett["Rasp"][ids][s])


    #Событие вызывается при изменении комбобокса вкл/выкл в расписании освещения
    def lightStateChangeEvent(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        sender = self.sender()
        row = int(sender.whatsThis)
        if sender.currentText() == "Включить":
            state = 1
        else:
            state = 0

        self.sett["Rasp"][ids]["Light"][row][0] = state
        #print(self.sett["Rasp"][ids]["Light"])


    #Кнопка добавления урока в 1 смену
    def addLesson1ButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        self.sett["Rasp"][ids]["Times"].append(["Урок", "0:00", "0:00"])

        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget.setRowCount(len(self.sett["Rasp"][ids]["Times"]))
        for item in self.sett["Rasp"][ids]["Times"]:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("1" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("2" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget.resizeColumnsToContents()


    #Кнопка добавления урока в 2 смену
    def addLesson2ButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        self.sett["Rasp"][ids]["Times2"].append(["Урок", "0:00", "0:00"])

        self.tableWidget_2.clear()
        self.tableWidget_2.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget_2.setRowCount(len(self.sett["Rasp"][ids]["Times2"]))
        for item in self.sett["Rasp"][ids]["Times2"]:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("3" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("4" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_2.resizeColumnsToContents()


    #Кнопка добавления освещения
    def addLightButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        self.sett["Rasp"][ids]["Light"].append([0, "0:00", "0:00"])

        self.tableWidget_4.clear()
        self.tableWidget_4.setHorizontalHeaderLabels(["№", "Начало", "Конец", "Состояние"])
        row = 0
        self.tableWidget_4.setRowCount(len(self.sett["Rasp"][ids]["Light"]))
        for item in self.sett["Rasp"][ids]["Light"]:
            cb = QComboBox()
            cb.addItems(["Выключить", "Включить"])
            if item[0] == 0:
                cb.setCurrentText("Выключить")
            else:
                cb.setCurrentText("Включить")
            cb.whatsThis = str(row)
            cb.currentTextChanged.connect(self.lightStateChangeEvent)
            self.tableWidget_4.setCellWidget(row, 3, cb)
            self.tableWidget_4.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("5" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("6" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_4.resizeColumnsToContents()


    #Кнопка удаления урока в 1 смену
    def deleteLesson1ButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return
        curRow = self.tableWidget.currentRow()
        if curRow == -1:
            return

        self.sett["Rasp"][ids]["Times"].pop(curRow)

        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget.setRowCount(len(self.sett["Rasp"][ids]["Times"]))
        for item in self.sett["Rasp"][ids]["Times"]:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("1" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("2" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget.resizeColumnsToContents()


    #Кнопка удаления урока в 2 смену
    def deleteLesson2ButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return
        curRow = self.tableWidget_2.currentRow()
        if curRow == -1:
            return

        self.sett["Rasp"][ids]["Times2"].pop(curRow)

        self.tableWidget_2.clear()
        self.tableWidget_2.setHorizontalHeaderLabels(["Урок", "Начало", "Конец"])
        row = 0
        self.tableWidget_2.setRowCount(len(self.sett["Rasp"][ids]["Times2"]))
        for item in self.sett["Rasp"][ids]["Times2"]:
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(item[0]))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("3" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("4" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_2.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_2.resizeColumnsToContents()


    #Кнопка удаления освещения
    def deleteLightButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return
        curRow = self.tableWidget_4.currentRow()
        if curRow == -1:
            return

        self.sett["Rasp"][ids]["Light"].pop(curRow)

        self.tableWidget_4.clear()
        self.tableWidget_4.setHorizontalHeaderLabels(["Начало", "Конец", "Состояние"])
        row = 0
        self.tableWidget_4.setRowCount(len(self.sett["Rasp"][ids]["Light"]))
        for item in self.sett["Rasp"][ids]["Light"]:
            cb = QComboBox()
            cb.addItems(["Выключить", "Включить"])
            if item[0] == 0:
                cb.setCurrentText("Выключить")
            else:
                cb.setCurrentText("Включить")
            cb.whatsThis = str(row)
            cb.currentTextChanged.connect(self.lightStateChangeEvent)
            self.tableWidget_4.setCellWidget(row, 3, cb)
            self.tableWidget_4.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[1].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("5" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 1, te)
            te = QTimeEdit()
            te.setGeometry(QtCore.QRect(100, 100, 100, 100))
            t = item[2].split(":")
            te.setTime(QtCore.QTime(int(t[0]), int(t[1]), 0))
            te.setWhatsThis("6" + "_" + str(row))
            te.timeChanged.connect(self.timeChangeEvent)
            self.tableWidget_4.setCellWidget(row, 2, te)
            row += 1
        self.tableWidget_4.resizeColumnsToContents()


    #Нажатие кнопки "Отмена"
    def buttonCancelClick(self):
        logger("Settings closed. Canceled.")
        swindow.close()


    #Нажатие кнопки "OK"
    def buttonOKClick(self):
        global settings
        logger("Settings closed. Saved.")

        settings = json.loads(json.dumps(self.sett))
        saveSettings()
        window.idr = -1
        swindow.close()



class AboutApp(QtWidgets.QDialog, aboutform.Ui_AboutDialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainform.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        
def main():
    logger("********** Starting application. **********")
    global swindow
    global window
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SchoolRingerApp()  # Создаём объект класса SchoolRingerApp
    window.show()  # Показываем окно
    swindow = SettingsApp()
    aboutwindow = AboutApp()
    
    app.exec_()  # и запускаем приложение
    logger("********** Terminating application. **********")


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
