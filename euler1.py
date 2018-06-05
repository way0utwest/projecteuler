def euler1(limit):
    x = range(1,limit)
    sum = 0
    for i in x:
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
            print(i)
    return (sum)


if __name__ == "__main__":
    y = euler1(1000)
    print("Sum: ", y)
