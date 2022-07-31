pyinstaller --icon=mainicon.ico --noconsole main.py
md dist\main\images
md dist\main\ArduinoFW\BellManagerController
md dist\main\ArduinoFW\BellManagerController_hwv2
md dist\main\sounds
copy ArduinoFW\BellManagerController\*.* dist\main\ArduinoFW\BellManagerController\
copy ArduinoFW\BellManagerController_hwv2\*.* dist\main\ArduinoFW\BellManagerController_hwv2\
copy images\*.* dist\main\images\
copy sounds\*.* dist\main\sounds\
copy license.txt dist\main\
copy changelog.txt dist\main\
rename dist\main\main.exe bellmanager.exe
rename dist\main\main.exe.manifest bellmanager.exe.manifest