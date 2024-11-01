def celsius_to_fahrenheit(celsius): 
    return(celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit): 
    return(fahrenheit - 31) * 5/9

def temp_converter(): 
    while True:
        try:
            temp_input = int(input("Choose the temperature scale to convert: \n1. Celsius to Fahrenheit \n2. Fahrenheit To Celsius \nEnter 1 or 2: "))
            if temp_input not in [1,2]:
                print("Invalid Option. Please Choose 1 or 2")
                continue
            
            if temp_input == 1: 
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F")
                
            else:
                fahrenheit = float(input("Enter your temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C")
                
            break
        
        except ValueError:
            print("Please Enter a Valid Number")

temp_converter()