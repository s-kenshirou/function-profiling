# performance-tuning

This library is for profiling your python function.

Cannable thing is same as cPfoile, but you can get pandas Dataframe object of the profiling information.


Usage
-----

>>> def test(a, b):
...     return a + b
>>>
>>> import function_profiling
>>> result = function_profiling.profile(test, a=10, b=5)
