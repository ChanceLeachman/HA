FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "-u", "lirc_watcher.py"]
