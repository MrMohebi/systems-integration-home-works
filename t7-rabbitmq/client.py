import pika, sys, os, threading
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode('ascii')}")


def main():
    credentials = pika.PlainCredentials('root', '123654789')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672,credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='user1')
    channel.queue_declare(queue='user2')

    channel.basic_consume(queue='user2', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    def xx(channel):
        channel.start_consuming()

    t1 = threading.Thread(target=xx, args=(channel,))
    t1.start()

    inp = ""

    while inp != "exit":
        inp = input("enter message: ")

        channel.basic_publish(exchange='', routing_key='user1', body=inp)

        print(" [x] Sent '{}'".format(inp))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
