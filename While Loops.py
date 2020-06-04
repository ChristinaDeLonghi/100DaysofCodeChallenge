#code that continually repeats until a certain condition is no longer met
import sys
MASTER_PASSWORD = 'opensesame'
#caps for variables that should not change throughout running the code. Better to put it at the top set of variables than only in the while loop itself. 
password = input("Please enter your password:  ")
attempt_count = 1 #want to limit the number of attempts allowed. 
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many password attempts")# message given to user
        #will exit the loop if the number of attempts is more than three. 
        #breaks out of the loop if 'if' conditional is met. 
    password = input ("Invalid password, try again: ")
    attempt_count += 1
    #this adds the number of attempts plus one. 
    #while starts a block of code that will continue to loop until the condition set out in the block is met. 
    