FROM mysql:5.7
ENV MYSQL_USER docker
ENV MYSQL_PASSWORD docker
ENV MYSQL_DB docker

WORKDIR /app

COPY create-table.py ./

RUN apt-get update
RUN apt install pip
RUN pip install sqlite3
RUN pip install mysql.connector
RUN pip install pyodbc

CMD [ "python", "create-table.py"  ]


