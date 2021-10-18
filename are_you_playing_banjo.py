# https://www.codewars.com/kata/53af2b8861023f1d88000832
# day 4
def are_you_playing_banjo(name):
    if name.lower()[0] == 'r':
        return '{} plays banjo'.format(name)
    else:
        return '{} does not play banjo'.format(name)

