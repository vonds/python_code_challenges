# https://www.codewars.com/kata/56f6ad906b88de513f000d96
def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))

# def bonus_time(salary, bonus):
#     return '$' + str(salary * 10) if bonus else '$' + str(salary)