'''Activity Instructions
Overview
An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond." For this assignment you will write a program that asks for your name and repeats it back in this way.

Instructions
Prompt the user for their first name. Then, prompt them for their last name. Display the text back all on one line saying, "Your name is last-name, first-name, last-name" as shown:


What is your first name? Scott
What is your last name? Burton

Your name is Burton, Scott Burton.

What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.'''

def name_and_last_name():
    first_name = input("What's  your first name? ")
    last_name =input("What's your last name? ")
    print(f"your name is {last_name.title()}, {first_name.title()} {last_name.title()}")

name_and_last_name()
# Be aware that there are many ways to do the formatting of that line, such as:
# print("Your name is " + last + ", " + first + " " + last + ".")
# print("Your name is {}, {} {}.".format(last, first, last))
# print("Your name is {0}, {1} {0}.".format(last, first))