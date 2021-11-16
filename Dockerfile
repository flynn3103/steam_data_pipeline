FROM puckel/docker-airflow:1.10.4
COPY dags /usr/local/airflow/dags

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/
