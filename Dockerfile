FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install --no-cache-dir numpy
WORKDIR /app
ENV FLASK_APP app.py
RUN ls -al /app

CMD [ "python3", "-u", "-m" , "flask", "run", "--host=0.0.0.0"]
