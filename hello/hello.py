import sys

#default for no arg
name = "World"

#set name var for arg passed in
if(len(sys.argv)>=2):
    name = sys.argv[1]

#print
print("Hello {0}".format(name))
