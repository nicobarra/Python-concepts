from datetime import datetime

def execution_time(func) -> int: #Calculates the time that takes to the function to execute
    def wrapper(*args, **kwargs): # args: argumentos || Keyword args: Argumentos definidos en el parámetro. Ej ok(name='Nico')
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"* {time_elapsed} seconds took the function to execute.")
    return wrapper # wrapper = envoltura

def format_upper(func) -> str:
    def wrapper(*args, **kwargs) -> str:
        func(*args, **kwargs)
        return f"{func(*args, **kwargs).upper()}"
    return wrapper

@format_upper
def chat(text: str) -> str:
    assert type(text) == str, "It only accepts text"
    return f"* {text}"

@execution_time    
def run():
    print(chat("before applying the function, this text was lower."))

if __name__=="__main__":
    run()