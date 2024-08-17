# syntax=docker/dockerfile:1

FROM python:3.10
EXPOSE 8000
WORKDIR /drf_project

COPY /drf_project/requirements.txt /drf_project
RUN pip install -r requirements.txt --no-cache-dir

COPY /drf_project /drf_project

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
