FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./app ./app

RUN pip install -r ./app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]