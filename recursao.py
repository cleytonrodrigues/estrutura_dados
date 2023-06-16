import time

n = 40

def fibonacci_iterative(n):
    if n <= 0:
        return "O valor de n deve ser maior que zero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev_1 = 0
        prev_2 = 1
        fib = 0
        for _ in range(2, n):
            fib = prev_1 + prev_2
            prev_1, prev_2 = prev_2, fib
        return fib

def fibonacci_recursive(n):
    if n <= 0:
        return "O valor de n deve ser maior que zero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Abordagem Iterativa
start_time = time.time()
fib_iterative = fibonacci_iterative(n)
end_time = time.time()
iterative_time = end_time - start_time

# Abordagem Recursiva
start_time = time.time()
fib_recursive = fibonacci_recursive(n)
end_time = time.time()
recursive_time = end_time - start_time

print("Abordagem Iterativa:")
print("Valor do 40º número da sequência de Fibonacci:", fib_iterative)
print("Tempo de execução:", iterative_time, "segundos")
print()
print("Abordagem Recursiva:")
print("Valor do 40º número da sequência de Fibonacci:", fib_recursive)
print("Tempo de execução:", recursive_time, "segundos")