#If, or, else
# if expression, followed by colon, use double equals to check if something is true
first_name = input ("What is your name?   ")
if first_name == "Christina" :
    #colon opens up body of if statement
    #make sure all indents line up within body of statenent. 4 spaces
    print (f" {first_name} is learning python")
elif first_name == "Pepe" :
    print (f" {first_name} is also learning python") 
else :
    print (f"You should learn python {first_name}")
    #else statements start on same indentation as if statements
#end a block of code by going back to original indentation f and {} for format method
print (f"Have a great day {first_name}")
# to check if values are NOT equal use != bang
#Comparisons, use < or > to compare values. => use operands Can do this with string for alphabetical order
#can nest if statements 
first_name = input ("What is your name?   ")
if first_name == "Christina" :
    #colon opens up body of if statement
    #make sure all indents line up within body of statenent. 4 spaces
    print (f" {first_name} is learning python")
elif first_name == "Pepe" :
    print (f" {first_name} is also learning python") 
else :
    age = int(input("What is your age?  "))
    #coerce the string age data into an int
    if age <= 6 :
        print(f"wow! You're {age}! Cool, if you think you are ready!")
    print (f"You should learn python {first_name}")