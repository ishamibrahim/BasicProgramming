# Python3 program for demonstrating coroutine chaining

def producer(sentence, next_coroutine):
    ''' 
    Producer which just split strings and 
    feed it to pattern_filter coroutine 
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    ''' 
    Search for pattern in received token 
    and if pattern got matched, send it to 
    print_token() coroutine for printing 
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                print(f"Sending {token} to next coroutine")
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    ''' 
    Act as a sink, simply print the 
    received tokens 
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(f"Received token {token}")
    except GeneratorExit:
        print("Done with printing!")

print("call 1")
pt = print_token()  # Won't do anything until __next__() is called
print("call 2")
pt.__next__()  # Will execute and wait for yield statement to execute
print("call 3")
pf = pattern_filter(next_coroutine=pt)
print("call 4")
pf.__next__()
print("call 5")
producer("The wyoming dependency isn't very amusing", next_coroutine=pf)
print("call 6")
