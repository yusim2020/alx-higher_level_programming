#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if char(a) != 'e' and char(a) != 'q':
        print("{:c}".format(a), end='')
