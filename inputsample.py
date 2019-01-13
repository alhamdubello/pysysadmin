#!/usr/bin/env python3.6

##Collect user input

##We want to collect a persons name , age

name = input ("What is your name? ")
birthdate = input ("What is your birthdate? ")

age = int(input ("How old are you?"))

print(f"{name} was born on {birthdate}")
print(f"Half of your age is {age / 2}")
