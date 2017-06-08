# More big-O practice! 
def bigOh0(L): 
    N = len(L)
    for x in range(0, N**2): 
        print("Why is Subra leaving us?")

def bigOh1(L): 
    N = len(L)
    for x in range(0, N**2, 2):
        print("I am Batman")


def bigOh2(L): 
    N = len(L)
    for x in range(0, N**2, N/2): 
        print("Subra is the hero we deserve, but not the one we need right now")

def bigOh3(L): 
    N = len(L)
    x = y = 0
    while (x < N):
        while (y < N):
            print("y", end = " ")
            y += 3
        print("x", end = " ")
        x += 4

def bigOh4(L): 
    L = L * len(L)
    return sorted(L)

def bigOh5(L): 
    N = len(L)
    M1 = [L[i]**2 for i in range(1, len(L), 3)] 
    M2 = [L[i]**3 for i in range(1, 3)]
    M3 = sorted([x*y for x in L for y in L]) 
    return sorted(M1 + M2 + M3) 

def bigOh6(n): 
    #assume n is an integer
    L = range(112, int(math.log(n, 2)))
    for c in str(n):
        L[0] += 5
        L.sort() 
    return L

