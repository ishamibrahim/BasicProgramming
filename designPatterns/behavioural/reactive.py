"""
This is based on a pyton package 'rx'.

Used for reactive programming.
Can be used on multiple streams of data. i.e handling event handling based on the stream input.

A stream is represented as `observable`.

"""

from rx.core import Observer, Observable, I

class MyObserver(Observer):

    def on_next(self, val):
        print("Read : ", val)

    def on_completed(self):
        print("Values completed")

    def on_error(self, error):
        print("Error found here : ", error)




def main():
    xs = Observable.pipe(range)
    xs.subscribe(MyObserver)


main()