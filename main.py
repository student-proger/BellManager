#!/usr/bin/python3

'''
* Author:         Gladyshev Dmitriy (2020) 
* 
* Design Name:    BellManager
* Description:    Программа для управления освещением и звонками в школе
'''

VER = "2.0.2"

import os
import sys  # sys нужен для передачи argv в QApplication
from datetime import datetime
import time
import json

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
    "IndexesRasp": [1, 1, 1, 1, 1, 3, 0],
    "IndexesRaspN": [1, 1, 1, 1, 1, 0, 0],
    "RaspList": {
        "0": "Выходной",
        "1": "Обычное",
        "2": "Классный час",
        "3": "Суббота основное"
    },
    "Rasp": {
        "1": {
            "LightOn": "7:00",
            "LightOff": "21:00",
            "Times": [
                ["Урок 1", "8:0", "8:40"],
                ["Урок 2", "8:50", "9:30"],
                ["Урок 3", "9:40", "10:20"],
                ["Урок 4", "10:30", "11:10"],
                ["Урок 5", "11:30", "12:10"],
                ["Урок 6", "12:15", "12:55"]
            ],
            "Times2": [
                ["Урок 1", "13:0", "13:35"],
                ["Урок 2", "13:45", "14:20"],
                ["Урок 3", "14:40", "15:15"],
                ["Урок 4", "15:25", "16:0"],
                ["Урок 5", "16:10", "16:45"],
                ["Урок 6", "16:55", "17:30"]
            ],
            "Light": [
            ]
        },
        "2": {
            "LightOn": "7:00",
            "LightOff": "21:00",
            "Times": [
                ["Урок 1", "8:0", "8:40"],
                ["Урок 2", "8:45", "9:25"],
                ["Урок 3", "9:40", "10:20"],
                ["Урок 4", "10:35", "11:15"],
                ["Урок 5", "11:30", "12:10"],
                ["Урок 6", "12:15", "12:55"],
                ["Кл.час", "13:00", "13:20"]
            ],
            "Times2": [
                ["Кл.час", "13:30", "13:50"],
                ["Урок 1", "13:55", "14:35"],
                ["Урок 2", "14:50", "15:30"],
                ["Урок 3", "15:35", "16:15"],
                ["Урок 4", "16:20", "17:0"],
                ["Урок 5", "17:5", "17:45"],
                ["Урок 6", "17:50", "18:30"]
            ],
            "Light": [
            ]
        },
        "3": {
            "LightOn": "7:00",
            "LightOff": "20:00",
            "Times": [
                ["Урок 1", "8:0", "8:40"],
                ["Урок 2", "8:45", "9:25"],
                ["Урок 3", "9:40", "10:20"],
                ["Урок 4", "10:35", "11:15"]
            ],
            "Times2": [
            ],
            "Light": [
                [0, "12:0", "18:0"]
            ]
        }
    },
    "SpecialRings": [
        ["24/9/2020", "13:56", 5],
        ["25/9/2020", "12:00", 5]
    ],
    "SpecDays": {
        "24/9/2020": "0:0",
        "25/9/2020": "2:1"
    },
}

#Флаг блокировки изменений в виджетах. Ставить True при загрузке данных на форму
blockChange = False
#Флаг блокировки многократного логирования ошибки порта
lastErrorPort = False


def messageBox(title, s):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(s)
    msg.setWindowTitle(title)
    msg.exec_()


def logger(msg):
    if settings["EnableLog"]:
        now = datetime.now()
        ss = datetime.strftime(datetime.now(), "%Y-%m")
        s = datetime.strftime(datetime.now(), "%d.%m.%Y  %H:%M:%S")
        s = s + " > " + msg
        f = open("log/log" + ss + ".txt", "at")
        f.write(s + "\n")
        print(s)
        f.close()


def isWindows():
    if os.name == "nt":
        return True
    else:
        return False


def saveSettings():
    logger("Сохранение настроек.")
    try:
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
    except:
        logger("ОШИБКА: Не удалось сохранить настройки.")
        messageBox("Критическая ошибка", "Ошибка сохранения файла настроек. Возможно нет прав доступа на запись.")


def loadSettings():
    global settings
    try:
        with open('settings.json') as f:
            settings = json.load(f)
    except FileNotFoundError:
        pass
    except:
        messageBox("Критическая ошибка", "Ошибка чтения файла настроек. Возможно нет прав доступа на чтение.")


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
        logger("Открытие COM-порта: " + ser.name)
        lastErrorPort = False
        time.sleep(2)
        writePort(b'Y')
        writePort(b'-')
        writePort(b'-')
        writePort(b'$')
        writePort(b'K')
    else:
        if lastErrorPort == False:
            logger("ОШИБКА: Не удалось открыть COM-порт.")
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
            logger("ОШИБКА: Не удалось отправить информацию в COM-порт.")
            lastErrorPort = True
        closePort()
        openPort()



