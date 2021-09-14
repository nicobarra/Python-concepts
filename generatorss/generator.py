def fibo_gen_number_limit(max_number:int) -> int:
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
class FibonacciGenerator:
    def fibonacci_number_limit(limit): 
        fibonacci_number_limit = fibo_gen_number_limit(limit)
        time_of_iteration = 0
        for element in fibonacci_number_limit:
            print(f"*    {time_of_iteration}: {element}")
            time_of_iteration += 1

    def fibonacci_iteration_limit(limit):
        fibonacci_counter_limit = fibo_gen_counter_limit(limit)
        iteration_time = 0
        for element in fibonacci_counter_limit:
            print(f"*    {iteration_time}: {element}")
            iteration_time += 1