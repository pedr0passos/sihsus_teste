FROM python:3

RUN pip install --upgrade pip 
COPY requirements.txt ./
RUN pip install --no-cache-dir --default-timeout=1000 -r ./requirements.txt

WORKDIR /sih
COPY . .

CMD ["python", "./teste.py"]