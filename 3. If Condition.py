print("\t\t3. If Condition ")


'''1. Write a program to determine the BMI Category based on user input. 
Ask the user to: 
Enter height in meters 
Enter weight in kilograms 
Calculate BMI using the formula: BMI = weight / (height)2 
Use the following categories: 
If BMI is 30 or greater, print "Obesity" 
If BMI is between 25 and 29, print "Overweight" 
If BMI is between 18.5 and 25, print "Normal" 
If BMI is less than 18.5, print "Underweight"  '''

try:
    height = float(input("Enter the height in meters : "))
    weight = float(input("Enter the weight in kilograms : "))

    BMI = weight / (height**2)
    print(f"Your BMI is :{BMI:.2f} ")

    if BMI>=30 :
        print("Obesity")
    elif 25<=  BMI<=29.9 :
        print("Overweight")
    elif 18.5 <= BMI <25 :
        print("Normal")
    else :
        print("Underweight")
    
except ValueError:
    print("Please , Enter only numbers ")

print("\n")



'''2. Write a program to determine which country a city belongs to. Given
 list of cities per country: 
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
Ask the user to enter a city name and print the corresponding country.
 Example: 
Enter a city name: "Abu Dhabi" 
Output: "Abu Dhabi is in UAE" '''




Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# In this program user can use both lower case and upper case to find the city : 

city_name=input("Enter a city name : ").strip().lower()

if city_name in[city.lower() for city in Australia] :
    print(f"{city_name.title()} is in Australia")

elif city_name in [city.lower() for city in  UAE] :
    print(f"{city_name.title()} is in UAE")

elif city_name in [city.lower() for city in  India] :
    print(f"{city_name.title()} is in India")

else:
    print("City not found from the above data")



