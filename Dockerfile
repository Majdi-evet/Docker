#Download base image Python 3.6
FROM python:3.6
# COPY . .
add . ./
RUN apt-get update
RUN pip install -r ./requirement.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]