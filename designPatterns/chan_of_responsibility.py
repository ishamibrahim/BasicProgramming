"""
 Used when many different processing has to be done based on the request. The request is sent to individual process
 based on the chain to whichever handler  is able to handle the request
"""



class Handler(object):
    def __init__(self, successor):
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request)

        if not handled :
            handled = self._successor.handle(request)

    def _handle(self, request):

        raise NotImplementedError("The parent handle hasnt been defined yet")


class SubHandler(Handler):
    def __init__(self, successor):
        Handler.__init__(self, successor)

    def _handle(self, request):
        if 0 < request <= 10 :
            print(" {} Handled by the Subhandler".format(request))
            return True


class SubSubHandler(Handler):
    def __init__(self, successor):
        Handler.__init__(self, successor)

    def _handle(self, request):
        if 10 < request <= 30 :
            print(" {} Handled by the SubSubHandler".format(request))
            return True

class DefaultHandler(Handler):
    def _handle(self, request):
        print("{} Cannot be handled even by Default Handler".format(request))
        return True


class Client:
    def __init__(self):
        self.handler = SubHandler(SubSubHandler(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

c = Client()

c.delegate([10, 4, 25, 80])