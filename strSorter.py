import sys


if len(sys.argv) > 1:
    mylist = []
    # sys.argv[0] is the program filename, slice it off
    for element in sys.argv[1:]:
        mylist.append(element)

mylist.sort()

print mylist
