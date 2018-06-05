import sys
import time


def Solution(digits):
    winner, x = 0, 1000
    while (winner == 0):
        for i in (range(1, (digits + 1))):
            #print(x, i, (x%i))
            if (x % i) > 0:
                break
            else:
                if (i == digits):
                    winner = x
        if (winner == 0):
            x += 1
        #print(x, digits, winner)
    return winner


if __name__ == "__main__":
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 10
    start = time.time()
    print(size, Solution(size))
    end = time.time()
    print("Elapsed:", end - start)