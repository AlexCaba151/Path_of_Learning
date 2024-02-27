'''Assignment
Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

Here is an example of the program when it runs:


What is the temperature in Fahrenheit? 81
The temperature in Celsius is 27.2 degrees. '''

import math
def temperature():
    t_fahrenheit= int(input("What is ther temperature in Fahrenheit? "))
    t_celcius = (t_fahrenheit - 32) * 5/9
    print(f"The temperature in Celcius is {t_celcius:.1f}")
temperature()


'''Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

1. Try the values in the examples on this page and ensure that your program generates the same results.

2. Verify that you are displaying the result to 1 decimal point of precision as shown.

3. Try converting 32 degrees Fahrenheit (freezing, which should be 0 degrees Celsius) and 212 degrees (boiling, which should be 100 degrees Celsius)

4. Try converting 0 and a negative number and make sure they come out as you would expect.

5. Verify that you have used good style, by checking the variable names you have used as well as the use of blank lines and whitespace around your operators.'''