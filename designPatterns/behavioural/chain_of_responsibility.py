"""
 Used when many different processing has to be done based on the request. The request is sent to individual process
 based on the chain to whichever handler  is able to handle the request
"""



class Handler(object):
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled :
            handled = self._successor.handle(request)

    def _handle(self, request):

        raise NotImplementedError("The parent handle hasn't been defined yet")


class SubHandler(Handler):
    def __init__(self, successor):
        Handler.__init__(self, successor)

    def _handle(self, request):
        if 0 < request <= 10 :
            print(" {} Handled by the Subhandler".format(request))
            return True


class SubSubHandler(Handler):
    def __init__(self, successor):
        Handler.__init__(self, successor)

    def _handle(self, request):
        if 10 < request <= 30 :
            print(" {} Handled by the SubSubHandler".format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print("{} Cannot be handled even by Default Handler".format(request))
        return True


class Client:
    def __init__(self):
        self.handler = SubHandler(SubSubHandler(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

c = Client()

c.delegate([10, 4, 25, 80])

##########################################################################

class Car(object):
    def __init__(self, name, water, fuel, oil):
        self.name = name
        self.water = water
        self.fuel = fuel
        self.oil = oil

    def is_fine(self):
        print(self.water, self.fuel, self.oil)
        if self.water >= 20 and self.fuel > 5 and self.oil > 50:
            print("Car has good essential liquid levels")
            return True
        else:
            return False

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, car):
        if car.is_fine() and self._successor is not None:
            self._successor.handle(car)
            


class WaterHandler(Handler):
    def handle(self, car):
        if car.water < 20:
            print("Adding water")
            car.water = 50
        self._successor.handle(car)


class FuelHandler(Handler):
    def handle(self, car):
        if car.fuel < 5:
            print("Adding fuel")
            car.fuel = 10
        self._successor.handle(car)


class OilHandler(Handler):
    def handle(self, car):
        if car.oil < 50:
            print("Adding oil")
            car.oil = 200
        self._successor.handle(car)



car = Car("contessa", 10, 10, 70)

handler = WaterHandler(OilHandler(FuelHandler(Handler())))

handler.handle(car)

