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
## docker
docker-compose up -d
## CLI
cd app
python collect_info.py
## api
cd app
python api.py
В этом случае инфомация будет выводится по адресам
- http://localhost:5000/cpu
- http://localhost:5000/ram
- http://localhost:5000/computer_name
- http://localhost:5000/app_on_net

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

# Запуск тестов
python -m pytest --rootdir=. tests --alluredir=report/

# пересобрать образ
docker-compose build

# Удалить старые не используемые образы
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
dangling=true - фильтрует не используемые образы

# Замечания
в docker кладу всё папку, а не только 
context: ./app
для того, чтобы import работали и напрямую и из docker

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


# Pytest - Run Tests in Parallel
## install
```pip install pytest-xdist```

also:
https://pypi.org/project/pytest-parallel/
## run
```pytest -n 2 test_common.py```


