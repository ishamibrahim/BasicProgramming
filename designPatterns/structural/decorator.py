

def add_footer(function):

    def decorator():
        ret = function()

        return "{} \n subject to copyright".format(ret)
    return decorator

@add_footer
def best_song():
    return "And I cant stop falling in love with you"


print(best_song())
########################################################################################################################

class CakeAbstract(object):
    """
    the decorate() is the function that is inherited throughout multiple inheritances. Even though all classes inherit
    one single Parent. The way objects are initialized keeps decorators layered over one another. 
    """
    def __init__(self, cake):
        self._cake = cake

    def decorate(self):
        print("Decorating the cake")


class Cake(object):

    def decorate(self): pass


class Frosting(CakeAbstract):
    def add_frosting(self):
        print("Adding white frosting to the cake")

    def decorate(self):
        self.add_frosting()
        self._cake.decorate()

class Topping(CakeAbstract):
    def add_topping(self):
        print("Topping with chocolate shaved")

    def decorate(self):
        self.add_topping()
        self._cake.decorate()

class Garnishing(CakeAbstract):
    def add_garnishing(self):
        print("Gramoshng with strawberry pieces")

    def decorate(self):
            self.add_garnishing()
            self._cake.decorate()


acake = Cake()

fcake = Frosting(acake)

tcake = Topping(fcake)

gcake = Garnishing(tcake)
gcake.decorate()

