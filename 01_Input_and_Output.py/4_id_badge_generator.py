'''Assignment
Write a program to prompt the user for the following:

First name

Last name

Email Address

Phone Number

Job Title

ID Number
In addition to the spacing and punctuation shown above, you must implement the following requirements:

The last name should be converted from whatever the user types to be displayed in ALL CAPS.

The job title should be displayed so that the first letter is capitalized.

The email address should be displayed in all lowercase.

An example of the program running is shown:


Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------
'''
def id_badge_generator():
    print("Please enter the following information:")
    print()
    first_name =input("Type your First  name: ")
    last_name = input("Type your Last name: ")
    email =input ("Type your Email address: ")
    phone = input("Type your Phone number: ")
    job =input("Type your Job title: ")
    id_number =input("Type your ID number: ")
    print(f"\nThe ID card is:")
    print("----------------------------------------")
    print(f"{last_name.upper()},{first_name.capitalize()}")
    print(f"{job.title()}")
    print(f"ID:{id_number}")
    print()
    print(f"{email.lower()}")
    print(f"{phone}")
    print("----------------------------------------")
id_badge_generator()
