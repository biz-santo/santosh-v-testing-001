FROM python:3.8
RUN pip install -U pip

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 9000
CMD ["python", "/app/main.py"]
