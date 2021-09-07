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