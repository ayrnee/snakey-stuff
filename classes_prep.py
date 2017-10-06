'''
this is called the docstring - it's the highlevel program overview
'''

import numpy as np # we import the module numpy as the keyword np

class Burger():
    def __init__(self, tomato=True, bun="classic", patty="lamb"):
        ## this is the constructor, this makes the class for us
        ## everytime we instatiate the class, this function gets called
        ## every declaration requires initialization
        ## self is needed here since we need to specify unlike in c++
        self.tomato = tomato
        self.bun = bun
        self.patty = patty
        self.__hidden = False
        return

    def getTomato(self):
        return self.tomato

    def getBun(self):
        return self.bun

    def getPatty(self):
        return self.patty

    def getHidden(self):
        return self.__hidden


def main():
    array = np.ndarray([1, 2, 3, 4])
    # instead of:
    # array = numpy.ndarray([1, 2, 3, 4])
    moger = Burger() # moger is an instance of Burger
    # del moger
    # print moger.getTomato()
    # print moger.__hidden
    moger.bun = "flat"


if __name__ == "__main__":
    main()
