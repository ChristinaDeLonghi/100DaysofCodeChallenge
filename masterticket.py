TICKET_PRICE = 10
tickets_remaining = 100
while tickets_remaining >= 1:
#while tickets_remaining: 
#use truth of variable (once down to zero, becomes false)
#tickets_purchased += 1
#tickets_remaining -= tickets_purchased
    print(f"There are {tickets_remaining} left")
    #gather users name and assign to new variable
    user_name = input("What is your name?   ")
    #prompt user by name and ask how many tickets they would like
    number_of_tickets = int(input(f"Hey {user_name}! How many tickets would you like?   "))
    #number_of_tickets = int(number_of_tickets)
    #calculate price of tickets 
    total_price = number_of_tickets * TICKET_PRICE
    #output price
    print(f"The total is {total_price}")

    #prompt user to proceed 
    proceed = input("Would you like to proceed? Y/N   ")
    #if proceed = "y".upper():
    if proceed.lower() == "y":
        print("Sold!")
        tickets_remaining -= number_of_tickets
        # A -= B -> A = A - B
        # A += B -> A = A + B
        # A++ -> A = A + 1
        # A-- -> A = A - 1
    else:
        print(f"Thank you {user_name}")
    #If they want to proceed
        #print sold 
    #otherwise thank them by name 
print("Sorry, all sold out")