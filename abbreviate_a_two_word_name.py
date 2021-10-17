# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

# def abbrev_name(name):
#     abrreviation = ''
#     nameArr = name.upper().split()
#     return nameArr[0][0:1] + '.' + nameArr[1][0:1]