# Start
This project is simple SmartHome app.

# File description
Combination framework Dash and Flask.
Admin Flask.
View Dash.
Database MongoDB.
OS Linux server Debian how Broker(MQTT).
MQTT.
SMTP for feedback.
Photo description all comuniocation in project.....
# End
In the future, new features will be added to the project.![Документ2](https://user-images.githubusercontent.com/74335902/128578283-29512dad-2199-4cc2-aaf1-cedf8bea133a.jpg)
![diagram](https://user-images.githubusercontent.com/74335902/128578314-bb94be83-04a6-45f5-a09a-fd38f6c72ede.jpg)
Опис схеми:
1)Користувач змінює параметри в додатку. Додаток надає брокеру параметри.
2)Сервер NodeMCU отримує сигнал що потрібно змінити температуру.
3)Статус датчиків та параметри сервера відправляються на брокер.
4)Брокер відає повідомлення на веб-сервер.
5)Веб-сервер записує дані в базу даних.
6)Дані з бази даних виводяться на dashboard.
Дані передаютсья в JSON-форматі.

![Діаграма послідовностей](https://user-images.githubusercontent.com/74335902/128578477-e3f0580f-6707-404c-b3d3-55586604f236.jpg)
