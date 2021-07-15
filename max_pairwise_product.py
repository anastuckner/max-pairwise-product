import random


def MaxPPFast(n, a):
   
   
    #To input the sequence manually:
      
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # assert(len(a) == n)
       
    result1 = 0
   
    a.sort()

   
    result1=a[n-1]*a[n-2]
    return result1

def MaxPPNaive(n, a):
   
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # assert(len(a) == n)
   
    result2 = 0
   
    for i in range(n):
        for j in range(i+1, n):
            
            if a[i]*a[j] > result2:
                result2 = a[i]*a[j]
            
   
    return result2


def StressTest(n, m):
  while True:
   
    n = random.randint(2,n)
   
    a = [None]*n
   
    for i in range(n):
       a[i] = random.randint(0,m)

    
    result1 = MaxPPNaive(n, a)
    result2 = MaxPPFast(n, a)
   
    if result1==result2:
       
          print('OK')
   
    else:
       
        print('Wrong answer:',result1,result2)
        return 
      
StressTest(500, 5000)
