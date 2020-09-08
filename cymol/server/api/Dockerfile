FROM pypy:3

WORKDIR /var/www/api

ADD requirements.txt .

RUN pip install --upgrade pip; \
    pip install -r requirements.txt;

COPY . /var/www/api/