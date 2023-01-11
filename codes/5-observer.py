class Observer:

    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(self.name, " ", message)


class SomethingLikeRedis:
    observers = []

    @staticmethod
    def subscribe(observer):
        SomethingLikeRedis.observers.append(observer)

    @staticmethod
    def publish(message):
        for observer in SomethingLikeRedis.observers:
            observer.notify(message)


publisher = SomethingLikeRedis()
subscriber1 = Observer("sub1")
subscriber2 = Observer("sub2")

publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

publisher.publish("here we are")
