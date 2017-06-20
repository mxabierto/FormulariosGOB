FROM python:2.7
MAINTAINER Francisco Vaquero <francisco@opi.la>

ENV DJANGO_HOME=Django

RUN pip install virtualenv && mkdir Django
RUN git clone https://github.com/vaquer/FormulariosGOB.git /Django && \
    pip install -r $DJANGO_HOME/Formularios/requirements.txt

EXPOSE 8000
CMD ["python", "Django/Formularios/manage.py", "runserver", "0.0.0.0:8000"]
