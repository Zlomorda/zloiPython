from random import randint
from random import shuffle
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
from string import punctuation as punct


# Zloi (and Evil) Password Generator v. 1.0
# Can generate high, medium and low level passwords based on user desired lenght.
# For correct view use print("".join(passLow(USER_ENTERED_LEN))) command.'''

def passHigh(len):
    '''Generate high level password.
    Includes all available punctuations, numbers (0-9), lower and upper case characters.
    Based on user desired lenght.
    Example: 3$lbn*B<-IMr7B0
    For correct view use print("".join(passLow(USER_ENTERED_LEN))) command.'''

    lis = []
    i = 0
    while i < len:
        lis.append(lower[randint(0, 25)])
        i += 1
        if i == len:
            break
        lis.append(punct[randint(0, 25)])
        i += 1
        if i == len:
            break
        lis.append(upper[randint(0, 25)])
        i += 1
        if i == len:
            break
        lis.append(str(randint(0, 9)))
        i += 1
        if i == len:
            break
    shuffle(lis)
    return lis

def passMed(len):
    '''Generate medium level password.
    Includes only numbers (0-9), lower and upper case characters.
    Based on user desired lenght.
    Example: scc5Qf2W2K70cYD
    For correct view use print("".join(passLow(USER_ENTERED_LEN))) command.'''

    lis = []
    i = 0
    while i < len:
        lis.append(lower[randint(0, 25)])
        i += 1
        if i == len:
            break
        lis.append(upper[randint(0, 25)])
        i += 1
        if i == len:
            break
        lis.append(str(randint(0, 9)))
        i += 1
        if i == len:
            break
    shuffle(lis)
    return lis
    
def passLow(len):
    '''Generate low level password.
    Includes only numbers (0-9).
    Based on user desired lenght.
    Example: 800875488517709
    For correct view use print("".join(passLow(USER_ENTERED_LEN))) command.'''
    
    lis = []
    x = 1
    for x in range(len):
        lis.append(str(randint(0, 9)))
    return lis
