FROM python:3.10

EXPOSE 4534

RUN mkdir -p /opt/services/my_tg_bot
WORKDIR /opt/services/my_tg_bot

COPY . /opt/services/my_tg_bot

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/my_tg_bot/main.py"]