"""
Write function bmi that calculates body mass index (bmi = weight / height2).
"""

def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5: 
        return "Underweight"

    elif bmi <= 25.0:
        return "Normal"

    elif bmi <= 30.0: 
        return "Overweight"

    elif bmi > 30:
        return "Obese"