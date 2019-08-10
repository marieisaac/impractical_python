```python
import math
def a(vector):
    squaredSum = 0
    for coordinate in vector:
        squaredSum += math.pow(coordinate, 2)
    return math.sqrt(squaredSum)
```

1. Explain what this function does in plain english.

2. What would you rename the function `a` so it is clearer what it does?

3. Assuming the argument `vector` is `[1, 2, 3, 4]` write the values that `squaredSum` stores in it over the course of the function.

4. How would you call the function as described above and print the result.

5. Why is it possible to run the following line of code `squaredSum += math.pow(coordinate, 2)` (ie what does it do)?

6. Let's say there is a python file called `mymath.py` which declares a function called `add`.
   This function takes 2 numbers as arguments and returns the sum of them.
   Import, call, and print the result of this function.

7. Now write the file `mymath.py` as described above.

8. What are the essential command for committing code for storing new code on an external git server?

9. How do you make a new branch and why?
