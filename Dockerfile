FROM python:3.5-alpine
MAINTAINER Francisco Vaquero <francisco@opi.la>

ENV DJANGO_HOME=Django

RUN pip install virtualenv
RUN mkdir Django
COPY .  Django/
RUN pip install -r $DJANGO_HOME/Formularios/requirements.txt

EXPOSE 8000
CMD ["python", "Django/Formularios/manage.py", "runserver", "0.0.0.0:8000"]