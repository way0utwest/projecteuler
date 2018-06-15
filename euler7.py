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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        param1 = int(sys.argv[1])
    else:
        param1 = 10
    start = time.time()
    print("Parameter:", param1)
    print("Answer:", Solution(param1))
    end = time.time()
    print("Elapsed:", end - start)


'''
Module Module1
  Sub Main()
    Dim beganAt As Date = Now
    Dim n = 10001
    Dim prime As Integer = 0
    Dim counter As Integer = 0
 
    ' Check each number until you've got 10001 prime numbers.
    Do Until prime = n + 1
      counter = counter + 1
      If isPrime(counter) Then
        prime = prime + 1
      End If
    Loop
 
    Dim endAt As Global.System.TimeSpan = Now.Subtract(beganAt)
    Dim took As Integer = endAt.Milliseconds
 
    Console.WriteLine(counter.ToString + " in " + took.ToString + "ms.")
    Console.ReadKey()
  End Sub
 
  Private Function isPrime(ByVal thisNumber As Integer) As Boolean
    ' Prime numbers other than two are odd...
    If thisNumber = 2 Then
      Return True
    ElseIf thisNumber Mod 2 = 0 Then
      Return False
    End If
 
    'Check it isn't divisible by up to its square root
    '(consider n=(root n)(root n) as factors)
    For counter As Integer = 3 To (Math.Sqrt(thisNumber)) Step 2
      If thisNumber Mod counter = 0 Then
        Return False
      End If
    Next
    Return True
  End Function
 
End Module
'''