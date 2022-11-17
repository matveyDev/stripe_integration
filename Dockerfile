FROM python:3.9

WORKDIR /backend

COPY req.txt ./

RUN pip install -r req.txt

COPY ./ ./

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