class SchoolRingerApp(QtWidgets.QMainWindow, mainform.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainform.py
        super().__init__()

        #Читаем настройки
        loadSettings()

        #Для обратной совместимости с предыдущими версиями проверяем настройки
        if not "IndexesRaspN" in settings:
            settings["IndexesRaspN"] = [0, 0, 0, 0, 0, 0, 0]
        if not "SpecDays" in settings:
            settings["SpecDays"] = {}
        if not "EnableLog" in settings:
            settings["EnableLog"] = True

        logger("********** Запуск приложения **********")
        if isWindows():
            print("OS: Windows")
            #print(sys.argv[0])
        else:
            print("OS: Linux")

        self.ringtimer = [QtCore.QTimer(), QtCore.QTimer()]
        #Флаги включения звонка и освещения
        self.RingOn = [False, False]
        self.LightOn = [False, False]
        #ID текущего установленного расписания
        self.idr = [-1, -1]
        self.crasp = [0, 0]
        #Флаг блокировки повторного автоматического включения звонка в течении минуты после срабатывания
        self.blockRing = [False, False]
        #Для обнаружения изменения состояния освещения
        self.lastLightState = [False, False]
        #Ручной режим освещения
        self.manualLightOn = [False, False]

        self.needLight = [False, False]

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.settingsButton.clicked.connect(self.openSettings)
        self.manualRingButton.pressed.connect(self.manualRingPress)
        self.manualRingButton.released.connect(self.manualRingRelease)
        self.manualLightButton.clicked.connect(self.manualLightClick)
        self.manualModeButton.clicked.connect(self.manualModeButtonClick)
        self.manualRingButton_2.pressed.connect(self.manualRingNPress)
        self.manualRingButton_2.released.connect(self.manualRingNRelease)
        self.manualLightButton_2.clicked.connect(self.manualLightNClick)
        self.autoModeButton.clicked.connect(self.autoModeButtonClick)
        self.amModeButton.clicked.connect(self.amModeButtonClick)
        self.aboutButton.clicked.connect(self.aboutButtonClick)

        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_3.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3.setRowCount(0)
        self.label.setText("")

        self.setWindowTitle("Bell Manager v" + VER)

        if settings["Mode"] == 0:
            logger("Автоматический режим включён.")
            self.manualModeButton.setChecked(False)
            self.autoModeButton.setChecked(True)
            self.amModeButton.setChecked(False)
            self.manualLightButton.setEnabled(False)
            self.manualLightButton_2.setEnabled(False)
        elif settings["Mode"] == 1:
            logger("Ручной режим включён.")
            self.manualModeButton.setChecked(True)
            self.autoModeButton.setChecked(False)
            self.amModeButton.setChecked(False)
            self.manualLightButton.setEnabled(True)
            self.manualLightButton_2.setEnabled(True)
        else:
            logger("Полуавтоматический режим включён.")
            self.manualModeButton.setChecked(False)
            self.autoModeButton.setChecked(False)
            self.amModeButton.setChecked(True)
            self.manualLightButton.setEnabled(True)
            self.manualLightButton_2.setEnabled(True)

        #Запускаем главный таймер
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(1000)

        self.pixmapRed = QPixmap("images/red.png")
        self.pixmapGreen = QPixmap("images/green.png")
        self.statusR.setPixmap(self.pixmapRed)
        self.statusL.setPixmap(self.pixmapRed)
        self.statusR_2.setPixmap(self.pixmapRed)
        self.statusL_2.setPixmap(self.pixmapRed)

        openPort()


    #Главный таймер
    def on_timer(self):
        global lastErrorPort
        newidr = [-1, -1]
        needRing = [False, False]

        now = datetime.now()
        s = RusDays[int(datetime.strftime(datetime.now(), "%w"))]
        s = s + datetime.strftime(datetime.now(), "  %d.%m.%Y  %H:%M:%S")

        self.label.setText(s)

        #Переход в автоматический режим в начале следующих суток
        ht = int(datetime.strftime(datetime.now(), "%H"))
        mt = int(datetime.strftime(datetime.now(), "%M"))
        if (ht == 0) and (mt < 1) and (settings["AutoOnNewDay"] == True):
            if settings["Mode"] != 0:
                logger("Автоматический режим включён.")
                self.manualModeButton.setChecked(False)
                self.autoModeButton.setChecked(True)
                self.amModeButton.setChecked(False)
                self.manualLightButton.setEnabled(False)
                self.manualLightButton_2.setEnabled(False)

        if lastErrorPort:
            self.label_7.setText("Ошибка связи с контроллером!")
        else:
            self.label_7.setText("Контроллер подключен.")

        changed = False

        newidr[0] = self.TodayRasp(0)
        if newidr[0] != self.idr[0]:
            #Расписание изменилось
            self.idr[0] = newidr[0]
            self.label_2.setText("Текущее расписание: " + settings["RaspList"][str(self.idr[0])])
            logger("Установка расписания: " + settings["RaspList"][str(self.idr[0])])
            changed = True
            if self.idr[0] != 0:
                self.crasp[0] = settings["Rasp"][str(self.idr[0])]

        newidr[1] = self.TodayRasp(1)
        if newidr[1] != self.idr[1]:
            #Расписание изменилось
            self.idr[1] = newidr[1]
            self.label_11.setText("Текущее расписание: " + settings["RaspList"][str(self.idr[1])])
            logger("Установка расписания в началке: " + settings["RaspList"][str(self.idr[1])])
            changed = True
            if self.idr[1] != 0:
                self.crasp[1] = settings["Rasp"][str(self.idr[1])]

        if changed:
            self.fillTimeTables()

        nowLesson = [False, False]

        h = int(datetime.strftime(datetime.now(), "%H"))
        m = int(datetime.strftime(datetime.now(), "%M"))
        day = int(datetime.strftime(datetime.now(), "%d"))
        month = int(datetime.strftime(datetime.now(), "%m"))
        year = int(datetime.strftime(datetime.now(), "%Y"))

        if self.idr[0] != 0:
            #Проверка совпадений в расписании уроков
            mtime = h * 60 + m
            needRing[0] = False
            self.needLight[0] = True
            for item in self.crasp[0]["Times"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing[0] = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight[0] = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson[0] = True
            for item in self.crasp[0]["Times2"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing[0] = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight[0] = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson[0] = True

            if nowLesson[0]:
                self.label_6.setText("Сейчас идёт урок")
            else:
                self.label_6.setText("Сейчас перемена")

            #Проверяем режим энергосбережения утром и вечером
            Lon = list(map(int, self.crasp[0]["LightOn"].split(":")))
            Loff = list(map(int, self.crasp[0]["LightOff"].split(":")))
            timeon = Lon[0] * 60 + Lon[1]
            timeoff = Loff[0] * 60 + Loff[1]
            if (mtime < timeon) or (mtime >= timeoff):
                self.needLight[0] = False
                self.label_6.setText("Режим энергосбережения")

            #Проверяем исключения по освещению
            if len(self.crasp[0]["Light"]) != 0:
                for item in self.crasp[0]["Light"]:
                    ts = list(map(int, item[1].split(":")))
                    te = list(map(int, item[2].split(":")))
                    stime = ts[0] * 60 + ts[1]
                    etime = te[0] * 60 + te[1]
                    if (mtime >= stime) and (mtime < etime):
                        if item[0] == 1:
                            self.needLight[0] = True
                        else:
                            self.needLight[0] = False

        else:
            self.label_6.setText("Режим энергосбережения - выходной")
            needRing[0] = False
            self.needLight[0] = False

        if self.idr[1] != 0:
            #Проверка совпадений в расписании уроков началки
            mtime = h * 60 + m
            needRing[1] = False
            self.needLight[1] = True
            for item in self.crasp[1]["Times"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing[1] = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight[1] = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson[1] = True
            for item in self.crasp[1]["Times2"]:
                ts = list(map(int, item[1].split(":")))
                te = list(map(int, item[2].split(":")))
                stime = ts[0] * 60 + ts[1]
                etime = te[0] * 60 + te[1]
                if (mtime == stime) or (mtime == etime):
                    needRing[1] = True
                if (mtime >= stime + settings["LightDelay"]) and (mtime < etime):
                    self.needLight[1] = False
                if (mtime >= stime) and (mtime < etime):
                    nowLesson[1] = True

            if nowLesson[1]:
                self.label_12.setText("Сейчас идёт урок")
            else:
                self.label_12.setText("Сейчас перемена")

            #Проверяем режим энергосбережения утром и вечером
            Lon = list(map(int, self.crasp[1]["LightOn"].split(":")))
            Loff = list(map(int, self.crasp[1]["LightOff"].split(":")))
            timeon = Lon[0] * 60 + Lon[1]
            timeoff = Loff[0] * 60 + Loff[1]
            if (mtime < timeon) or (mtime >= timeoff):
                self.needLight[1] = False
                self.label_12.setText("Режим энергосбережения")

            #Проверяем исключения по освещению
            if len(self.crasp[1]["Light"]) != 0:
                for item in self.crasp[1]["Light"]:
                    ts = list(map(int, item[1].split(":")))
                    te = list(map(int, item[2].split(":")))
                    stime = ts[0] * 60 + ts[1]
                    etime = te[0] * 60 + te[1]
                    if (mtime >= stime) and (mtime < etime):
                        if item[0] == 1:
                            self.needLight[1] = True
                        else:
                            self.needLight[1] = False
        else:
            self.label_12.setText("Режим энергосбережения - выходной")
            needRing[1] = False
            self.needLight[1] = False

        #Проверяем дополнительные звонки
        if len(settings["SpecialRings"]) != 0:
            for item in settings["SpecialRings"]:
                sday = list(map(int, item[0].split("/")))
                ts = list(map(int, item[1].split(":")))
                stime = ts[0] * 60 + ts[1]
                duration = item[2]
                if (sday[0] == day) and (sday[1] == month) and (sday[2] == year):
                    if mtime == stime:
                        self.startRing(duration, 0)
                        self.startRing(duration, 1)

        #КОНЕЦ ПРОВЕРОК, передаём управление
        if settings["Mode"] != 1:
            if needRing[0]:
                if self.blockRing[0] == False:
                    self.startRing(settings["RingDuration"], 0)
                #блокируем звонки при следующих итерациях таймера
                self.blockRing[0] = True
            else:
                self.blockRing[0] = False

            if needRing[1]:
                if self.blockRing[1] == False:
                    self.startRing(settings["RingDuration"], 1)
                #блокируем звонки при следующих итерациях таймера
                self.blockRing[1] = True
            else:
                self.blockRing[1] = False


        if settings["Mode"] == 0:
            self.LightOn[0] = self.needLight[0]
            self.LightOn[1] = self.needLight[1]
        else:
            self.LightOn[0] = self.manualLightOn[0];
            self.LightOn[1] = self.manualLightOn[1];
        if self.LightOn[0]:
            self.LightEnable(0)
        else:
            self.LightDisable(0)
        if self.LightOn[1]:
            self.LightEnable(1)
        else:
            self.LightDisable(1)
        self.UpdateStatus()


    #Обновляем пиктограммы статуса
    def UpdateStatus(self):
        if self.RingOn[0] == True:
            self.statusR.setPixmap(self.pixmapGreen)
        else:
            self.statusR.setPixmap(self.pixmapRed)
        if self.LightOn[0]:
            self.statusL.setPixmap(self.pixmapGreen)
        else:
            self.statusL.setPixmap(self.pixmapRed)

        if self.RingOn[1] == True:
            self.statusR_2.setPixmap(self.pixmapGreen)
        else:
            self.statusR_2.setPixmap(self.pixmapRed)
        if self.LightOn[1]:
            self.statusL_2.setPixmap(self.pixmapGreen)
        else:
            self.statusL_2.setPixmap(self.pixmapRed)


    #"7:5" --> "7:05"
    def formatTime(self, s):
        t = list(map(int, s.split(":")))
        ss = str(t[0]) + ":"
        if t[1] < 10:
            ss = ss + "0"
        ss = ss + str(t[1])
        return ss


    #Возвращает индекс текущего действующего расписания
    #index: 0 - основная, 1 - началка
    def TodayRasp(self, index):
        wday = int(datetime.strftime(datetime.now(), "%w"))
        if wday == 0:
            wday = 7
        wday -= 1
        if index == 0:
            idr = settings["IndexesRasp"][wday]
        else:
            idr = settings["IndexesRaspN"][wday]

        #Проверяем особенные дни
        day = int(datetime.strftime(datetime.now(), "%d"))
        month = int(datetime.strftime(datetime.now(), "%m"))
        year = int(datetime.strftime(datetime.now(), "%Y"))
        if len(settings["SpecDays"]) != 0:
            for item in settings["SpecDays"]:
                sday = list(map(int, item.split("/")))
                if (day == sday[0]) and (month == sday[1]) and (year == sday[2]):
                    k = list(map(int, settings["SpecDays"][item].split(":")))
                    idr = k[index]
                    break

        return idr


    #Заполнение таблиц расписания на главной форме
    def fillTimeTables(self):
        #Заполняем время уроков
        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_3.clear()
        self.tableWidget_4.clear()
        self.tableWidget_5.clear()
        self.tableWidget_6.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_2.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_3.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_4.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_5.setHorizontalHeaderLabels(["Начало", "Конец"])
        self.tableWidget_6.setHorizontalHeaderLabels(["Начало", "Конец"])

        if self.idr[0] == 0:
            self.tableWidget.setRowCount(0)
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_3.setRowCount(0)
        else:
            row = 0
            vh = []
            self.tableWidget.setRowCount(len(settings["Rasp"][str(self.idr[0])]["Times"]))
            for item in settings["Rasp"][str(self.idr[0])]["Times"]:
                vh.append(item[0])
                self.tableWidget.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget.setVerticalHeaderLabels(vh)
            self.tableWidget.resizeColumnsToContents()

            row = 0
            vh = []
            self.tableWidget_2.setRowCount(len(settings["Rasp"][str(self.idr[0])]["Times2"]))
            for item in settings["Rasp"][str(self.idr[0])]["Times2"]:
                vh.append(item[0])
                self.tableWidget_2.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget_2.setVerticalHeaderLabels(vh)
            self.tableWidget_2.resizeColumnsToContents()

            row = 0
            vh = []
            self.tableWidget_3.setRowCount(len(settings["Rasp"][str(self.idr[0])]["Light"]))
            for item in settings["Rasp"][str(self.idr[0])]["Light"]:
                if item[0] == 1:
                    vh.append("Вкл")
                else:
                    vh.append("Выкл")
                self.tableWidget_3.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget_3.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget_3.setVerticalHeaderLabels(vh)
            self.tableWidget_3.resizeColumnsToContents()

        if self.idr[1] == 0:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_6.setRowCount(0)
        else:
            row = 0
            vh = []
            self.tableWidget_4.setRowCount(len(settings["Rasp"][str(self.idr[1])]["Times"]))
            for item in settings["Rasp"][str(self.idr[1])]["Times"]:
                vh.append(item[0])
                self.tableWidget_4.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget_4.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget_4.setVerticalHeaderLabels(vh)
            self.tableWidget_4.resizeColumnsToContents()

            row = 0
            vh = []
            self.tableWidget_5.setRowCount(len(settings["Rasp"][str(self.idr[1])]["Times2"]))
            for item in settings["Rasp"][str(self.idr[1])]["Times2"]:
                vh.append(item[0])
                self.tableWidget_5.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget_5.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget_5.setVerticalHeaderLabels(vh)
            self.tableWidget_5.resizeColumnsToContents()

            row = 0
            vh = []
            self.tableWidget_6.setRowCount(len(settings["Rasp"][str(self.idr[1])]["Light"]))
            for item in settings["Rasp"][str(self.idr[1])]["Light"]:
                if item[0] == 1:
                    vh.append("Вкл")
                else:
                    vh.append("Выкл")
                self.tableWidget_6.setItem(row, 0, QTableWidgetItem(self.formatTime(item[1])))
                self.tableWidget_6.setItem(row, 1, QTableWidgetItem(self.formatTime(item[2])))
                row += 1
            self.tableWidget_6.setVerticalHeaderLabels(vh)
            self.tableWidget_6.resizeColumnsToContents()
        


    def startRing(self, duration, index):
        if duration != 0:
            self.ringtimer[index].timeout.connect(lambda: self.stopRing(index))
            self.ringtimer[index].start(duration * 1000)
        logger("Звонок включен.")
        self.RingOn[index] = True
        if index == 0:
            writePort(b'Q')
        else:
            writePort(b'W')
        self.UpdateStatus()


    def stopRing(self, index):
        try:
            self.ringtimer[index].stop()
        except AttributeError:
            pass
        logger("Звонок выключен.")
        self.RingOn[index] = False
        if index == 0:
            writePort(b'q')
        else:
            writePort(b'w')
        self.UpdateStatus()


    def LightEnable(self, index):
        if self.lastLightState[index] == False:
            self.lastLightState[index] = True
            logger("Освещение включено.")
        if index == 0:
            writePort(b'E')
        else:
            writePort(b'R')


    def LightDisable(self, index):
        if self.lastLightState[index] == True:
            self.lastLightState[index] = False
            logger("Освещение выключено.")
        if index == 0:
            writePort(b'e')
        else:
            writePort(b'r')


    def openSettings(self):
        global blockChange
        logger("Открытие настроек.")
        blockChange = True
        swindow.comboBox.clear()
        swindow.comboBox_2.clear()
        swindow.comboBox_3.clear()
        swindow.comboBox_4.clear()
        swindow.comboBox_5.clear()
        swindow.comboBox_6.clear()
        swindow.comboBox_7.clear()
        swindow.comboBox_8.clear()
        swindow.comboBox_9.clear()
        swindow.comboBox_10.clear()
        swindow.comboBox_11.clear()
        swindow.comboBox_12.clear()
        swindow.comboBox_13.clear()
        swindow.comboBox_14.clear()
        swindow.comboBox_15.clear()
        swindow.comboBox_16.clear()
        swindow.listWidget.clear()
        swindow.comboBox.addItem("Выходной")
        swindow.comboBox_2.addItem("Выходной")
        swindow.comboBox_3.addItem("Выходной")
        swindow.comboBox_4.addItem("Выходной")
        swindow.comboBox_5.addItem("Выходной")
        swindow.comboBox_6.addItem("Выходной")
        swindow.comboBox_7.addItem("Выходной")
        swindow.comboBox_8.addItem("Выходной")
        swindow.comboBox_9.addItem("Выходной")
        swindow.comboBox_10.addItem("Выходной")
        swindow.comboBox_11.addItem("Выходной")
        swindow.comboBox_12.addItem("Выходной")
        swindow.comboBox_13.addItem("Выходной")
        swindow.comboBox_14.addItem("Выходной")
        swindow.comboBox_15.addItem("Выходной")
        swindow.comboBox_16.addItem("Выходной")
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
            swindow.comboBox_9.addItem(settings["RaspList"][item])
            swindow.comboBox_10.addItem(settings["RaspList"][item])
            swindow.comboBox_11.addItem(settings["RaspList"][item])
            swindow.comboBox_12.addItem(settings["RaspList"][item])
            swindow.comboBox_13.addItem(settings["RaspList"][item])
            swindow.comboBox_14.addItem(settings["RaspList"][item])
            swindow.comboBox_15.addItem(settings["RaspList"][item])
            swindow.comboBox_16.addItem(settings["RaspList"][item])
            swindow.listWidget.addItem(settings["RaspList"][item])
        swindow.spinBox.setValue(settings["RingDuration"])
        swindow.spinBox_2.setValue(settings["LightDelay"])
        swindow.autoOnNewDayCheckbox.setChecked(settings["AutoOnNewDay"])
        swindow.logCheckBox.setChecked(settings["EnableLog"])

        swindow.comboBox.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][0])])
        swindow.comboBox_2.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][1])])
        swindow.comboBox_3.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][2])])
        swindow.comboBox_4.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][3])])
        swindow.comboBox_5.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][4])])
        swindow.comboBox_6.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][5])])
        swindow.comboBox_8.setCurrentText(settings["RaspList"][str(settings["IndexesRasp"][6])])

        swindow.comboBox_10.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][0])])
        swindow.comboBox_14.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][1])])
        swindow.comboBox_11.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][2])])
        swindow.comboBox_9.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][3])])
        swindow.comboBox_12.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][4])])
        swindow.comboBox_15.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][5])])
        swindow.comboBox_13.setCurrentText(settings["RaspList"][str(settings["IndexesRaspN"][6])])

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
        for item in settings["SpecDays"]:
            ids = settings["SpecDays"][item].split(":")
            tdate = item.split("/")
            s = str(tdate[0]) + "/"
            if int(tdate[1]) < 10:
                s = s + "0"
            s = s + tdate[1] + "/" + tdate[2] + " - " + settings["RaspList"][ids[0]] + " / "
            s = s + settings["RaspList"][ids[1]]
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

        swindow.portComboBox.setCurrentText(settings["Port"]["Win"])
        swindow.portLineEdit.setText(settings["Port"]["Linux"])
        swindow.portSpeed.setCurrentText(str(settings["Port"]["Speed"]))

        blockChange = False

        try:
            del(swindow.CurrentIds)
        except:
            pass
        try:
            del(swindow.currentSpecialDay)
        except:
            pass
        try:
            del(swindow.currentSpecialRing)
        except:
            pass

        #Костыль для копирования параметров.
        swindow.sett = json.loads(json.dumps(settings))

        swindow.exec_() #exec_ делает форму модальной


    def autoModeButtonClick(self):
        logger("Автоматический режим включён.")
        self.manualModeButton.setChecked(False)
        self.autoModeButton.setChecked(True)
        self.amModeButton.setChecked(False)
        if settings["Mode"] != 0:
            settings["Mode"] = 0
            self.manualLightButton.setEnabled(False)
            self.manualLightButton_2.setEnabled(False)
            saveSettings()


    def manualModeButtonClick(self):
        logger("Ручной режим включён.")
        self.manualModeButton.setChecked(True)
        self.autoModeButton.setChecked(False)
        self.amModeButton.setChecked(False)
        if settings["Mode"] != 1:
            settings["Mode"] = 1
            self.manualLightOn[0] = self.needLight[0]
            self.manualLightOn[1] = self.needLight[1]
            self.manualLightButton.setEnabled(True)
            self.manualLightButton_2.setEnabled(True)
            saveSettings()


    def amModeButtonClick(self):
        logger("Полуавтоматический режим включён.")
        self.manualModeButton.setChecked(False)
        self.autoModeButton.setChecked(False)
        self.amModeButton.setChecked(True)
        if settings["Mode"] != 2:
            settings["Mode"] = 2
            self.manualLightOn[0] = self.needLight[0]
            self.manualLightOn[1] = self.needLight[1]
            self.manualLightButton.setEnabled(True)
            self.manualLightButton_2.setEnabled(True)
            saveSettings()


    def manualRingPress(self):
        logger("Ручное нажатие кнопки звонка.")
        self.startRing(0, 0)


    def manualRingRelease(self):
        logger("Кнопка отпущена.")
        self.stopRing(0)

    def manualRingNPress(self):
        logger("Ручное нажатие кнопки звонка в началке.")
        self.startRing(0, 1)


    def manualRingNRelease(self):
        logger("Кнопка отпущена.")
        self.stopRing(1)


    def manualLightClick(self):
        self.manualLightOn[0] = not self.manualLightOn[0]
        if self.manualLightOn[0]:
            logger("Ручное включение освещения в основной школе.")
        else:
            logger("Ручное выключение освещения в основной школе.")
        self.UpdateStatus()

    def manualLightNClick(self):
        self.manualLightOn[1] = not self.manualLightOn[1]
        if self.manualLightOn[1]:
            logger("Ручное включение освещения в начальной школе.")
        else:
            logger("Ручное выключение освещения в начальной школе.")
        self.UpdateStatus()

    def aboutButtonClick(self):
        aboutwindow.exec_()



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
        self.comboBox_9.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_10.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_11.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_12.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_13.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_14.currentTextChanged.connect(self.raspDayChanged)
        self.comboBox_15.currentTextChanged.connect(self.raspDayChanged)
        self.addSpecialDayButton.clicked.connect(self.addSpecialDayButtonClick)
        self.deleteSpecialDayButton.clicked.connect(self.deleteSpecialDayButtonClick)
        self.addSpecialRingButton.clicked.connect(self.addSpecialRingButtonClick)
        self.deleteSpecialRingButton.clicked.connect(self.deleteSpecialRingButtonClick)

        self.portComboBox.clear()
        for i in range(1, 31):
            self.portComboBox.addItem("COM" + str(i))

        self.autoStartCheckbox.setVisible(False)
        self.groupBox_2.setVisible(False)


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
        self.comboBox_9.clear()
        self.comboBox_10.clear()
        self.comboBox_11.clear()
        self.comboBox_12.clear()
        self.comboBox_13.clear()
        self.comboBox_14.clear()
        self.comboBox_15.clear()
        self.comboBox_16.clear()
        self.listWidget.clear()
        self.comboBox.addItem("Выходной")
        self.comboBox_2.addItem("Выходной")
        self.comboBox_3.addItem("Выходной")
        self.comboBox_4.addItem("Выходной")
        self.comboBox_5.addItem("Выходной")
        self.comboBox_6.addItem("Выходной")
        self.comboBox_7.addItem("Выходной")
        self.comboBox_8.addItem("Выходной")
        self.comboBox_9.addItem("Выходной")
        self.comboBox_10.addItem("Выходной")
        self.comboBox_11.addItem("Выходной")
        self.comboBox_12.addItem("Выходной")
        self.comboBox_13.addItem("Выходной")
        self.comboBox_14.addItem("Выходной")
        self.comboBox_15.addItem("Выходной")
        self.comboBox_16.addItem("Выходной")
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
            self.comboBox_9.addItem(self.sett["RaspList"][item])
            self.comboBox_10.addItem(self.sett["RaspList"][item])
            self.comboBox_11.addItem(self.sett["RaspList"][item])
            self.comboBox_12.addItem(self.sett["RaspList"][item])
            self.comboBox_13.addItem(self.sett["RaspList"][item])
            self.comboBox_14.addItem(self.sett["RaspList"][item])
            self.comboBox_15.addItem(self.sett["RaspList"][item])
            self.comboBox_16.addItem(self.sett["RaspList"][item])
            self.listWidget.addItem(self.sett["RaspList"][item])

        self.comboBox.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][0])])
        self.comboBox_2.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][1])])
        self.comboBox_3.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][2])])
        self.comboBox_4.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][3])])
        self.comboBox_5.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][4])])
        self.comboBox_6.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][5])])
        self.comboBox_8.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRasp"][6])])

        self.comboBox_10.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][0])])
        self.comboBox_14.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][1])])
        self.comboBox_11.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][2])])
        self.comboBox_9.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][3])])
        self.comboBox_12.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][4])])
        self.comboBox_15.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][5])])
        self.comboBox_13.setCurrentText(self.sett["RaspList"][str(self.sett["IndexesRaspN"][6])])

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
        for item in self.sett["SpecDays"]:
            ids = self.sett["SpecDays"][item].split(":")
            tdate = item.split("/")
            s = str(tdate[0]) + "/"
            if int(tdate[1]) < 10:
                s = s + "0"
            s = s + tdate[1] + "/" + tdate[2] + " - " + self.sett["RaspList"][ids[0]] + " / "
            s = s + self.sett["RaspList"][ids[1]]
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

        if d < 7:
            self.sett["IndexesRasp"][d] = ids
        else:
            d -= 7
            self.sett["IndexesRaspN"][d] = ids


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
                    messageBox("Ошибка", "Расписание с таким именем уже существует")
            else:
                break


    #Кнопка удаления расписания
    def deleteRaspButtonClick(self):
        try:
            ids = self.CurrentIds
        except AttributeError:
            return

        if (int(ids) in self.sett["IndexesRasp"]) or (int(ids) in self.sett["IndexesRaspN"]):
            messageBox("Ошибка", "Нельзя удалить расписание, так как оно назначено на один из дней недели.")
            return

        for item in self.sett["SpecDays"]:
            k = self.sett["SpecDays"][item].split(":")
            if (k[0] == ids) or (k[1] == ids):
                messageBox("Ошибка", "Нельзя удалить расписание, так как оно назначено на один из дней календаря.")
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
                    messageBox("Ошибка", "Расписание с таким именем уже существует")
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
            if self.sett["RaspList"][item] == self.comboBox_16.currentText():
                ids2 = int(item)

        s = str(day) + "/" + str(month) + "/" + str(year)
        self.sett["SpecDays"][s] = str(ids) + ":" + str(ids2)

        self.updateLists()


    #Кнопка удаления особенного дня
    def deleteSpecialDayButtonClick(self):
        try:
            csd = self.currentSpecialDay
        except AttributeError:
            return

        self.sett["SpecDays"].pop(csd)
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
        logger("Настройки закрыты. Отмена.")
        self.close()


    #Нажатие кнопки "OK"
    def buttonOKClick(self):
        global settings
        logger("Настройки закрыты. Применение.")

        self.sett["Port"]["Win"] = self.portComboBox.currentText()
        self.sett["Port"]["Linux"] = self.portLineEdit.text()
        self.sett["Port"]["Speed"] = int(self.portSpeed.currentText())

        self.sett["RingDuration"] = self.spinBox.value()
        self.sett["LightDelay"] = self.spinBox_2.value()
        if self.autoOnNewDayCheckbox.checkState():
            self.sett["AutoOnNewDay"] = True
        else:
            self.sett["AutoOnNewDay"] = False

        if self.logCheckBox.checkState():
            self.sett["EnableLog"] = True
        else:
            self.sett["EnableLog"] = False

        settings = json.loads(json.dumps(self.sett))
        saveSettings()
        window.idr = [-1, -1]
        self.close()



class AboutApp(QtWidgets.QDialog, aboutform.Ui_AboutDialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainform.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.versionLabel.setText("Версия " + VER)
        
        
def main():
    global swindow
    global window
    global aboutwindow

    try:
        if not os.path.exists("log"):
            os.mkdir("log")
    except:
        pass

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SchoolRingerApp()  # Создаём объект класса SchoolRingerApp
    window.show()  # Показываем окно
    swindow = SettingsApp()
    aboutwindow = AboutApp()
    
    app.exec_()  # и запускаем приложение
    logger("********** Завершение приложения **********")


if __name__ == '__main__':
    main()
