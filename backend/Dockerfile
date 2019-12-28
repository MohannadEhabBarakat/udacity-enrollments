FROM python:3.5.2

LABEL Author="Mohannad Barakat"
LABEL E-mail="M.Barakat@nu.edu.eg"
LABEL version="0.0.5"

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./ 
COPY .env ./ 
COPY .flaskenv ./ 

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0


