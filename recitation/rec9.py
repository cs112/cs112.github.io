def bigOh1(s): 
    charCount=""
    for c in s: #O(N)
        count=s.count(c) 
        if c in charCount: 
            continue
        else:
            charCount += "%s%d " % (c, count) 

def bigOh2(s): 
    myS = s * len(s) 
    result = ""
    for c in myS: 
        if c in result: 
           break
        else:
            result+=c 
    return result

def bigOh3(a): 
    for i in range(len(a)): 
        j=1
        while (j < len(a)):
            j*=2 
    print(a) 

def bigOh4(L): 
    # assume L is a 1d list
    N = len(L) 
    while (N > 0): 
        print(max(L[0:N])) 
        N //= 4

def bigOh5(L): 
    # assume L is a 1d list
    N = len(L)
    for i in range(N):
        for j in range(i, N):
            if (L[i] > L[j]):
                (L[i], L[j]) = (L[j], L[i])




