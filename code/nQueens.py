def isLegal(row, constraints):
    for ccol in range(len(constraints)):
        crow = constraints[ccol]
        shift = (len(constraints))-ccol
        if ((row == crow) or
            (row == crow + shift) or
            (row == crow - shift)):
            return False
    return True 

def solve(n, m, constraints):
    if(m == 0):
        return []       
    for row in range(n):
        if (isLegal(row, constraints)):         
            newConstraints = constraints + [row]            
            result = solve(n, m-1, newConstraints)
            if (result != False):
                return [row] + result
    return False

def make2dSolution(queenRow):
    n = len(queenRow)
    solution = [(["- "] * n) for row in range(n)]
    for col in range(n):
        row = queenRow[col]
        solution[row][col] = "Q "
    return "\n".join(["".join(row) for row in solution])

def queen(n):
    result = solve(n,n,[])
    if (result != False):
        print(make2dSolution(result))
    else:
        print("No solution exists.")

#print(make2dSolution(solve(4,4,[])))