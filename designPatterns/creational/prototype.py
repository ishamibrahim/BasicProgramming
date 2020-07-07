import copy


class Car:
    def __init__(self):
        self.name = "Nissan"
        self.model = "GTR 100"
        self.color = "GREY"

    def __str__(self):
        return "{0} - {1} of {2} color".format(self.name, self.model, self.color)


class Prototype:
    """
    The prototype can be used to clone new objects with variataions to the attributes.
    Instead of creating new objects from scratch

    clone() is a distinct feature of prototype class
    """
    def __init__(self):
        self._objects = dict()

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone_new(self, key, **attrs):
        obj = copy.deepcopy(self._objects[key])
        obj.__dict__.update(attrs)
        return obj


myproto = Prototype()

c = Car()
myproto.register_object("GTR 100", c)
print(c)

c1 = myproto.clone_new("GTR 100", model="Corolla", color="WHITE", name="Toyota")
myproto.register_object("Corolla", c1)

print(c1)
