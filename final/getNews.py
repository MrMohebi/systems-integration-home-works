import json
import sys

import pika
import requests

BASE_API_URL = "http://127.0.0.1:6060"
RABBIT_URL = "127.0.0.1"

phone = sys.argv[1] if len(sys.argv) > 1 else exit(0)

res = requests.get(url=BASE_API_URL + "/user/topics", params={"phone": phone})

if res.status_code != 200:
    print("user not found!")
    exit(0)

topics = res.json()

if len(topics) < 1:
    print("user not found!")
    exit(0)

print(topics)


def callback(ch, method, properties, body):
    body = json.loads(body)
    print("----------- new message -----------")
    print("title => {}".format(body["title"]))
    print("topic => {}".format(body["topic"]))
    print("details => {}".format(body["text"]))
    print("sentAt => {}".format(body["createdAt"]))
    print("-----------------------------------")


credentials = pika.PlainCredentials('root', '123654789')
rabbit_connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBIT_URL, port=5672, credentials=credentials))
channel = rabbit_connection.channel()
channel.exchange_declare(exchange='news', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue


for topic in topics:
    channel.queue_bind(exchange='news', queue=queue_name, routing_key=topic)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    rabbit_connection.close()
