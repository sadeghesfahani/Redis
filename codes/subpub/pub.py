import redis

re = redis.Redis()
pubsub = re.pubsub()


for i in range(10):
    re.publish("channel_name", i)
