
"""
 Used to separate the Object on whom an action is performed  and the object that performs the operation
"""


class Screen(object):
    def __init__(self, text):
        self.text = text
        self._clipboard = ""

    def cut(self, start, end):
        self._clipboard = self.text[start:end]
        self.text = self.text[:start] + self.text[end:]

    def copy(self, start, end):
        self._clipboard = self.text[start:end]

    def __str__(self):
        return self.text

    def clear_clipboard(self):
        self._clipboard = ""

    def paste(self, offset):
        self.text = self.text[:offset] + self._clipboard + self.text[offset:]


class ScreenCommand(object):
    def __init__(self, screen):
        self.screen = screen
        self.previous_state = screen.text

    def execute(self):
        pass

    def undo(self):
        pass


class CutCommand(ScreenCommand):
    def __init__(self, screen, start=0, end=0):
        super().__init__(screen)
        self.start = start
        self.end = end


    def execute(self):
        self.screen.cut(start=self.start, end=self.end)

    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state


class PasteCommand(ScreenCommand):
    def __init__(self, screen, offset=0):
        super().__init__(screen)
        self.offset = offset


    def execute(self):
        self.screen.paste(offset=self.offset)

    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state


class CommandClient(object):
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


myscreen = Screen("Aye Captain")
print(myscreen)
cut_command = CutCommand(myscreen, 0, 4)

cclient = CommandClient()
cclient.execute_command(cut_command)
print(myscreen)

paste_command = PasteCommand(myscreen, offset = 7)
cclient.execute_command(paste_command)

print(myscreen)



cclient.undo_last()
print(myscreen)

cclient.undo_last()
print(myscreen)

