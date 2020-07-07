

# class GlobalAttrs:
#     """
#     Global attributes as class members
#     """
#     _shared_state = dict()
#
#     def __init__(self):
#         self.__dict__= self._shared_state


# class Singleton(GlobalAttrs):
#     def __init__(self, **kwargs):
#         GlobalAttrs.__init__(self, )
#         self._shared_state.update(kwargs)
#
#     def __str__(self):
#         return str(self._shared_state)



class Singleton():
    """
    There will only be one single instance of this singleton class
    using __new__method

    Another variant is the borg
    """
    _instance_exists = None

    def __new__(cls, song=""):
        if not cls._instance_exists:
            cls._instance_exists = object.__new__(cls)
        cls.song = song
        return cls

    def __str__(self):
        return str(self.val)


x = Singleton(song="Casablanca")
print("x : ", x.song)
y = Singleton(song="A WHOLE NEW WORLD")
print("x : ", x.song)
print("y : ", y.song )

z = Singleton(song="let it go")

print("x : ", x.song)
print("y : ", y.song)
print("z",  z.song)
