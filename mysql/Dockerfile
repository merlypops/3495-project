FROM mysql:5.7
ENV MYSQL_USER docker
ENV MYSQL_PASSWORD docker
ENV MYSQL_DB docker

WORKDIR /app

COPY create-table.py ./

CMD [ "python", "create-table.py"  ]


