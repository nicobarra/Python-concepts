from sets.sets import remove_duplicates_with_for
from closures.closure import make_divison_by
from decorators.decorator import format_upper, execution_time
from generatorss.generator import fibo_gen_counter_limit, fibonacci_gen
from iterators.iterators import FiboIter
from sets.sets import remove_duplicates_with_for, set_remove_duplicates


def run():
    by5 = make_divison_by(5)
    print(remove_duplicates_with_for([1, 1, 1, 2, 2]), by5(100))

if __name__=='__main__':
    run()