import copy

class Car:
    def __init__(self):
        self.name = "BMW"
        self.model =  "GT 100"
        self.color = "GREY"

    def __str__(self):
        return "{0} - {1} of {2} color".format(self.name, self.model, self.color)

class Prototype:
    def __init__(self):
        self._objects = dict()

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone_new(self, name, **attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


myproto = Prototype()

c = Car()
myproto.register_object("GT 100", c)
print(c)

c1 = myproto.clone_new("GT 100", model = "Corolla", color = "WHITE")
myproto.register_object("Corolla",c1)

print (c1)
