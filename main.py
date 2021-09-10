from closures.closure import make_divison_by
from decorators.decorator import upper_text, execution_time
from iterators.iterators import FiboIter, FiboNumber
from generatorss.generator import fibo_gen_counter_limit, fibonacci_gen
from sets.sets import remove_duplicates_with_for, set_remove_duplicates

def divisor(): ## Closure
    divisor = 5
    division_by = make_divison_by(divisor)
    numerator = 100
    return f"The result of diving {numerator} by {divisor} is:  {division_by(numerator)}"

def transform_text(): ## Decorator
    new_text = upper_text("before applying the decorator on the function, this text was lower.")
    return new_text
class FibonacciIterator:

    def fibonacci_iterator_limit(): 
        fibonacci = FiboIter(6)
        print("Fibonacci iterator: \n*  n°: fibonacci number")
        iterator_counter = 0
        for element in fibonacci:
            print(f"*   {iterator_counter}: {element}")
            iterator_counter += 1

    def fibonacci_number_limit(): 
        fibonacci_number = 21
        fibonacci_number_limit = FiboNumber(21)
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        time_of_iteration = 0
        for element in fibonacci_number_limit:
            print(f"*    {time_of_iteration}: {element}")
            time_of_iteration += 1
        

class FibonacciGenerator:

    def fibonacci_number_limit(): 
        fibonacci_number = 21
        fibonacci_number_limit = fibonacci_gen(fibonacci_number)
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        time_of_iteration = 0
        for element in fibonacci_number_limit:
            print(f"*    {time_of_iteration}: {element}")
            time_of_iteration += 1

    def fibonacci_iterator_limit():
        iteration = 8
        fibonacci_counter_limit = fibo_gen_counter_limit(iteration)
        iteration_time = 0
        for element in fibonacci_counter_limit:
            print(f"*    {iteration_time}: {element}")
            iteration_time += 1

def unique_element():
    # Function for removing duplicates with a list, a for loop and an if:
    clean_list = remove_duplicates_with_for([1, 2, 2, 3, 3, 4, 5, 6, 6])
    print(f"Unique list created with a for loop: {clean_list}")

def set_unique_element():
    # Function for removing duplicates by only using set():
    set_list = set_remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 6, 6])
    print(f"Unique list created with a set(): {set_list} --> (Is more efficient)")

@execution_time # Returns how much times it takes to run() to execute
def run():
    ## Closure:
    print("-- "*19 +"\n# CLOSURES FUNCTION:")
    print(divisor())

    ## Decorator:
    print("-- "*19 +"\n# DECORATORS FUNCTION:")
    print(transform_text())

    ## Iterators: In this case Fibonacci with iteration limit
    print("-- "*19 +"\n# ITERATORS FUNCTION")
    FibonacciIterator.fibonacci_iterator_limit()

    ## Generators: Sugar syntax iterators. In this case of FiboIter
    print("-- "*19 +"\n# GENERATORS FUNCTION:")
    # Fibonacci with a fibonacci number as a limit:
    FibonacciGenerator.fibonacci_number_limit()
    print("* "*19)
    # Fibonacci with an iteration of the fibonacci series as a limit:
    print("Limit method by Fibonacci iteration: \n*   n°: fibonacci number")
    FibonacciGenerator.fibonacci_iterator_limit()

    ## Sets
    print("-- "*25 +"\n# SETS FUNCTION:")
    unique_element()
    set_unique_element()

    ## Decorator '@execution_time' output:
    print("-- "*25 +"\n# OUTPUT FROM THE DECORATOR 'EXECUTION_TIME':")

if __name__=='__main__':
    run()
