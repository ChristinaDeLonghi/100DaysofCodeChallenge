#when you want to iterate over a set number of items
banner = "Happy Birthday!"
for letter in banner :
    print(letter.upper())
    #for each time during the loop, the letter variable is set. 
    # the loop runs through each item on the right of 'in' (each letter in this case )
    # It sets the variable on the left of 'in' to that item. 
    # The object on the right of 'in' must be iterable. 
    # for loops run through each value in iterable eg, letters in string 