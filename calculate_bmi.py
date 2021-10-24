# https://www.codewars.com/kata/57a429e253ba3381850000fb
def bmi(weight, height):
    b = weight / height ** 2
    if b <= 18.5:
        return "Underweight"
    elif b <= 25.0:
        return "Normal"
    elif b <= 30.0:
        return "Overweight"
    elif b > 30:
        return "Obese"