FROM python:3.8-alpine
LABEL maintainer="Galen Guyer <galen@galenguyer.com>"

RUN apk add tzdata gcc musl-dev python3-dev libffi-dev openssl-dev cargo rust && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone && \
    apk del tzdata

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
RUN apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo rust
ADD . /app

ENTRYPOINT ["gunicorn", "api:APP"]
CMD ["--bind=0.0.0.0:5000"]
