# Fraction

# Title:
The title of this program is called Fraction, coded by Morgan James Humphreys updated till the 7th June. Fraction.py is the class file and FractionDemo.py is the client file. The purpose of the program is to have a simple fraction class that reads in two user defined fractions and add them together.

# Requirements/Specifications:
The program 'Fraction' was coded to the requirements asked for by the client. The program begins by starting the loop and asking for a fraction from the user, if the denominator of the fraction is negative it will swap the negative symbol with the numerator. The fraction will then print before asking for the next fraction from the user repeating the same process. The two fractions are then added together and displayed. The program then begins at the beginning of the loop. If a fraction that is the equivalent of zero for the first fraction entered of the loop then the program will close. 

Assumptions made about the program:

-User won’t input punctuation.
-User will know how to use the program.

# User Guide
## Running from CMD
Firstly, make sure you have python downloaded on your machine. Open the command line prompt to the file destination of Fractiondemo.py. You can do this be right clicking while holding shift and clicking on “open cmd here”. Input the command: “python Fractiondemo.py”. The program should now be running via the command line.

# Structure
The program starts by printing a welcome message and how to exit the program before beginning a do-while loop. As python does not have a do-while loop built-in I created one by having a continus loop until the exit clause is fulfilled where frac1 is equal to 0. The user input is read via the function readInput, you pass the message of what input you want from the user as the parameter. The first fraction object is then created, checked to see if the denominator is negative then the numerator is made negative and the denominator positive. The first fraction is then printed. The exit clause for the loop is then checked. The second fraction is then inputted and the same steps as frac1 are carried out. frac1 and frac2 is then added to create frac3, which is then printed. The loop then begins again.
