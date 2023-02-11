
def palindrome(*args):

    inputWord=args
    revword=inputWord[::-1]

    if inputWord == revword:
        return print('palindromo')
    else:
        return print('no palindromo')

palindrome('pata')