# I am converting celcius to farenhight
# 9/18/18
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Sean Allen

# ask user to put in a celsius temperature

Celsius = float (input ("please enter a temperature in Celsius: "))

# conveerting the temperature to farenhiet

Farenhight = ((9/5) * Celsius) + 32

# print farenhiet tempiture

print ("Farenhiet temperature is", format (Farenhight, ".1f"  ))
