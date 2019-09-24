"""
Used when a change in the subject need to be notified to the observers.
Generally used when monitoring one system and a change would require many kinds of notifications to be sent

"""


class Subject(object):
    def __init__(self):
        self._observers = list()

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, modifier=None):
        for observer in self._observers:

            if modifier != observer:
                observer.update(self)

class PowerPlant(Subject):
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temp):
        self._temperature = temp
        self.notify()


class TempObserver:
    def update(self, subject):
        print("Temperature Viewer {} has reached the temperature {}".format(subject._name, subject.temperature))


c1 = PowerPlant("Chernobyl")
c2 = PowerPlant("Hiroshima")


o1 = TempObserver()
o2 = TempObserver()

c1.attach(o1)
c1.attach(o2)


c1.temperature = 800
c1.temperature = 100
