import sys
def CheckPalidrome(StartPoint, digits):
    x = StartPoint
    end = (10 ** (digits - 1)) - 1
    winner = 0
    print("lower bound", end)
    while x > end:
        y = x
        while (y > end):
            check = str(x * y)
            if ( check == check[::-1] ):
                print("found", x, y, check)
                if ((x * y) > winner):
                    winner = x * y
            #print(x, " x ", y, " = ", check)
            y -= 1
        x -= 1
    return winner



if __name__ == "__main__":
    start, size = int(sys.argv[1]), int(sys.argv[2])
    if start is None:
        start, size = 99, 2
    print(start, CheckPalidrome(start, size))
    #for i in range(25):
    #    print(i, IsPrime(i))
