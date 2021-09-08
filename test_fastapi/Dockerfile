FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app
COPY Pipfile Pipfile.lock ./

RUN apt-get update \
 && apt-get install -y -qq gnupg wget \
 && wget -O - http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add - \
 && echo "deb http://packages.couchbase.com/ubuntu buster buster/main" | tee /etc/apt/sources.list.d/couchbase.list \
 && apt-get update \
 && apt-get install -y -qq libcouchbase-dev libcouchbase2-bin gcc\
 && apt-get clean

run python -m pip install pipenv httpx
RUN pipenv install --deploy
ENV PYTHONPATH ${WORKDIR_PATH}

CMD "uvicorn", "runserver:app", "--host", "0.0.0.0", "--port", "9418"
