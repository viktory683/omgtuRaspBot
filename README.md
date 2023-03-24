# omgtuRaspBot

Бот расписания Омского политеха (ОмГТУ)

Перед запуском необходимо установить нужные зависимости из [файла](requirements.txt)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Для запуска достаточно передать исполняемому `python` файлу в виртуальном окружении главный [main.py](main.py) файл

```bash
.venv/bin/python main.py
```

Переменные, которые должны быть секретными (токен бота например), задавать через переменные окружения при запуске, либо
в файле `.env`

```bash
BOT_TOKEN=000000000:00000000000000000000000000000000000 .venv/bin/python main.py
```

Пример файла `.env`

```bash
BOT_TOKEN=000000000:00000000000000000000000000000000000
VAR1=1
...
```

### TODO

- [x] Выбор группы
- [ ] Выбор подгруппы
- [x] Пары сегодня
- [x] Пары завтра
- [x] Пары на неделе
- [ ] Получение пар по заданному расписанию
- [ ] Получение пар выбранного дня/недели
- [ ] Получение пар выбранного дня/недели с инлайн-кнопочным календарем
- [x] Пара сейчас/следующая
- [x] Формат сообщения при отсутствии того или иного поля
- [ ] Миграция с json "базы данных" на sqlite

[Телега жалоб и предложений](https://t.me/bzglve "@bzglve")
