import datetime
import json
import math
import random

import redis


def generate_list(number_of_items):
    random.seed(number_of_items)
    list_of_numbers = [math.floor(random.getrandbits(32)) for x in range(number_of_items)]
    return list_of_numbers


def sort_list(list_of_values):
    new_list_of_values = sorted(list_of_values)
    return new_list_of_values


def find_leaner(value, list_of_values):
    for index, val in enumerate(list_of_values):
        if val == value:
            return "found"

    return "not found"


def find_binary(value, list_of_values):
    while len(list_of_values) > 1:
        value_of_the_half = list_of_values[len(list_of_values) // 2]
        # print(list_of_values)
        if value_of_the_half == value:
            return "found"
        elif value < value_of_the_half:
            list_of_values = list_of_values[:len(list_of_values) // 2]
        else:
            list_of_values = list_of_values[len(list_of_values) // 2:]

    if len(list_of_values) == 2:
        pass

    return "not found"


if __name__ == '__main__':
    redis_client = redis.Redis()
    redis_client.set("key", "value")
    print(redis_client.get("key"))
    if redis_client.get("sorted_list"):
        sorted_list = json.loads(redis_client.get("sorted_list").decode("utf-8"))
        what_to_find = int(redis_client.get("what_to_find").decode("utf-8"))
    else:
        list_of_values = generate_list(10000000)
        redis_client.set("list_of_values", json.dumps(list_of_values))
        what_to_find = list_of_values[40]
        redis_client.set("what_to_find", what_to_find)
        sorted_list = sort_list(list_of_values)
        redis_client.set("sorted_list", json.dumps(sorted_list))
    time0 = datetime.datetime.now()
    index_of_value = find_leaner(what_to_find, sorted_list)
    time1 = datetime.datetime.now()
    index_of_value = find_binary(what_to_find, sorted_list)
    time2 = datetime.datetime.now()

    print(time1 - time0, time2 - time1)


