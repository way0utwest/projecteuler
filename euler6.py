import sys
import time

def Solution(digits):
    One = SquareSum(digits)
    print(One)
    Two = SumSquare(digits)
    print(Two)
    return (One - Two)

def SquareSum(digits):
    sum = 0
    for x in (range(1, digits+1)):
        sum += x
    return (sum * sum)


def SumSquare(digits):
    sum = 0
    for x in (range(1, digits+1)):
        sum += (x*x)
    return (sum)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 10
    start = time.time()
    print(size, Solution(size))
    end = time.time()
    print("Elapsed:", end - start)
