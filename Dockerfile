FROM python:latest

WORKDIR /app

COPY requirements.txt ./

ENV VIRTUAL_ENV=/venv

RUN python -m venv venv

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app/index_cards

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]