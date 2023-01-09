import redis
import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
        }

r = redis.Redis(db=1)  # we choose db = 1 to work on a separate database than 1-simple-test.py

# bad practice
[r.hmset(h_id, hat) for h_id, hat in hats.items()]


with r.pipeline() as pip:
    [pip.hmset(h_id, hat) for h_id, hat in hats.items()]  # note that hmset is deprecated
    pip.execute()

# above code is like below code in python
# data = {
#     "hat:random0": {
#         "color": "maroon",
#         "price": 59.99,
#         "style": "hipster",
#         "quantity": 500,
#         "npurchased": 0,
#     },
#     "hat:random1": {
#         "color": "maroon",
#         "price": 59.99,
#         "style": "hipster",
#         "quantity": 500,
#         "npurchased": 0,
#     },
#     "hat:random2": {
#         "color": "maroon",
#         "price": 59.99,
#         "style": "hipster",
#         "quantity": 500,
#         "npurchased": 0,
#     }
# }

# it will put save command into a queue if other commands
# has received by redis first. persist data in binary file
r.bgsave()

keys = r.keys()

for key in keys:  # Careful on a big DB. keys() is O(N). todo: set reference to linked lists here
    print(r.hgetall(key))
