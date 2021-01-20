FROM python:latest

EXPOSE 5000

COPY ./requirements.txt ./
ADD app ./app
RUN pip install -r requirements.txt
CMD python app/app.py
