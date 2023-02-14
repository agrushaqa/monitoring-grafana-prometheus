# Телеграм-бот.
система мониторинга ПК в корпоративной сети

Цель:

    закрепить знания и навыки, полученные в течение курса;
    реализовать собственный проект;
    пополнить своё портфолио качественным проектом.

Критерии:
    структура (примеры можно нагуглить, посмотреть ссылку в 1 ДЗ или посмотреть на крупные проекты а-ля fastapi, aiohttp и т.п.)
    тесты
    CI с запуском тестов, black, isort, mypy, flake8 и прочего
    управление зависимостей через poetry
    Dockerfile/docker-compose
    Краткое описание в README.md
    если там ООП, то есть попытка соблюдать SOLID

Ссылки:

    https://www.marwandebbiche.com/posts/python-package-tooling/
    https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/

# requirements.txt
## create
pip freeze > requirements.txt
## use
pip install -r requirements.txt

# code style
## isort
python -m pip install isort
### run 
isort .
## mypy
python -m pip install mypy
### run 
mypy .
## flake8
python -m pip install flake8
### run
flake8 --exclude venv,docs --ignore=F401
## code coverage
pip install coverage
### run
coverage run C:\Users\agrusha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\behave\__main__.py
в файле .coveragerc нужно указать исходники

# Pytest - Run Tests in Parallel
## install
```pip install pytest-xdist```

also:
https://pypi.org/project/pytest-parallel/
## run
```pytest -n 2 test_common.py```


# Замечания
при асинхронной загрузке я получаю ошибку
 Sorry, we're not able to serve your requests this quickly. 

## Cкачивание страницы curl
curl.exe --insecure https://news.ycombinator.com/item?id=34722118