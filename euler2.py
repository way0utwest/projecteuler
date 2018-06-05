import sys


def euler2(limit):
    sum = 0
    a, b = 1, 2
    while b < limit:
        if (b % 2 == 0):
            sum += b
            print("adding", b)
        a, b = b, a+b
    return (sum)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        top = 4000000
    else:
        top = sys.argv[1]
    y = euler2(top)
    print("Sum: ", y)
