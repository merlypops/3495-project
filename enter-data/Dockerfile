from python:latest

WORKDIR /app

COPY enter-data.py ./

RUN apt-get update
RUN apt install pip
RUN pip install sqlite3
RUN pip install mysql.connector
RUN pip install pyodbc
RUN pip install pandas

CMD [ "python", "enter-data.py"  ]

