
def make_divison_by(divisor: int) -> int:
    assert type(divisor) == int or type(divisor) == float, "Solo se pueden números"
    assert divisor != 0, "You can't divide by zero"
    
    def division(numerator: int) -> int:
        assert type(numerator) == int or type(numerator) == float, "Solo se pueden números"
        return numerator / divisor
    
    return division

# def make_repeater_of(times: int) -> str:
#     def repeater(word: str):
#         assert type(word) == str, "Solo se puede texto"
#         return word * times

#     return repeater
