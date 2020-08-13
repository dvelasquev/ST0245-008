import time
n = int(input("Factorial a calcular: "))

def factorial_recursivo(n):
    if n==0:
        return 1
    else:
        return n*factorial_recursivo(n-1)

def factorial_iterativo(*n):
    if n == 0:
        return 1
    else:
        for x in n:
            a = 1
        for y in range(1,x+1):
            a = a*y
        return a

start_time = time.time()
factorial_recursivo(n)
print("Recursion--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
factorial_iterativo(n)
print("Iteration--- %s seconds ---" % (time.time() - start_time))