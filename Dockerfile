FROM python:3

RUN pip install --upgrade pip
RUN pip install pandas
RUN pip --default-timeout=1000 install pysus
RUN pip install sqlalchemy
RUN pip install psycopg2

WORKDIR /sih
COPY . .

CMD ["python", "sih/main.py"]