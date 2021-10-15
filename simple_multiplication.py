#  https://www.codewars.com/kata/583710ccaa6717322c000105
def simple_multiplication(number):
    return number * 9 if number % 2 == 0 else number * 8

print(simple_multiplication(8)) # 64
print(simple_multiplication(7)) # 63

