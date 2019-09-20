class Star:
    def __init__(self, name):
        self._name = name

    def shine(self):
        return "Bright as the {}".format(self._name)


class Satelite:
    def __init__(self, name):
        self._name = name

    def shine(self):
        return "Dim as the {}".format(self._name)


class StarFactory:
    """
    Concrete Factory class
    """
    def get_body(self, name="star"):
        if name == "star":
            return Star("Beetelgeuse")

    def get_shine_color(self):
        return "Bright Orange"


class HeavenDemo:

    def __init__(self, heavenly_factory=None):
        self._factory_obj = heavenly_factory

    def describe_body(self):
        body = self._factory_obj.get_body()
        body_color = self._factory_obj.get_shine_color()

        print("The Object is a {}".format(type(body).__name__))
        print("The light - {}".format(body.shine()))
        print("The color of the body is - {}".format(body_color))

# concrete factory
star = StarFactory()

#Abstract factory
heavenly_body = HeavenDemo(star)

heavenly_body.describe_body()