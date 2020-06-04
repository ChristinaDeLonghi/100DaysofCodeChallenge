def split_cheque (total, number_of_people) :
    #two parameters needed for calculation in the function. colon to start body of fuction
    if number_of_people <= 1:
        raise ValueError("Please provide a number greater than 1")
    #use raise to raise an exception. As soon as it hits the raise line and the exception is raised, it exits that function. 
     #value needs to be greater than 1 for number of people, otherwise you get a division error. Can't have it look like the restaurant owes you money by having a negative number of people. 
    return math.ceil(total/number_of_people)
    # don't necessarily need to create a new variable to hold the information of cost per person (cost_per_person = math.ceil(total/number_of_people))
    #cost_per_person is the value we want to return within the function. 
    #can just return the value on one line instead of creating a new variable to return
    #use keyword return to do so. 
    #math.ceil function rounds up amount from calculation in parens

#total_due = float(input("What is the total?  "))
#create a variavle for total_due, coerce it to be a float from a string so you have a number to work with that allows decimals 
#number_of_people = int(input("How many people?  "))
#coerce the input to int so it's a number you can do math with (int, no need for decimal.)
#amount_due = split_cheque(total_due,number_of_people)
#make variables arguments so it can be used with different answers, whatever input given by user. 
#value of cost per person is stored in variable amount_due
#print (f"Each person owes {amount_due}")
#import math module so we can call on a function to round up (ceil)
#imports go at top of the file
#can put code you think might cause exceptions in a try 
try:
    #put possibly problem code in try block
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_cheque(total_due,number_of_people) 

 
except ValueError as err:
#put what error you expect and a message to tell user about error
#use as to get reference to exception that was raised. 
    print ("Oh no, that's not a real value")
    print (f"{err}")
#try block allows for an else so that some code only runs if it doesn't cause the error.
else:
     print (f"Each person owes {amount_due}")

