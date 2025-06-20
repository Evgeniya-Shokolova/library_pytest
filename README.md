![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## Инструкция по созданию и запуску автоматизированных тестов для текстовой библиотеки на Python


Убедитесь, что у вас установлен Python
Клонируйте репозиторий
```bash
git clone git@github.com:Evgeniya-Shokolova/library_pytest.git
```
Перейти в папку с проектом
```bash
cd library_pytest
```
Создать виртуальное окружение:
   Команда для Windows: -
```bash
python -m venv venv
```
Команда для Linux и macOS: - 
```bash
python3 -m venv venv
```
Активировать виртуальное окружение:
   Команда для Windows: -
```bash
source venv/Scripts/activate
```
Для Linux и macOS: -
```bash
source venv/bin/activate
```
Установить PyTest:
```bash
pip install pytest
```
Обновить пакетный менеджер:
   Для Windows: -
```bash
python -m pip install --upgrade pip
```
Для Linux и macOS: -
```bash
python3 -m pip install --upgrade pip
```


### Запуск тестов

Чтобы запустить написанные тесты, выполните следующую команду в терминале:
```bash
pytest --tb=short test_functions.py
```

### Отчет о тестировании

Установить плагин pytest-html, который необходим для генерации HTML отчетов:
```bash
pip install pytest-html
```
Для генерации отчета в HTML формате:
```bash
pytest --tb=short --html=report.html --self-contained-html test_text_functions.py
```
Это создаст файл report.html, который можно открыть в браузере для ознакомления с результатами тестов.

Комментарии к коду

- Каждый тест имеет строки с проверками assert, которые сопоставляют ожидаемые выходные данные с фактическими.
- Тесты структурированы так, что легко добавлять новые случаи, какими бы сложными они ни были.

