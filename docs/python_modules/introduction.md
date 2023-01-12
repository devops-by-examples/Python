## Python Modules

Modularization is the technique of splitting a large programming task into smaller, separate and manageable subtasks. Python is a modular programming language like most modern programming languages. Functions, modules, and packages in Python promote modularity. In this writing, we will discuss Python modules and packages in detail.


### Python Modules

Every Python file is a module. If you create a file with .py extension that has some actual Python code in it, you’ve created a Python module.

For example, suppose you want to create a simple calculator. The calculator will have four functionalities: summation, subtraction, multiplication, and division. You can create a Python file called ```calculator.py```. This file will have four functions: ```sum()```, ```subtract()```, ```multiply()```, ```divide()```.


```
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

```
You’ve created a module called ```calculator```.
