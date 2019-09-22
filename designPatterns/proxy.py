import time
"""
 This type of design is used when producer object is very expensive. Proxy will handle instantiating producer object 
 creations looking at the available resources.
"""


class Producer:
    def produce(self):
        print("Producer started working")

    def available(self):
        print("Producer is available to take up now.")


class Proxy:
    def __init__(self):
        self.occupied = False
        self.producer = None

    def produce(self):
        print("Actor checks if producer is available")
        if not self.occupied:
            print("Producer is not busy")
            p = Producer()
            time.sleep(1)

            p.available()
        else:
            time.sleep(1)
            print("Producer is busy and cant take your call")

p = Proxy()
p.produce()

p.occupied = True
p.produce()