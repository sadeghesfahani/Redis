import redis

re = redis.Redis()
pubsub = re.pubsub()
#
# re.publish("something", "hi")
# re.publish("something", "hi")

for i in range(10):
    re.publish("channel_name", i)
