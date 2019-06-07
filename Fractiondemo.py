import Fraction

prompt = "> "

def readInput(message):
    print(message)
    num = input(prompt)
    return(num)

#Main

numer = 0

print("""
Welcome to FractionDemo.py
""")

while True:
    numer = readInput("Please enter a numerator")
    denom = readInput("Please enter a denominator")

    frac1 = Fraction.Fraction(numer, denom)
    frac1.checkNeg()
    frac1.printFraction()

    if(frac1.isZero() == True):
        break

    numer = readInput("Please enter a numerator")
    denom = readInput("Please enter a denominator")

    frac2 = Fraction.Fraction(numer, denom)
    frac2.checkNeg()

    frac3 = frac1.addFraction(frac2.getNumer(), frac2.getDenom())
    print("The sum of {} and {} is {}".format(frac1.toString(), frac2.toString(), frac3.toString()))
    print("")


print("The program will now close")
