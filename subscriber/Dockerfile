FROM python:3.7-alpine
COPY subscriber.py subscriber.py
RUN pip install paho-mqtt redis
CMD ["python","subscriber.py"]