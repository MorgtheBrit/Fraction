
class Fraction:

    #Constructors

    def __init__(self, numer, denom):
        self.__numer = numer
        self.__denom = denom

    def __init__(self):
        self.__numer = 0
        self.__denom = 1

    #Print/String Functions

    def printFraction(self):
        print("{}/{}".format(self.numer, self.denom))

    def toString(self):
        frac = "{}/{}".format(self.numer, self.denom)
        return(frac)

    #Getters

    def getNumer(self):
        return(self.numer)

    def getDenom(self):
        return(self.denom)

    #Comparing Functions

    def isZero(self): #If numerator is equal to 0 then it returns true
        if(self.numer == 0):
            return(True)
        else:
            return(False)

    def isEqual(self, f2numer, f2denom):
        f1 = self.numer / self.denom
        f2 = f2numer / f2denom

        if(f1 == f2):
            return(True)
        else:
            return(False)

    def checkNeg(self): #If the denominator is negative on input it will assign the numerator the negative and remove it from the denominator
        if(self.denom < 0):
            self.numer = self.numer * -1
            self.denom = self.denom * -1

    #Math Functions

    def addFraction(self, f2numer, f2denom):
        f3numer = (self.numer * f2denom) + (self.denom * f2numer)
        f3denom = (self.denom * f2denom)
        frac3 = Fraction(f3numer, f3denom)
        return(frac3)

    def dblValue(self):
        return(self.numer/self.denom)
