"""
Currency Converter in Python

This program takes in the current rate of conversion 
and the amount to be converted and returns the amount 
in the required currency.

"""
From = input("What are you converting from? ")
To = input("What are you converting to? ")
Amount = int(input("How much are you converting? "))
Rate = int(input("What is the current rate? "))

Result = Amount/Rate

print(str(Amount) + " " + From + " makes " + str(Result)+ " " + To)