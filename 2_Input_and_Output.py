'''Overview
I will build on the basic input/output ideas from your programs in 
the last lesson, and learn to store more information and display 
it using better formatting. While not all programs use the console input and output approach 
that we have taken thus far (where people type the answers 
and see the results in text), almost all programs make use of many string variables and combine 
and format them in one form or another. '''

'''Variables
One of the things you learned in the previous lesson was how to store data in a variable. A variable is like a name that we attach to that data, so that later we can refer to it when we need it.
In your programs this week, you are going to start to see many variables used simultaneously in the same program. This is very common, and doesn't cause any problem for the computer. As long as you are consistent and always use the same name for the same data, you won't have any problems.
Because we will have to keep track of more and more variables, it becomes increasingly important to choose good names for them. For example, while you may remember what x means now, in a few weeks, months, or years, you might forget. On the other hand a variable name like 
color or even favorite_color is much 
more descriptive and will help you and others better understand your code.'''

def combine_strings():
    first_name =("Christopher ")
    last_name =("Harrison")
    print(first_name + last_name)
    print("Hello " + first_name + "" + last_name)
    
combine_strings()