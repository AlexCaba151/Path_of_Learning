'''Write a program that does the following:

Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

Here is an example of the tasks when run:

How old are you? 25
On your next birthday, you will be 26

How many egg cartons do you have? 3
You have 36 eggs

How many cookies do you have? 18
How many people are there? 8
Each person may have 2.25 cookies     '''
#This is for the first activity
print("================================================================")
def future_age():
    age = int(input("How old are your? "))
    number = 1
    result = age + number
    print(f"On next birthday, you will be {result} ")
future_age()
print("================================================================")

#This is for the second
def eggs_count():
    cartons = int(input("How many egg cartons do you have? "))
    total = cartons * 12
    print(f"You have {total} eggs ")
eggs_count()
print("================================================================")


#/this one is the third
def cookies_count():
    cookies= int(input("How many cookies do you have? "))
    people = int(input("How many people are there? "))
    result = cookies / people
    print(f"Each person may have {result:.2f} cookies ")
    
cookies_count()
print("================================================================")