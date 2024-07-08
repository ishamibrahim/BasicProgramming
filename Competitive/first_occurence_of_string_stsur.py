"""
Given two strings x and s, find the position of the first occurence of x in string s
x may have a "*" as a wildcard character

"""

def is_x_found(start, key, word):
    found = True
    for i in range(len(key)):
        if key[i] != "*" and key[i] != word[start+i]:
            found = False
            break

    return found


def firstOccurrence(s, x):
    x_point = -1
    for start in range(len(s)-len(x)+1):
         if is_x_found(start, x, s):
            x_point = start
            break
    return x_point

if __name__ == "__main__":
    print(firstOccurrence("abracadabra", "ca*ab"))
