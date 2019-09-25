
"""
    Used to dynamically change the class method behavior
"""

import types


class Strategy(object):
    def __init__(self, function =None):
        self.name = "AbstractStrategy"

        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("Abstract strategy called to implement default strategy")


def divide_and_conquer(cls):
    print("{} called for divide and conquer".format(cls.name))


def brute_force(cls):
    print("{} called for brute force".format(cls.name))


s1 = Strategy()
s1.execute()

s2 = Strategy(divide_and_conquer)
s2.name = "Strategy Two"
s2.execute()

s3 = Strategy(brute_force)
s3.name = "Srtategy Three"
s3.execute()
