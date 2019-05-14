#!/usr/bin/python3
from scipy import pi
import sys

def retpi(numdig):
    num=str(pi)
    for dig in range(numdig+1):
        yield num[dig]

def getinp():
    try:
        print(f"How many digits of pi do you want? The maximum number of digits we can give is {len(str(pi))-1}. To exit type 0.")
        try:
            numdigits=int(input())
        except:
            print(sys.exec_info[0])
            sys.exit()
        print(numdigits)
        print('Here')
        if numdigits==0:
            print('called')
            print('I hope you found this program useful')
            quit()
            print('past quit')
        else:
            print(''.join(list(retpi(numdigits))))
    except KeyboardInterrupt:
        quit()
    except:
        print('An error occured try again')



if __name__ == '__main__':
    while True:
        getinp()
