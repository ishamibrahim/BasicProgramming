
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



###########################################
print("\n\n\n\n\n ******************************************************************** ")


class PrimeFinderAbstract(object):
    def __init__(self):
        self._prime_list = []

    def calculate(self, limit):
        """
            Calculates all prime numbers under the limit
        :param limit:
        :return:
        """

    def list_them(self):
        print(self._prime_list)

class QuickPrimeFinder(PrimeFinderAbstract):
    def __init__(self):
        self.ready_list = [2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        super(QuickPrimeFinder, self).__init__()

    def calculate(self, limit):
        print("QuickPrimeFinder calculate called")
        for prime in self.ready_list:
            if prime < limit:
                self._prime_list.append(prime)



class OriginalPrimeFinder(PrimeFinderAbstract):
    def calculate(self, limit):
        print("OriginalPrimeFinder calculate called")
        self._prime_list = [2]
        for new_num in range(3, limit, 2):
            prime_found = True
            for existing in self._prime_list:
                if new_num % existing == 0:
                    prime_found = False

            if prime_found:
                self._prime_list.append(new_num)



class PrimeClient():
    def __init__(self):
        self.prime_finder = None

    def list_primes(self, limit):
        if limit < 50:
            self.prime_finder = QuickPrimeFinder()
        else:
            self.prime_finder = OriginalPrimeFinder()
        print(self.prime_finder.__class__)
        self.prime_finder.calculate(limit)
        self.prime_finder.list_them()


myclient = PrimeClient()
myclient.list_primes(80)


