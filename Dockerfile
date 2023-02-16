FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt && pip install django-s3-collectstatic
CMD [ "python", "./catalog_api/manage.py", "runserver", "0.0.0.0:8000" ]
