# Problems

## Question 1

Complete the 'fullName' function below. The function is expected to return below STRING.

Hello Abhishek Veeramalla! Happy Learning Python

The function accepts following parameters:

1. First Name
2. Last Name

```python
def fullName(first, last):
    print("Hello " + first + " " + last + "! Happy Learning Python")

if __name__ == '__main__':
    print("Please enter First Name")
    first = input()
    print("Please enter Last Name")
    last = input()
    fullName(first, last)
```

## Question 2

Write a program to switch the case of each letter in a string.

Example Input:

Iam ABHIsheK VEERamaLlA

Output:

iAM abhiSHEk veerAMAlLa

```python
def switchCase(a):
    return a.swapcase()

if __name__ == '__main__':
    print("Please enter a string")
    a = input()
    result = switchCase(a)
    print(result)
```

## Question 3

Write a function that returns the first 2 and the last 2 chars from a given string. If the length of string is less than 2 it should return an empty string.

```python
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]


if __name__ == '__main__':
    print(string_both_ends('Abhishek'))
    print(string_both_ends('Veeramalla'))
    print(string_both_ends('a'))
    
main()
```
