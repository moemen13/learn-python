#!/usr/bin/python3.7
# author: moemen.ahmed@gmail.com
# date: 14 May 20
# purpose: test different ways to call and assign args in python

### Notice: all args are assigned by reference, not value.

def calculator(operands, opt='add' ):
    if opt == 'add':
        r = 0
        for o in operands: r += o
    elif opt == 'sub':
        r = operands[0]
        for o in operands[1:]: r -= o
    elif opt == 'multi':
        r = 1
        for o in operands: r *= o
    elif opt == 'div':
        r = operands[0]
        for o in operands[1:]: r /= o
    else: r = 'err'

    return r


def main():
    opt = input("Choose your operator: add, sub, multi, div: ")
    operands = []
    operands.append(int(input("Enter your operands: ")))
    while (operands[len(operands) - 1] != ""):
        num = input("Enter your operands: ")
        if num.isdigit():
            operands.append (int(num))
        else: break

    r = calculator(operands, opt)
    print ("result = " + str(r))


main()
