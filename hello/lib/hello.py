import sys
import getpass

#author: Aashir Tuladhar (tuladhar@123.com)

#default for no arg
name = "World"

# adding in a class to get user name
def loggedUser():
    return getpass.getuser()

#set name var for arg passed in
if(len(sys.argv)>=2):
    name = sys.argv[1]

#print
print("Hello {0}".format(loggedUser()))
