'''Activity Instructions
Practice writing programs that compare strings and numbers.

Comparing Numbers
Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".'''

def comparing_strings():
    print("==============================")
    first_num = int(input("What's the first number? "))
    second_number = int(input("What's the second number? "))
    print("=================================")
    if first_num > second_number:
        print("1-The first number is greater")
    else:
        print("1-The first number is not greater")
        
    if first_num == second_number:
        print("The numbers are equals")
    else:
        print("2-The numbers are not equal")
    if second_number > first_num:
        print("3-The second number is greater")
    else:
        print("3-The second number is not greater")
    print("=================================")
    animal = input("What's your favorite animal? ")
    if animal.lower() == ("bear"):
        print("That's my favorite animal too! ")
    else:
        print("That one isn't my favorite!")
    print("=================================")
comparing_strings()

'''Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

1. Test the first part of your program with pairs of numbers where the first is greater and also where 
the second is greater. Verify that all three values that are printed are correct.

2. Test it with two numbers that are equal. Verify that all three values that are printed are correct.

3. Test the second part of your program with an animal that is different. Verify that the correct message is shown.

4. Test it with an animal that is the same. Verify that the correct message is shown.

5. Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.'''