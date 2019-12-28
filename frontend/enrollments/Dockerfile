FROM node:latest

LABEL Auther="Mohannad Barakat"
LABEL Email="M.Barakat@nu.edu.eg"
# LABEL Email="M.Barakat@nu.edu.eg"

WORKDIR /app

COPY . /app

RUN npm install && \
    npm install -g @angular/cli

EXPOSE 4200


CMD ng serve --host 0.0.0.0