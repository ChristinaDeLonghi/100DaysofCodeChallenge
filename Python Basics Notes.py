print("hello")
#calling a funtion, open a parenthesis and closing parenthesis. Everything in between is an argument. Function call needs the closing parens to end. 
#Parsing is the way the interpreter breaks down the code you wrote into something it understands. 
#Be careful to match single and double quotes. 
#Create a string by surrounding text with quotation marks. 
#In python, everything you create is an object. You can refer to an object later by labelling it. These labels are called variables. They are object references - you can use them to refer to objects that have been created. 
#multiple arguements can go in a set of brackets/function and they are separated by commas
first_name = "Ada"
print("Hello,", first_name)
print(first_name, "is learning python")
#Gathering input in python
#call the input function, it outputs the prompt and then waits for an answer. 
current_mood = input ("How are you today?   ") # you can capture the input function in a variable. 
#Leave spaces for user experience and space to input info. 
#variable will return the input given by a user. 
first_name = input("What is your name?   ")
print ("Hello,", first_name)
#data types = integers = whole numbers (no decimal, answer to math of integers is stored in the variake _)
# , string = "series of characters in quotes"
#float = fraction, not a whole number, number with a decimal, used when you need more precision, always with division
# Can round floats to nearest int with round function eg round(_) 
#use Bedmas   type errors occur when you try to do math with incompatible data types. Even if the string is numeric, it is still a string not an integer
#Can coerce data types to make them others. You can pass a string to the function int() or float() to change the data type. 
#Can change between ints and floats as well, not the same as rounding though. 
# // divide but with answer as integer, get remainder with % 
#After you create a string it is immutable. \ tells the program to treat the next character as part of the string and not syntax, called an escape. 
#\n for new line, but in same line of code. 
#"""lets you use other "quotes in your sentence" """"
#combine strings with + for concatenation, include spaces because they will be pushed together Can store in a variable
#add to an immutable string like
dessert = "chocolate" + " marshmallow"
dessert = dessert + " graham crackers"
#use shortcut 'in place addition' 
dessert += " yum"
#repeat a string with * # of repetitions
#everything you create is an object, all objects can have abilities (methods)
#methods are functions that belong to an object. access methods with dot notation
#methods take parentheses, though don't necessarily require an additional argument
quote = "A person who never makes mistakes never tries anything new"
print(quote.title())
#coerce objects into strings with str() find out info about a method with help function
#{} are place holders in strings
#Booleans 
#Can coerce numbers to bools boo(). Any non zero number is true
#Any object that isn't empty is true. 
#true or false = true 
#true and false = false 
