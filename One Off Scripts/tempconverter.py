temperatures=[10,-20,-289,100]

def celsius_to_fahrenheit(celsius):
    if int(celsius) == 0:
        fahrenheit = 32
    else:
        fahrenheit = int(celsius) * 9/5 + 32
    return fahrenheit


for i in temperatures:
    if float(i) >= -273.15:
        print(celsius_to_fahrenheit(i))
    else:
        print("The lowest it can be is -273.15.")
