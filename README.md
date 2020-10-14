![Python v3](https://img.shields.io/badge/Python-v3-blue)

# BellManager
Программа для управления звонками и освещением в школе    
Текущая версия: **v2.0.1**    
Подробности о проекте: [https://19dx.ru/2020/10/light-and-bell-school-controller/](https://19dx.ru/2020/10/light-and-bell-school-controller/)

## Аппаратное обеспечение
Управляющий контроллер: Arduino UNO / Arduino Mega    
Контроллеры освещения: К2010 или аналогичные (используется шина управления 4-20 мА)

## Схема управляющего контроллера
![Схема управляющего контроллера](https://19dx.ru/wp-content/uploads/2020/10/BellManager.png)

## Протокол обмена данными
Приложение отправляет на контроллер следующие текстовые команды:    
| Символ или их комбинация | Значение |
|:------------------------:|----------|
| **Y--$K** | Инициализация контроллера. Команда посылается при установке связи с контроллером. До её получения все остальные команды игнорируются. |
| **Q** | Включение звонка в основной школе |
| **q** | Выключение звонка в основной школе |
| **W** | Включение звонка в начальной школе |
| **w** | Выключение звонка в начальной школе |
| **E** | Включение освещения в основной школе |
| **e** | Выключение освещения в основной школе |
| **R** | Включение освещения в начальной школе |
| **r** | Выключение освещения в начальной школе |

Команды для звонка передаются непосредственно в моменты его включения/выключения. Команды на освещение передаются каждую секунду. При отсутствии команд в течении 5 секунд - контроллер считает, что связь потеряна и выключает всё.

## TODO
[Список TODO](https://github.com/student-proger/BellManager/labels/todo)