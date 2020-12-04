FROM python:3.6

LABEL maintainer="arthur.sl.lin@modovision.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8081

ENTRYPOINT ["python"]

CMD ["server.py"]
