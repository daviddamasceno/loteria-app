FROM python:3.12-slim
WORKDIR /code
# Atualiza os pacotes do SO para corrigir vulnerabilidades de segurança (Debian)
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
