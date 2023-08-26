FROM python:3.10.11

WORKDIR /RapidFort

COPY . /RapidFort


RUN pip install -r requirements.txt

EXPOSE 80

ENV Name World

CMD ["python", "fileupload.py"]

