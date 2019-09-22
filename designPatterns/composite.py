"""
Used when there is a tree structure involved in the objects
"""


class Component:
    def __init__(self, *args, **kwargs):
        self._name = args[0]

    def component_function(self):
        pass


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print("object of {}".format(self._name))

        for child in self.children:
            child.component_function()


class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

    def component_function(self):
        print("object of {}".format(self._name))


top = Composite("Main menu")

sub1 = Composite("Starters")
sub11 = Child("Sukka Chicken")
sub12 = Child("Sukka Paneer")

sub2 = Composite("Dessert")
sub21 = Child("Brown Brownie")
sub22 = Child("Chocolate fudge")

# Create the tree structure menu
sub1.add_child(sub11)
sub1.add_child(sub12)
sub2.add_child(sub21)
sub2.add_child(sub22)
top.add_child(sub1)
top.add_child(sub2)


top.component_function()
