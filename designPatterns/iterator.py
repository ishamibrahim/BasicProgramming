
def count_arab(count):

    arab_numbers = ["wahad", "saani", "salas", "arbae", "khams", "shith", "sabe", "samani", "tisae", "ashrae"]

    iterator = zip(range(count), arab_numbers)

    for i, number in iterator:
        yield number


for arb in count_arab(3):
    print(arb)

