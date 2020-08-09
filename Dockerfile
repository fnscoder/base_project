FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --dev
COPY . /code/
EXPOSE 8000
CMD ["gunicorn", \
     "--workers=2",\
     "--worker-class=gthread",  \
     "--worker-tmp-dir=/dev/shm",\
     "--threads=4", \
     "--log-file=-", \
     "--bind=0.0.0.0:8000",\
     "base_project.wsgi"]
