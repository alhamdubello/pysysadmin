#!/usr/bin/env python3.6

##BMI script

## BMI = (weight in kg/ height in meters squared)
## Imperail version BMI * 703


## Gather infomation from user in a function

def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (inches or meters) "))
    system = input("Are your measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calc_bmi(weight, height, system='metric'):
    """
    Return the Body Mass index and measurement system
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi
while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calc_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calc_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please, use imperial or metric.")
