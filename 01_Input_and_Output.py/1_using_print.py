'''Typing python and the name of your program to run it (like they do in the video) only works if your computer is set up to find Python automatically. If it works for you, feel free to use that approach, but otherwise, it's not a problem.
If typing python doesn't work for you, the simplest way to run your program, and the one that works the most reliably regardless of your computer's configuration, is to make sure your program is saved with .py at the end of the filename, and then click the green play button in the upper right hand corner to run the program. Other students have also found that typing python3 or py instead of python has worked for their configuration. '''

'''Write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.
In the following example, the user types in "Blue" for their favorite color.

For this activity you will write a program that uses both input (obtaining data from the user via the keyboard) and output (displaying data to the user on the screen).
'''

def favorite_color():
    
    color = input("Please type your favorite color: ")
    
    print(f"Your favorite color is: ")
    print(color)
    
favorite_color()

# Please note that you can use either single quotes: 'Your favorite color is' or double
# quotes: "Your favorite color is" in your print and inputs statements and it will work
# just fine. It is completely a programmer preference.

''' Notice that the program displays back the color that the user entered, so it is different each time, depending on the color that was typed.

To make this program work, you will need to get input from the user and then save the data they provide into a variable. Then, at the appropriate time you print (i.e. display) the data stored in that variable.'''

