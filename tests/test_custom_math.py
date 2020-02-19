from mathlib.math import CustomMath

def test_sum_two_arguments():
    first = 2
    second = 11
    custom_math = CustomMath()
    result = custom_math.sum(first,second)
    assert result == (first+second)



