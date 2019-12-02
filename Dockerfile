FROM python:3.7

ENV DASH_DEBUG_MODE True

EXPOSE 8050

COPY ./src /src

WORKDIR /src

RUN set -ex && \
    pip install -r requirements.txt

CMD ["python", "index.py"]