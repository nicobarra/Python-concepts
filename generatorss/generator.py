from time import sleep

def fibonacci_gen(max_number:int) -> int:
    a, b = 0, 1
    while a <= max_number:
        yield a
        a, b = b, a+b

def fibo_gen_counter_limit(max_counter: int) -> int:
    n1, n2 = 0, 1
    counter = 0
    while counter <= max_counter:
        yield  n1
        n1, n2 = n2, n1+n2
        counter += 1

def run():
    fibonacci_number_limit = fibonacci_gen(21)
    print("Método límite por el número de Fibonacci: \n* time: fibonacci number")
    time = 0
    for element in fibonacci_number_limit:
        print(f"*    {time}: {element}")
        time += 1

    print("-- "*19)
    print("Método límite por el contador de sucesiones de Fibonacci: \n* time: fibonacci number")
    fibonacci_counter_limit = fibo_gen_counter_limit(8)
    time = 0
    for element in fibonacci_counter_limit:
        print(f"*    {time}: {element}")
        time += 1

if __name__ == "__main__":
    run()

