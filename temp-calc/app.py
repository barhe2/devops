def temp_unit():
    while True:
        mode = input("Please choose base unit to convert (C or F):\n").strip().upper()
        if mode in ['C', 'F']:
            if mode == 'C':
                print("You chose Celsius.")
            elif mode == 'F':
                print("You chose Fahrenheit.")
            return mode
        else:
            print("Invalid input. Please enter 'C' or 'F'.")

# Example usage
unit = temp_unit()
print(f"You have selected {unit} as the temperature unit.")


def get_temp():
    while True:
        try:
            temp_num = float(input("Pick your temp to convert (as a number):\n"))
            return temp_num
        except ValueError:
            print("Invalid input. Please enter a number only.")

temp = get_temp()
print(f"You have entered {temp:.2f} as the temperature.")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32
    
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

if unit == 'C':
    converted_temp = celsius_to_fahrenheit(temp)
    print(f"{temp:.2f}°C is equal to {converted_temp:.2f}°F")
elif unit == 'F':
    converted_temp = fahrenheit_to_celsius(temp)
    print(f"{temp:.2f}°F is equal to {converted_temp:.2f}°C")
