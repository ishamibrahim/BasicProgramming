
class Engine:
    def __init__(self):
        self.spin = 0

    def start(self, spin):
        self.spin = max(spin, 100)


class Motor:
    def __init__(self):
        self.spin = 0

    def start(self, charge):
        if charge > 5 :
            self.spin = 100 * charge

class Battery :
    def __init__(self):
        self.charge = 0


class Car:
    def __init__(self):
        self.battery = Battery()
        self.motorStart = Motor()
        self.engine = Engine()

    def turnon(self):
        self.motorStart.start(self.battery.charge)
        self.engine.start(self.motorStart.spin)

        if self.engine.spin > 3000:
            print("Car has been started with {} spin".format(self.engine.spin))

        else:
            print("Engine doesn't start")

    def jumpstart(self):
        self.battery.charge = 70




moto = Car()
moto.jumpstart()
moto.turnon()