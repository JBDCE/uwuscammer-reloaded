FROM python:3.14-slim

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .
COPY model ./model
COPY static ./static
COPY templates ./templates
COPY main.py .

RUN pip install pipenv
RUN pipenv install --deploy --system

EXPOSE 8000
CMD ["fastapi", "run", "main.py"]
