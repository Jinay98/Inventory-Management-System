FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app

CMD python3 manage.py runserver 0.0.0.0:8000