# Arithmetic Operators

Arithmetic Operators are the most commonly used mathematic operations such as `addition`, `subtraction`, `multiplication` and `division`.

Below program implements all the different types of Arithmetic Operations one can use in Python.

```python
def addition(x, y):
    print("Performing Addition")
    return x + y

def subtraction(x, y):
    print("Performing Subtraction")
    return x - y

def multiplication(x, y):
    print("Performing Multiplication")
    return x * y

def division(x, y):
    print("Performing Division")
    return x / y

def modulus(x, y):
    print("Performing Modulus")
    return x % y

def exponential(x, y):
    print("Performing Exponentiation")
    return x ** y

if __name__ == '__main__':

    # You can alternatively use input() to fetch values from user.
    a = 3
    b = 2

    # Addition
    add = addition(a, b)
    print(add)
    print("\n")

    # Subtraction
    sub = subtraction(a, b)
    print(sub)
    print("\n")

    # Multiplication
    mul = multiplication(a, b)
    print(mul)
    print("\n")

    # Division
    div = division(a, b)
    print(div)
    print("\n")

    # Modulus
    mod = modulus(a, b)
    print(mod)
    print("\n")

    # Exponential
    exp = exponential(a, b)
    print(exp)
    print("\n")
```

## Output

```txt
Performing Addition
5


Performing Subtraction
1


Performing Multiplication
6


Performing Division
1.5


Performing Modulus
1


Performing Exponentiation
9
```
