
class Borg:
    """
    Borg is like singleton, but it has different instances sharing the same values of  attributes.
    """
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state


b1 = Borg()
b2 = Borg()
b1.val = "Hi"

print("b1", b1.val)


b2.val = "Salaam"

print("b1", b1.val)
print("b2", b2.val)