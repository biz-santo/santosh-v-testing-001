RUN python3 -m  venv ee-test-env
RUN source ee-test-env/bin/activate

FROM python:3.8
RUN pip install -U pip

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 9000
CMD ["python", "/app/main.py"]
