FROM python:3.8-slim-buster
RUN pip install --no-cache-dir numpy
WORKDIR /app
ENV FLASK_RUN_FROM_CLI true
ENV FLASK_APP app.py
ENV FLASK_ENV=development
COPY php.ini /usr/local/etc/php/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN ls -al /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
