
"""
USed when there is different signatues in similar classes. Adapter blends both signature based on the
object that's being called
"""

class Indian:
    def __init__(self):
        self.name = type(self).__name__


    def speak_indian(self):
        return "Namashkaar Dost"


class Arabian:
    def __init__(self):
        self.name = type(self).__name__

    def speak_arabic(self):
        return "Asslamau alaikum Habeebi"


class Adapter:
    def __init__(self, person, **adapted_method):
        self._person = person
        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        """Return rest of the items"""
        return getattr(self._person, item)


arabian = Arabian()
indian = Indian()

adapter_a = Adapter(arabian , speak=arabian.speak_arabic)
adapter_i = Adapter(indian, speak=indian.speak_indian)

objects = [adapter_a, adapter_i]
for obj in objects:
    print("An {} would say - {}".format(obj.name, obj.speak()))
