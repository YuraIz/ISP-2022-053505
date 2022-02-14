FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir numpy

COPY . .

ENTRYPOINT [ "python", "./text_stat.py" ]