FROM python:3.7-alpine
ADD publisher.py publisher.py
RUN pip install flask flask_restful flask_cors paho-mqtt
CMD ["python","publisher.py"]