

class GlobalAttrs:
    """
    Global attributes as class members
    """
    _shared_state = dict()

    def __init__(self):
        self.__dict__= self._shared_state

class Singleton(GlobalAttrs):
    def __init__(self, **kwargs):
        GlobalAttrs.__init__(self, )
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)



x = Singleton(movie="Casablanca")
print (x)
y = Singleton(song="A WHOLE NEW WORLD")
print("x ; ", x)
print("y", y)

z = Singleton(song="let it go")

print("z", z.movie, z.song)