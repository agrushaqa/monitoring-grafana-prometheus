# Система мониторинга
система мониторинга ПК в корпоративной сети

# Цель:

    закрепить знания и навыки, полученные в течение курса;
    реализовать собственный проект;
    пополнить своё портфолио качественным проектом.

# Критерии:
    структура (примеры можно нагуглить, посмотреть ссылку в 1 ДЗ или посмотреть на крупные проекты а-ля fastapi, aiohttp и т.п.)
    тесты
    CI с запуском тестов, black, isort, mypy, flake8 и прочего
    управление зависимостей через poetry
    Dockerfile/docker-compose
    Краткое описание в README.md
    если там ООП, то есть попытка соблюдать SOLID

# Ссылки:

    https://www.marwandebbiche.com/posts/python-package-tooling/
    https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/

# Описание:
Цель этого приложения - исследование способов мониторинга приложения
на примере таких характеристик как
- скорость сети
- приложения использующие сеть
- потребляемая память
- свободное место на диске

в рамках этой задачи я исследовал
- grafana
- prometheus
- flask
- zabbix

я планировал добавить телеграмм бот для оповещений, но как оказалось
grafana уже позволяет отправлять оповещения в telegram

# Запуск:
docker-compose up -d

grafana:
http://localhost:3000
- креды admin\grushagraphana (пароль можно изменить в docker-compose.yml)
prometheus:
http://localhost:9090
http://127.0.0.1:5000/metrics
flask
- http://localhost:5000/cpu
- http://localhost:5000/ram
- http://localhost:5000/computer_name
- http://localhost:5000/app_on_net
  (в prometheus http://127.0.0.1:5000/metrics пока попадает только ram)

# Настройка

если в virtualbox то рекомендуется скопировать исходники в обычную папку
cp -r copy_telegram_bot /home/artem/2023
и дать ей права для запуска prometheus
chgrp -R nogroup ./prometheus
chmod 777 -R prometheus


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