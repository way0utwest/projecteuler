import sys
def GetFactors(bignumber):
    factors = []
    potentialfactor = 2
    while potentialfactor < (bignumber / 2):
        largefactor = bignumber // potentialfactor
        if bignumber % potentialfactor == 0:
            if IsPrime(largefactor):
                if (largefactor) not in factors:
                    factors.append(largefactor)
                    return factors
        potentialfactor += 1
    return factors


def IsPrime(number):
    if number <= 3:
        return True
    if (number % 2 == 0) or (number % 3 == 0):
        return False
    i = 5
    while(i * i < number):
        if number%i == 0 or (number%(i+2) == 0):
                return False
        i = i + 6
    return True



if __name__ == "__main__":
    para = int(sys.argv[1])
    print(para, GetFactors(para))
    #for i in range(25):
    #    print(i, IsPrime(i))
