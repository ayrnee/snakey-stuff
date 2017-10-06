'''
git commands:
git stage
git commit -am "message"
git push

to create a branch and then checking it out
git checkout -b nameOfBranch
to check what branch you are on use
git branch
to switch branches use
git checkout nameOfBranch


Interactive language with build tools and package managers
package managers-anaconda and pip

size of any iterable comes with function len() for length

"he" * 3 = "hehehe"
[0] * 3 = [0,0,0]

loops:
range function takes in one mandatory arg and two default params
range(3): returns a list => [0,1,2]
range(number of what you want, starting num,step)

for i in range(5):
    print i
    #prints 0-4

lissy = ["helo", "boi", 7]
for i in lissy:
    print i
    #prints the list

for i in range(len(lissy)):
    print lissy[i]

i = 0
while (i < len(lissy)):
    print lissy[i]
    i += 1

Strings are ALWAYS immutable

Classes:


'''

import numpy
#Method1
#import copy
#copy.deepcopy(list_item)
#Method2
#from copy import *
#deepcopy(list_item)
from copy import deepcopy
import sys

sys.add.path("~/modules/new_module_project_dir")

import classes_prep

def f(x):
    return x ** 2 + 3 * x

def g(lissy):
    x = raw_input("give me something ")
    y = raw_input("give me another something")
    lissy2 = [x,y]
    lissy.extend(lissy2)
    return lissy

def main():
    # x = int(raw_input("give me a number "))
    #
    # x = 5
    # print x
    #
    # x = "hello"
    # print x
    #
    # lissy = []
    # lissy.append(51)
    # print lissy
    # lissy.append("boi")
    # print lissy.pop()
    # print lissy
    #
    # d = {"fourteen":14, "seven":7}
    # #in Java HashMap<string,int> = new HashMap<string,int>()
    # print d["fourteen"]
    lissy = [5, "world", "sevem" , 7]
    # g(lissy)
    # print lissy
    # x = deepcopy(lissy)
    # x.append("sissy")
    # print x
    # print lissy

    print lissy[-1]
    string = "   \n75\t22\n5 "
    string2 = string.strip()
    print string
    print string2

    word_list = string.split()

    ernger = classes_prep.Burger(tomato=True, bun="fuego", patty="human'")
    print str(ernger)




if __name__ == '__main__':
    main()
