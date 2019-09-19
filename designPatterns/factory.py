

class Star:
    def __init__(self, name):
        self.name = name

    def shine(self):
        return "Bright as the {}".format(self.name)


class Satelite:
    def __init__(self, name):
        self.name = name

    def shine(self):
        return "Dim as the {}".format(self.name)


def get_body(body="sun"):
    bodies = dict(sun=Star("sun"), moon=Satelite("moon"))
    return bodies[body]


moon = get_body("moon")
print(moon.shine())

sun = get_body("sun")
print(sun.shine())
