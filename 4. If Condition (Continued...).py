print("\t\t4. If Condition (Continued...)")


'''3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.

Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"

Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"  '''


try:
    Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
    UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
    India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

    # In this program user can use both lower case and upper case to find the city : 

    city_name1=input("Enter a first city : ").strip().lower()
    city_name2=input("Enter a second city : ").strip().lower()

    all_cities_names={city.lower() for city in (Australia + UAE + India)}

    if city_name1 not in all_cities_names or city_name2 not in all_cities_names :
        raise ValueError("The cities are not from the above mentiones list")

    if city_name1  in[city.lower() for city in Australia] and city_name2  in[city.lower() for city in Australia]:
        print(" Both cities are in Australia")

    elif city_name1  in[city.lower() for city in UAE ] and city_name2  in[city.lower() for city in UAE]:
        print("Both cities are in UAE")

    elif city_name1 in [city.lower() for city in  India] and city_name2 in [city.lower() for city in  India] :
        print("Both cities are in India")

    else:
        print("They don't belong to the same country")


except Exception as exc:
    print("Error : ",exc)
    print("Enter the city name from the above list")
