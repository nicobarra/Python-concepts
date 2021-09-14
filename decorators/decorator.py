from datetime import datetime

def execution_time(func) -> int: #Calculates the time that takes to the function to execute
    def wrapper(*args, **kwargs): # args: arguments || Keyword args: Arguments defined in the parameter. Ej: func(name='Nico')
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"* {time_elapsed} seconds took the function to execute.")
    return wrapper

def format_upper(func) -> str: # It works as an upper decorator for text
    def wrapper(*args, **kwargs) -> str:
        func(*args, **kwargs)
        return f"{func(*args, **kwargs).upper()}"
    return wrapper

def format_lower(func) -> str:
    def wrapper(*args, **kwargs) -> str:
        func(*args, **kwargs)
        return f"{func(*args, **kwargs).lower()}"
    return wrapper

@format_upper
def upper_text(text: str) -> str: # It only has an assert and returns the text
    assert type(text) == str, "It only accepts text"
    return f"* {text}"

@format_lower
def lower_text(text: str) -> str: # It only has an assert and returns the text
    assert type(text) == str, "It only accepts text"
    return f"* {text}"
