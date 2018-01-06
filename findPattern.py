import sys

s1 = sys.argv[1]
s2 = sys.argv[2]

if s1.find(s2) == -1:
    print "not found"
else :
    print "found"

