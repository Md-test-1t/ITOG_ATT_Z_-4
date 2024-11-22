FROM python:3.10

WORKDIR /app

COPY data.csv .
COPY app.py .

RUN pip install pandas

CMD ["python", "app.py"]