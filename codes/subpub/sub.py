import redis

re = redis.Redis()

def get_data():
    pubsub = re.pubsub()
    pubsub.subscribe("channel_name")
    for message in pubsub.listen():
        print(message)


while True:
    get_data()

