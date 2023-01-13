FROM python:latest

EXPOSE 8000

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv venv

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/src/index_cards

CMD [ "python", "manage.py", "runserver"]