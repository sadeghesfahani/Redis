import redis

r = redis.Redis(db=1)

# inserting with hset
r.hset("newHashTable", "key1", "value1")
r.hset("newHashTable", "key2", "value2")

print(r.hget("newHashTable", "key1"))
print(r.hgetall("newHashTable"))

# inserting with hmset
r.hmset("anotherHashTable", {"key-1": "value-1", "key-2": "value-2"}) # note that this function is deprecated
print(r.hgetall("anotherHashTable"))
