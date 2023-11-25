#!/usr/bin/env python3

def print_fibonacci(length):
    '''function print_fibonacci()'''
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib = [0, 1]
        fib.extend(fib[i - 1] + fib[i - 2] for i in range(2, length))
        print(fib)