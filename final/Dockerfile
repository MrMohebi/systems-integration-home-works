FROM hub.hamdocker.ir/python:3.10-alpine AS builder
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 6060
CMD ["flask","-A", "api.py", "run", "-h", "0.0.0.0", "-p", "6060"]
