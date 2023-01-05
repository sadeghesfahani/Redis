import redis

r = redis.Redis()

r.set("key", "value")

value_of_key = r.get("key")
print(value_of_key)  # note that it is not a python string to use

pythonic_string_value_of_key = value_of_key.decode("utf-8")  # by decode binary string will be converted to real string
print(pythonic_string_value_of_key)
