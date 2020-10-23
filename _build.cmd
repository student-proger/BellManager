pyinstaller --icon=mainicon.ico --noconsole main.py
md dist\main\images
md dist\main\ArduinoFW\BellManagerController
copy ArduinoFW\BellManagerController\*.* dist\main\ArduinoFW\BellManagerController\
copy images\*.* dist\main\images\
copy license.txt dist\main\
rename dist\main\main.exe bellmanager.exe
rename dist\main\main.exe.manifest bellmanager.exe.manifest