"""
Creates a template or a pattern that the subclasses need to follow.



"""


class MakeFood(object):
    """
    The template to make food
    """
    def __init__(self, cost_of_ingredients):
        self.cost_of_ingredients = cost_of_ingredients

    def buy_ingredients(self, money):
        if money < self.cost_of_ingredients:
            assert 0, "Not enought money to buy ingredients"
        else:
            print("All ingredients to make {} available.".format(type(self).__name__))

    def cook(self):
        pass

    def serve(self):
        pass

    def make(self, money):
        self.buy_ingredients(money)
        self.cook()
        self.serve()


class MakePizza(MakeFood):

    def cook(self):
        print("Baking a pan pizza in a hot oven")

    def serve(self):
        print("Served hot pizza in cardboard box with Origami and Chilli flakes")


class MakePasta(MakeFood):

    def cook(self):
        print("Cooking pasta with Bolognese sauce")

    def serve(self):
        print("Served pasta on a Porcelain bowl")


pastaBaker = MakePasta(120)
pizzaBaker = MakePizza(99)

pastaBaker.make(200)
pizzaBaker.make(180)
