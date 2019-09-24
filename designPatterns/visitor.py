"""
Allows adding features to an existing class without changing the code base of the original object

"""

class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def workon_plumber(self, plumber):
        print("{0} is working in the {1}".format(plumber, self, ))

    def workon_electrician(self, electrician):
        print("{0} is working in the {1}".format(electrician, self, ))

    def __str__(self):
        return type(self).__name__


class Visitor(object):
    def __str__(self):
        return type(self).__name__


class Plumber(Visitor):
    def visit(self, house):
        house.workon_plumber(self)


class Electrician(Visitor):
    def visit(self, house):
        house.workon_electrician(self)


elt = Electrician()
plb = Plumber()

home=House()

home.accept(elt)
home.accept(plb)
