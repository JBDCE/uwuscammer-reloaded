FROM python:3.14-slim

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .
COPY uwu_scammer_reloaded_fastapi/model ./model
COPY uwu_scammer_reloaded_fastapi/static ./static
COPY uwu_scammer_reloaded_fastapi/templates ./templates
COPY uwu_scammer_reloaded_fastapi/main.py .

RUN pip install pipenv
RUN pipenv install --deploy --system

EXPOSE 8000
CMD ["fastapi", "run", "main.py"]
