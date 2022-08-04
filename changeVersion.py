# Мне надоело постоянно менять номер версии в разных файлах, поэтому появился данный скрипт :)

import io

newver = input("Введите номер новой версии: ")

f = open("installer.iss", "rt")
buf = f.readlines()
f.close()
f = open("installer.iss", "wt")
for item in buf:
	if item.startswith("#define MyAppVersion "):
		print(item.strip(), "---> ", end="")
		item = "#define MyAppVersion \"" + newver + "\"\n"
		print(item)
	f.write(item)
f.close()

f = io.open("main.py", mode="rt", encoding="utf-8")
buf = f.readlines()
f.close()
f = io.open("main.py", mode="wt", encoding="utf-8")
for item in buf:
	if item.startswith("VER = "):
		print(item.strip(), "---> ", end="")
		item = "VER = \"" + newver + "\"\n"
		print(item)
	f.write(item)
f.close()

f = io.open("README.md", mode="rt", encoding="utf-8")
buf = f.readlines()
f.close()
f = io.open("README.md", mode="wt", encoding="utf-8")
for item in buf:
	if item.startswith("Текущая версия: "):
		print(item.strip(), "---> ", end="")
		item = "Текущая версия: **v" + newver + "**    \n"
		print(item)
	f.write(item)
f.close()
