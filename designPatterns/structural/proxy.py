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
    def __init__(self, producer):
        self.occupied = False
        self.producer = producer

    def produce(self):
        print("Actor checks if producer is available")
        if not self.occupied:
            self.producer.available()
            time.sleep(1)

            self.producer.produce()
        else:
            time.sleep(1)
            print("Producer is busy and cant take your call")
# prod = Producer()
# p = Proxy(prod)
# p.produce()
#
# p.occupied = True
# p.produce()

# ####################### Another way of implementing proxy #########################


class Blog:
    def write(self):
        print("Writing the blog")

    def read(self):
        print("Reading the blog")


class UserProxy:
    def __init__(self, blog):
        self.blog=blog

    def __getattr__(self, item):
        return getattr(self.blog, item)


class AnonymousUser(UserProxy):

    def __init__(self, blog):
        UserProxy.__init__(self, blog)

    def write(self):
        print("Writing not allowed for anonymous user")


b = Blog()
legit_user = UserProxy(b)
legit_user.read()
legit_user.write()

anonymous = AnonymousUser(b)
anonymous.read()
anonymous.write()
