#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if value < 0:
            for i, v in enumerate(str(abs(value))):
                if i == 0:
                    print("{:d}".format(int(v) * -1), end='')
                else:
                    print("{:d}".format(int(v)), end='')
                    
        else:
            for i in str(value):
                print("{:d}".format(int(i)), end='')
        print('')
        return True
    except TypeError:
        return False
