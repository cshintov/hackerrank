from read_input import read_lines
from itertools import islice

if __name__ == '__main__':
    number_of_entries = input()

    lines = read_lines()

    phone_book = {
        name: phone_number 
        for name, phone_number in islice(lines, number_of_entries)
    }

    for name, in lines:
        phone_number = phone_book.get(name, None)
        print name + '=' + phone_number if phone_number else 'Not found'

