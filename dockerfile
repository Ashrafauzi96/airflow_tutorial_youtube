FROM apache/airflow:2.10.1

# Compulsory to switch parameter
ENV PIP_USER=false

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ENV PIP_USER=true