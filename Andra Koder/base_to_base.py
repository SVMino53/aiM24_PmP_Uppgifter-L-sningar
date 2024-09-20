import argparse

parser = argparse.ArgumentParser(description='A script that calculates and shows an integer given in a certain base in other bases.\
                                (Digits above 9 are represented by letters, e.g. a=10, f=15)\
                                (Minimum: base 2, maximum: base 36)')

parser.add_argument('--number', type=str, help='Integer to calculate and show in other bases', required=True)

parser.add_argument('--base', type=int, default=10, help='The base that the given integer is in. Default = 10')
parser.add_argument('--new_base', type=int, default=2, help='Base to convert the integer to and show. Default = 2')

args = parser.parse_args()


def number_in_bases(number, base, new_base):
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'

    print(f'Base {base}: {number}')
    
    value = 0
    for position, digit in enumerate(number):
        digit_value = chars.index(digit)
        exponent = len(number) - position - 1
        value += base**exponent*digit_value

    new_number = ''

    while value != 0:
        digit_value = value % new_base
        new_number = chars[digit_value] + new_number
        value //= new_base
    
    print(f'Base {new_base}: {new_number}')


number_in_bases(args.number, args.base, args.new_base)