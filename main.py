from closures.closure import make_divison_by
from decorators.decorator import upper_text, lower_text, execution_time
from iterators.iterators import FibonacciIterator
from generatorss.generator import FibonacciGenerator

def division(numerator, denominator): ## Closure
    division_by = make_divison_by(denominator)
    return f"The result of diving {numerator} by {denominator} is:  {division_by(numerator)}"

def transform_text(text, transform_option): ## Decorator
    assert type(text) == str, "You only can only enter string"
    assert type(transform_option) == int, "You only can only enter a number"
    assert transform_option == 1 or transform_option == 2, "The number must be one of the option: 1 or 2"
    if transform_option == 1:
        return lower_text(text)
    elif transform_option == 2:
        return upper_text(text)

def fibonacci_iterator(option): ## Iterator
    assert type(option) == int, "You can only insert a number for choosing the option"
    assert option == 1 or option == 2 or option == 3, "You can only insert a number of the mentioned options"
    
    if option == 1:
        iteration_limit = int(input("Set the iteration time limit: ")) 
        assert type(iteration_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciIterator.fibonacci_iterator_limit(iteration_limit)

    elif option == 2:
        number_limit = int(input("Set the Fibonacci number limit: ")) 
        assert type(number_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciIterator.fibonacci_number_limit(number_limit)

    elif option == 3:
        iteration_limit = int(input("Set the iteration limit: ")) 
        assert type(iteration_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciIterator.fibonacci_iterator_limit(iteration_limit)
        number_limit = int(input("Set the Fibonacci number limit: ")) 
        assert type(number_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciIterator.fibonacci_number_limit(number_limit)

def fibonacci_generator(option): ## Generator
    assert type(option) == int, "You can only insert a number for choosing the option"
    assert option == 1 or option == 2 or option == 3, "You can only insert a number of the mentioned options"
    
    if option == 1:
        iteration_limit = int(input("Set the iteration time limit: ")) 
        assert type(iteration_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciGenerator.fibonacci_iteration_limit(iteration_limit)

    elif option == 2:
        number_limit = int(input("Set the Fibonacci number limit: ")) 
        assert type(number_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciGenerator.fibonacci_number_limit(number_limit)

    elif option == 3:
        iteration_limit = int(input("Set the iteration limit: ")) 
        assert type(iteration_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciGenerator.fibonacci_iteration_limit(iteration_limit)
        number_limit = int(input("Set the Fibonacci number limit: ")) 
        assert type(number_limit) == int, "You only can set an integer as the limit"
        print("Limit method by Fibonacci number: \n*   n°: fibonacci number")
        FibonacciGenerator.fibonacci_number_limit(number_limit)

def set_unique_element(elements_text): ## Set
    elements_text = elements_text.replace(",","")
    list = elements_text.split(" ")
    set_list = set(list) # Function for removing duplicates by only using set():
    return f"Unique list created with a set(): {set_list} --> (set() is efficient)"


@execution_time # Returns how much times it takes to run() to execute
def run():
    ## Closure:
    print("-- "*19 +"\n# CLOSURES: \n This is a division function")
    numerator = float(input("Set the numerator you want: "))
    denominator = float(input("Set the denominator you want: "))
    print(division(numerator, denominator))

    ## Decorator:
    print("-- "*19 +"\n# DECORATORS FUNCTION:")
    text = input("Write the text that the function will transform: \n")
    transform_option = int(input("Choose how you want to transform the previous text:\
        \n 1. Lower text \
        \n 2. Upper text \
    \n Enter the number of the option you want: "))
    print(transform_text(text, transform_option))

    ## Iterators: 
    print("-- "*19 +"\n# ITERATORS FUNCTION")
    print("The Fibonacci function created with an iterator")
    option_fibonacci_iterator = int(input("Choose the option you want in order to set the limit of the Fibonacci iterator function: \n \
        1. Set the limit by the time of the iteration \n \
        2. Set the limit by the number of fibonacci \n \
        3. I want to try both options \n \
Enter the number of the option you want: "))
    fibonacci_iterator(option_fibonacci_iterator)     

    ## Generators: (Sugar syntax iterators.)
    print("-- "*19 +"\n# GENERATORS FUNCTION:")
    print("The same Fibonacci function, but in this case created with a generator")
    option_fibonacci_generator = int(input("Choose the option you want in order to set the limit of the Fibonacci generator function: \n \
        1. Set the limit by the time of the iteration \n \
        2. Set the limit by the number of fibonacci \n \
        3. I want to try both options \n \
Enter the number of the option you want: "))
    fibonacci_generator(option_fibonacci_generator)  

    ## Sets
    print("-- "*25 +"\n# SETS FUNCTION:")
    element_text = input("Enter a text separating with an space each element that you want to be added. \n \
 The set() function will delete the ',' and will only return only an unique element of this text. \n \
  For example: 'I am good today, how are you today ?' \n \
Enter your text with your elements: ")
    print(set_unique_element(element_text))

    ## Decorator '@execution_time' output:
    print("-- "*25 +"\n# OUTPUT FROM THE DECORATOR 'EXECUTION_TIME':")

if __name__=='__main__':
    run()
