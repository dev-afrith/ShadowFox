print("\t\t\t1.Variables\n")

'''1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.'''

pi=22/7
print("Data type = ",type(pi))
print("\n")





'''2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.'''

'''
for=4        if we try to print this program it will results in a syntax error as 'for' is a keyword in python so it can't be printed
print(for) '''


#Alternately we can try the below program


for_value= 4   #here (for_value) is a variable used instead of 'for'
print(for_value)
print("\n")



'''3. Store the principal amount, rate of interest, and time indifferent variables and then calculate the Simple Interest for 3years. Formula: Simple Interest = P x R x T / 100'''


p = int(input("Enter the principal amount : " ))
r=  int(input("Enter the rate of interest : "))
t=3               #time for 3 years is given in question!

Simple_Interest = (p*r*t)/100
print("Simple Interest =  ", Simple_Interest )
print("\n\n")






