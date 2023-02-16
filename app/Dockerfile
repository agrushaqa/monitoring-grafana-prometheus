FROM alpine:3.17

WORKDIR /usr/src/

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONPATH=/usr/src/

RUN apk update && apk add libffi-dev python3-dev gcc libc-dev
RUN apk add py3-pip py3-psycopg2 uwsgi uwsgi-python3 uwsgi-http postgresql-client

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", ".app/api.py" ]