import sys

if len(sys.argv) > 1:
    mylist = []
    for x in sys.argv[1:]:
        mylist.append(x)

print max(mylist)
