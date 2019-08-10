```python
# import math
# def a(vector): #defining function called "a" with the argument vector
#     squaredSum = 0 #squaredsum is a variable with value 0
#     for coordinate in vector:
#         squaredSum = squaredSum + math.pow(coordinate, 2)
#     return math.sqrt(squaredSum)
#
# This function determines the distance of the vector from the origin

# [
#   [1,2,3],
#   [4,5,6]
# ]

def matrixSum(matrix):
  total = 0
  for row in matrix:
    for column in row:
      total = total + column
  return total

def sum(list): #defining function called "a" with the argument vector
    b = 0 #squaredsum is a variable with value 0
    for item in list:
        b = b + item
    return b

# a^b
def power(a, b): #defining function called "a" with the argument vector
    total = 1 #squaredsum is a variable with value 0
    for i in range(b):
        total = total * a
    return total
```

1. Explain what this function does in plain english

  This function sums all values in list

2. What would you rename the function `a` so it is clearer what it does?

√+

3. Assuming the argument `vector` is `[2, 4]` write the values that `squaredSum` stores in it over the course of the function.

√+

4. How would you call the function as described above and print the result.

```py
print(power(1, 2)) #1

print(sum([2, 3])) #5
```

5. Why is it possible to run the following line of code `squaredSum = squaredSum + math.pow(coordinate, 2)` (ie what does it do)?

6. Let's say there is a python file called `mymath.py` which declares a function called `add`.
   This function takes 2 numbers as arguments and returns the sum of them.
   Import, call, and print the result of this function.

```py
import add from mymath

print(add(5,3))  
```

7. Now write the file `mymath.py` as described above.
```py
def add(a,b):
  return a + b
```
8. What are the essential command for committing code for storing new code on an external git server?

git add --all
git commit -m "take quiz on functions and loops"
git push origin master

9. How do you make a new branch and why?

```sh
git branch new
git checkout new
```

So that we do not commit incomplete or incorrect code to the master branch
