FROM python:3.10
LABEL authors="tlsabara"
LABEL project="fake_gaspar"

ENV ROOT_DIR=/code

WORKDIR $ROOT_DIR

COPY ./ $ROOT_DIR

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python ./fake_phamtom/endpointlocal.py
