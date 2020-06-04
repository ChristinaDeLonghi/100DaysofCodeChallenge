import math
praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * (number_of_characters //2)
print (result)
#create a function with def, give it a name and define the parameters that are expected
def yell(text) :
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters //2)
    print (result)

yell ("You are doing great")
yell ("Don't repeat yourself")
#writing code to split a cheque. 
def split_cheque (total, number_of_people) :
    #two parameters needed for calculation in the function. colon to start body of fuction
    return math.ceil(total/number_of_people)
    # don't necessarily need to create a new variable to hold the information of cost per person (cost_per_person = math.ceil(total/number_of_people))
    #cost_per_person is the value we want to return within the function. 
    #can just return the value on one line instead of creating a new variable to return
    #use keyword return to do so. 
    #math.ceil function rounds up amount from calculation in parens

total_due = float(input("What is the total?  "))
#create a variavle for total_due, coerce it to be a float from a string so you have a number to work with that allows decimals 
number_of_people = int(input("How many people?  "))
#coerce the input to int so it's a number you can do math with (int, no need for decimal.)
amount_due = split_cheque (total_due,number_of_people)
#make variables arguments so it can be used with different answers, whatever input given by user. 
#value of cost per person is stored in variable amount_due
print (f"Each person owes {amount_due}")
#import math module so we can call on a function to round up (ceil)
#imports go at top of the file