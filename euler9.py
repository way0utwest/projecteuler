'''
Euler 9



A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a*2 + b*2 = c*2

For example, 3^2 + 4*2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''


import sys
import time

def Solution(end):
    x, counter, answer = 2, 1, 0
    while counter <= (end + 1):
        if(IsPrime(x) == True):
            print(x)
            answer = x
            counter += 1
        x += 1
    return answer


def IsPrime(number):
    if number <= 3:
        return True
    if (number % 2 == 0) or (number % 3 == 0):
        return False
    i = 5
    while(i * i < number):
        if number % i == 0 or (number % (i+2) == 0):
                return False
        i = i + 6
    return True

# 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        param1 = int(sys.argv[1])
    else:
        param1 = 10001
    start = time.time()
    print("Parameter:", param1)
    print("Answer:", Solution(param1))
    end = time.time()
    print("Elapsed:", end - start)
