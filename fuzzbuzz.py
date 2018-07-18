import sys
import unicodedata

def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


def main(argv):
    assert argv
    
    if argv[0].isdigit:
        number = int(argv[0])
    else:
        number = 21

    print ('\n'.join(fizzbuzz(n) for n in range(1, number+1)))

if __name__ == '__main__':
    main(sys.argv[1:])
