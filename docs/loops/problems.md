# Problems

## Question 1

Write a function to print all letters in a string except `a` and `b`.

Solution

```python
for item in 'abhishekveeramalla':
    if letter == 'a' or letter == 'b':
        continue
    print(item)
```

## Question 2

Write a python program to print the below pattern. While it might look silly at the very first place but for a beginer such creative problems are very useful.

```txt
* 
* * 
* * * 
* * * * 
* * * * * 
```

Solution

```python
from __future__ import print_function
def pyramid(n):
    # number of rows
    for x in range(n):
        # number of columns
        for y in range(x+1):
            print("* ", end='')

        # new line
        print("\r")
 

if __name__ == '__main__':
    n = 5
    pyramid(n)
```

## Try by yourself

Write a python function to print the below pattern.

```txt
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

Solution

```python
from __future__ import print_function
def pyramid(n):

    num = 1
    # number of rows
    for x in range(n):
        num = 1
        # number of columns
        for y in range(x+1):
            print(num, end=" ")
            # increament
            num = num + 1

        # new line
        print("\r")
 
# Driver code
n = 5
pyramid(n)
```

## Knowledge Test

By now, you have learnt about loops and how they are used in Python. Solve the below problem to access your expertise on loops.

## Question 4

Print the below patten

```txt
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
```

## Question 5

Read a number `n` as input from users.  

Example: `n = 3`

The list of non-negative integers that are less than `n = 3`  is `0, 1, 2`. Print the square of each number on a separate line.

Sample Output:

```txt
0 
1
4
```

## Question 6

Read a number `n` as input from users.  

Example: `n = 100`

Write a program for the below.

1. Print Odd numbers and Even numbers between `0` and `n`
2. Print ONLY numbers which are divisible by `3` OR divisible by `5`. DO NOT print numbers which are divisible by both `3` and `5`.
