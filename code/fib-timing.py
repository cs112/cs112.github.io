
fibResult = dict()

def fib(n):
    if(n in fibResult):
        return fibResult[n]
    if (n < 2):
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    fibResult[n] = result
    return result

import time
def testFib(maxN=10000):
    for n in range(maxN+1):
        start = time.time()
        fibOfN = fib(n)
        ms = 1000*(time.time() - start)
        print("fib(%2d) = %8d, time =%5dms" % (n, fibOfN, ms))

testFib()