FROM python:3.9-slim
COPY requirements.txt /
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["gunicorn", "--workers=2", "--threads=2", "-b 0.0.0.0:80", "app:server"]