class Star:
    def __init__(self, name="Beetelgeuse"):
        self._name = name

    def shine(self):
        return "Bright as the {}".format(self._name)


class Satelite:
    def __init__(self, name="Titan"):
        self._name = name

    def shine(self):
        return "Dim as the {}".format(self._name)


class HaevenInterface:
    def get_heavenly_body(self):
        pass


class HeavenFactory:
    """
    Concrete Factory class
    """
    def __init__(self, name):
        self._name = name

    def get_heavenly_body(self):
        if self._name == "star":
            return Star()
        elif self._name == "satelite":
            return Satelite()


def describe_body():
    factory = HeavenFactory("satelite")
    heavenly = factory.get_heavenly_body()
    print(heavenly.shine())

describe_body()

