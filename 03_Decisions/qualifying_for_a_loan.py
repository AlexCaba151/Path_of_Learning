'''Activity Instructions
For this activity, you will implement a simplistic system to determine if a user can qualify for a loan.

The Problem: Qualifying for a loan
When loaning money to someone, you want to have some level of confidence that they will be able to repay the loan.

There are different characteristics you might base this decision on, or different questions you might 
ask someone. And depending on their answers to those questions, you might ask other questions. For 
example, consider the following possible questions:

-Does the person have a job, and if so, how long have they worked there, and how much money do they make?

-Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)

-Does the person have a good credit score or history of paying back loans?

-How much other debt does the person have?

-How much money does the person have?

-Will the person have a down payment, and if so, what percentage of the loan does it amount to? '''

def loan_apply():
    print("Welcome to the Qualifying for a Loan Program! ")
    print("===========================================================")
    print("-First, Rate from 1-10 on the following information: ")
    
    large = int(input("How large is the loan? "))
    credit =int(input("How good is your credit history? "))
    income =int(input("How high is your income? "))
    down_payment = int(input("How large is your down payment? "))
    print("===========================================================")
# For safety sake, I always like to set the variable to a default value of False
# That way, if for some reason it doesn't get set it in our rules below it will
# not be left "undefined" and cause an error, and I don't like to set the default
# to be True, because I don't want to accidentally give someone a loan!
    should_loan = False
    
    if large >= 5:
        if credit >= 7 or income >= 7:
            should_loan= True
        elif credit >= 7 or income >=7:
            if down_payment >=5:
                should_loan = True
            else:
                should_loan = False
            
    else: #This means its a small loan
            
        if credit < 4:
            should_loan= False
        else:
            if income >= 7 or down_payment >= 7:
                should_loan = True
            elif income >= 4 or down_payment >= 4:
                should_loan = True
            else:
                should_loan = False
    
    if should_loan:
        print("The decision is YES!. This is good loan. ")
    else:
        print("The decision is NO!. You should not loan this money.")
        print("===========================================================")
loan_apply()
# In case you are wondering, all of the above if/elif/else statements
# could be combined into one great big huge if statement, but I've left it
# this way to better match the rules that were provided.