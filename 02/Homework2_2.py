temperature_C = input("Please key in temperature in Celsius: ")  # read input
temperature_F = float(temperature_C) * 1.8 + 32  # convert the inout into floating point number
print("Temperature in Fahrenheit: {:.2f}".format(temperature_F))  # keep 2 decimals in result
