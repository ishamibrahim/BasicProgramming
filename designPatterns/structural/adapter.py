
"""
USed when there is different signatues in similar classes. Adapter blends both signature based on the
object that's being called
"""

class Indian:
    def __init__(self):
        self.name = type(self).__name__


    def speak_indian(self):
        return "Namashkaar Dost"


class Arabian:
    def __init__(self):
        self.name = type(self).__name__

    def speak_arabic(self):
        return "Assalamu alaikum Habeebi"


class Adapter:
    def __init__(self, person, **adapted_method):
        self._person = person
        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        """Return rest of the items"""
        return getattr(self._person, item)


arabian = Arabian()
indian = Indian()

adapter_a = Adapter(arabian , speak=arabian.speak_arabic)
adapter_i = Adapter(indian, speak=indian.speak_indian)

objects = [adapter_a, adapter_i]
for obj in objects:
    print("An {} would say - {}".format(obj.name, obj.speak()))


##################################################################################

class AmericanSocket:
    def voltage(self):
        return 110

    def live(self):
        return 1

    def neutral(self):
        return -1

class EuropeanSocket:
    def voltage(self):
        return 240

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 1

class AmericanKettle:
    _power = None

    def __init__(self, power):
        self._power = power

    def boil(self):
        if self._power.voltage() > 110:
            print("Too much power. Kettle burst to flames")

        else:
            if self._power.live() and self._power.neutral() == -1:
                print("Coffee connects people")
            else:
                print("No power")


class Adapter:
    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        if self._socket.voltage() > 110:
            return 110
        else:
            return self._socket.power()

    def live(self):
        return self._socket.live()

    def neutral(self):
        return self._socket.neutral()




print(" Without using the adapter ")
# Cannot use the European socket for boiling in AmericanKettle
# Because the european socket has too much voltage
euro_socket = EuropeanSocket()
us_kettle = AmericanKettle(euro_socket)
us_kettle.boil()

# using an adapter solves it
print(" Using the adapter now")
adapter = Adapter(euro_socket)
us_kettle = AmericanKettle(adapter)
us_kettle.boil()
