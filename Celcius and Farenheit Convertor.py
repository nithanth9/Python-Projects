print("""Would you like to convert from Celcius to Farenheit or Farenheit to Celcius? 
Enter 1 for Celcius to Farenheit or 2 for Farenheit to Celcius: """)
number = int(input())

def Celcius_to_Farenheit():
    Celcius = float(input("Enter the temperature in Degrees Celcius: "))
    convertor = ((9/5) * Celcius) + 32
    print("The temperature in Farenheit is",  convertor)

def Farenheit_to_Celcius():
    Farenheit = float(input("Enter the temperature in Degrees Farenheit: "))
    convertor_2 = (Farenheit - 32) * (5/9)
    print("The temperature in Celcius is",  convertor_2)

if number == 1:
    Celcius_to_Farenheit()
    
if number == 2:
    Farenheit_to_Celcius()