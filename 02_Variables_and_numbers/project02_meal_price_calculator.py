'''Instructions
Compute the price of a meal as follows by asking for the price of child and 
adult meals, the number of each, and then the sales tax rate. Use these values 
to determine the total price of the meal. Then, ask for the payment amount and compute the 
amount of change to give back to the customer.

Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

Ask the user for the following:

-The price of a child's meal (floating point)

-The price of an adult's meal (floating point)

-The number of children (integer)

-The number of adults (integer)

-Then, complete the following steps:

-Determine the meal's subtotal (before adding sales tax) by multiplying the number of children 
by the price of their meal, and multiplying the number of adults by the price of their meal and 
adding those two values together.

Hint from Instructor:
As you will see in the requirements list below, this is all that is needed for the milestone requirements in 
the middle of the week, but you should try to get as far as you can to make it even easier for yourself to finish 
the week, especially if you run into trouble.

Ask the user for the sales tax rate as a percentage (floating point). Please note that thispercentage should be 
entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.

Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

Compute and display the total price of the meal by adding the subtotal and the sales tax. '''

import math
def meal_calculator():
    print("Welcome to The Meal Calculator!")
    print("=============================================")
    print("Enter the Following information: ")
    #User question about prices and persons
    child_meal = float(input("What's the price of a child's meal? "))
    adult_meal = float(input("What's the price of an adult meal? "))
    children_num = int(input("How many children are there? "))
    adults_num = int(input("How many adults are there?  "))
    subtotal = children_num * child_meal + adults_num * adult_meal
    print(f"Subtotal: ${subtotal}")
    print("=============================================")
    #Tax rate question and calculation
    tax_rate = float(input("What's the sales tax rate? "))
    sales_tax = subtotal * tax_rate / 100
    total = subtotal + sales_tax
    print(f"Tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("=============================================")
    #Payment and charge calculation
    payment =int(input("What's the payment amount? "))
    charge = payment - total
    print(f"Charge: ${charge:.2f}")
print("=============================================")
meal_calculator()

'''Final requirements
At the end, in addition to the milestone requirements above, you need to also complete the following:

1. Ask the user for the sales tax rate and store the value properly as a floating point number.

2. Compute and display the sales tax.

3. Compute and display the total.

4. Ask the user for the payment amount and store the value properly as a floating point number.

5. Compute and display the change.

6. Include the appropriate currency symbol (for example $, €, etc.) before each displayed value.

7. Display each value to two decimals.

8. Double check that the calculations are correct.

9. Show creativity and exceed the core requirements by adding additional features.

10. Use good style in your program, including variable names and whitespace.'''