import math

# m=n
#
# m*n
#
# m>n
#
# (m)!/(m-n)! + sum((n-1)!/(n-1-i)!i!)i=(m-n)->(m) 
#
# 		hacer lo mismo con lo que sobra disminuyendo de a 1,
# 		ver cuantos hace y eso permutarlo con las posiciones 			
# 		faltantes

def permutationCounter(m,n):
    return math.factorial(m)/math.factorial(m-n)

def combinationCounter(m,n):
    return math.factorial(m)/(math.factorial(n)*math.factorial(m-n))

def layoutCounter(m, n):
    if m==n:
        return 1

    if m<n:
        permutationCounter(m,n)

    count = 0

    count += permutationCounter(m,n)

    for i in range(m-n,m):
        counter += combinationCounter(n-1,i)
        counter += layoutCounter(m-i,n-1)

    return count


n=26
m=2

print(layoutCounter(m,n))
