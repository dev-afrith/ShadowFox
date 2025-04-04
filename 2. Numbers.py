print("\t\t\t2.Numbers\n")

''' 1. Write a function that takes two arguments, 145 and 'o', and
 uses the `format` function to return a formatted string. Print the
 result. Try to identify the representation used.'''


number = 145                                     
formt = 'o'
result = format(number, formt)
print("Result = " ,result)

#Explanation:
'''In the above program the variable number assigns a value of 145 and
the variable formt contains a value 'o' which is a octal representation
which converts the decimal value to octal(base 8) when it converts to
octal it gives a value of 221 base₈(octal)'''

print("\n")


''' 2. In a village, there is a circular pond with a radius of 84 meters.
 Calculate the area of the pond using the formula: Circle Area = π
 r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
 1.4 liters of water in a square meter, what is the total amount of
 water in the pond? Print the answer without any decimal point in
 it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
 Water per Square Meter '''


pi = 3.14
radius = 84
water_sqr_meter= 1.4

area_of_the_pond = pi*(radius**2)

total_amount_of_water_in_pond = area_of_the_pond  * water_sqr_meter

print("Water in the pond = ",(int(total_amount_of_water_in_pond )))





'''3. If you cross a 490meterlong street in 7 minutes, calculate your
 speed in meters per second. Print the answer without any decimal
 point in it. Hint: Speed = Distance / Time '''



Distance=490
Time=7*60            #convert the minutes into seconds
Speed=Distance/Time
print("\n")
print("Speed = ",int(Speed)) 






