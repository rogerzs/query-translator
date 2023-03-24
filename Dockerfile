FROM PYTHON 3.10.6

EXPOSE 8080

COPY requirements.txt requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY 🏠Home.py 🏠Home.py

COPY pages pages

WORKDIR .

RUN ENTRYPOINT["streamlit", "run", "🏠Home.py", "-server.port=8080", "-server.address=0.0.0.0"]
