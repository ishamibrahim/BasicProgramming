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


pt = print_token()  # Won't do anything until __next__() is called

pt.__next__()  # Will execute and wait for yield statement to execute

pf = pattern_filter(next_coroutine=pt)

pf.__next__()

producer("The wyoming dependency isn't very amusing", pf)
