FROM python:latest

EXPOSE 5000

COPY ./requirements.txt ./app.py .
RUN pip install -r requirements.txt
CMD python app.py
