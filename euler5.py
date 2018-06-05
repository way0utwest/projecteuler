import sys
def FindSmallest(digits):
    winner, x, done = 0, 10, False
    while (done == False):
        keeplooping = True
        for i in range(digits):
            if x % (i + 1) > 0:
                keeplooping = False
        if keeplooping:
            winner = x
            done = True
        else:
            x += 1
    return winner



if __name__ == "__main__":
    size = int(sys.argv[1])
    if size is None:
        size = 99
    print(size, FindSmallest(size))
