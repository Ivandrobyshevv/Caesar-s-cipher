### 14.04.2023

```Commit:55a7bd2```

- Добавлена функция **decryption_caesar()** и **test_decryption_caesar.py** к ней
    * test_decryption_caesar.py - Тесты

```Commit:03608f6```

- Добавлены тесты к функции **encryption_caesar()**
    * test_exceptions.py - Тесты к функции encryption_caesar

```Commit:745e843```

- Добавлены модули: **src/caesar.py,** **src/main.py.**
    * caesar.py - Логика шифрования
    * main.py - Точка входа

```Commit:1572ec1```

- Добавлены модули: **src/controller.py,**, **src/db.py,** **src/exceptions.py.**
    * controller.py - Взаимодействие с пользователем
    * db.py - Своеобразная база данных
    * exceptions.py - Обработка исключений

- Добавлены **test/test_exceptions.py**
    * test_check_language - Выбор языка
    * test_check_operation - Выбор операции (Зашифровать/Расшифровать)
    * test_check_shift_ru - Сдвиг для русского алфавита
    * test_check_shift_eng - Сдвиг для английского алфавита
    * test_check_text_ru / test_check_text_eng - Проверка входного текса к принадлежности выбранного алфавиту

```Commit: 697a0eb```

- Инициализация Git
