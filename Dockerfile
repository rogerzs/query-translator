FROM python:3.10.6

WORKDIR /query-translator

EXPOSE 8085

COPY requirements.txt requirements.txt


RUN pip install -U pip

RUN pip install -r requirements.txt

COPY Home.py Home.py

COPY pages pages

WORKDIR .

CMD streamlit run Home.py