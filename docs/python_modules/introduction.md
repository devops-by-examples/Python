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

### import ```module_name```
You can use a module by importing it. Create another Python file called main.py in the same location as calculator.py. All the functions inside calculator.py can be accessed from main.py by importing it.


```
import calculator

print(calculator.sum(5, 10))
print(calculator.subtract(5, 10))
print(calculator.multiply(5, 10))
print(calculator.divide(5, 10))

```
Now if you run main.py you will see the appropriate outputs:

```
15
-5
50
0.5

```
### import ```module_name``` as ```shortened_name```

There is a way to use a short form of the module name calculator. You can associate a suitable smaller name for a module when importing it.

```
import calculator as cal

print(cal.sum(5, 10))
print(cal.subtract(5, 10))
print(cal.multiply(5, 10))
print(cal.divide(5, 10))

```

You can find many examples of renaming the name of a module. People always use ```import numpy as np``` and ```import pandas as pd```.

### from ```module_name``` import ```some_object(s)```
Maybe you don’t want to import all the functions from the calculator module. You can specify what you want to import from a module. Let’s import just the ```sum()``` and ```subtract()``` functions from ```calculator.py```.

```
from calculator import sum, subtract

print(sum(5, 10))
print(subtract(5, 10))

```

Now you can write the function names directly without having to write ```calculator.sum()``` and ```calculator.subtract()```.

### from <module_name> import *

```

from calculator import *

print(sum(5, 10))
print(subtract(5, 10))
print(multiply(5, 10))
print(divide(5, 10))

```

### Path of a Module

When you import a module in a script and run it, the Python interpreter first searches the current directory from where the script is being run. The calculator.py and main.py files are in the same directory. The import works only because calculator.py is in the same directory as main.py.

But this is not the only way to import a module. We can import modules from another directory too. Even we often import modules from the standard library, and also from third parties.

When the interpreter executes an import statement, it searches the module in a list of directories:

- The same directory from where the script was run.
- The list of directories in the PYTHONPATH environment variable. You need to manually set the environment variable.
- The list of installation-dependent directories that were configured when Python was installed on your computer. (The modules from Python’s standard library and also the third-party modules that you install.)

You can access the path list using the variable ```sys.path``` which comes from the module ```sys```.

Import the ```sys``` module in your ```main.py``` and print the ```sys.path``` variable.

```
import sys
print(sys.path)

```

It will print a ```list``` containing all the paths.

### Import a Module From a Different Directory

If you want to import a module that is in a different directory from your script, you need to add the path to the environment variable PYTHONPATH. Again depending on which OS you are using, the process of adding a path to the environment variable will be different.

To make things simple, you can just add the path of your module to the ```sys.path``` variable.

Put the ```calculator.py``` file in a different directory than the ```main.py``` file. Then add the path of ```calculator.py``` to ```sys.path```.


Add the path of your module in ```sys.path``` like this:

```

import sys
sys.path.append('/home/shadhin/dev/modules_and_packages/calc_dir')
print(sys.path)

```
You will see the path as you print ```sys.path```.

Now you can import the ```calculator.py``` module from a different directory like before.

After importing a module you can find its location by using the ```__file__``` attribute.


```
import sys
sys.path.append(##fullpath)
# print(sys.path)

import calculator
print(calculator.__file__)
`
```

Output:

You will see the location accordingly.


### The Standard Library

Python has a rich collection of pre-implemented modules. They are in the Standard Library.

Using the __file__ attribute you can also determine their location.

```
>>> import os
>>> os.__file__
‘/usr/lib/python3.9/os.py’
```


From above you can see I imported the os module. os.__file__ shows me the location of the module. Let’s navigate to that exact location and see what’s happening.

There are a lot of ```.py``` files. All of them came with my Python installation and they are part of the Python standard library.

You can go to the location of your computer and check these Python files. You will be amazed to see that they all contain actual Python codes and many of them you can actually understand!

### Modules Are Also Executable Python Scripts
Python modules are nothing but Python files. So nothing is preventing you to run a module as a Python script.

You can run the ```calculator.py``` file like this:

```
$ python calculator.py

```

Of course, it will not do anything as it has nothing to show as an output. Let’s add some code to it and run it again.

```

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("I am a module, but I can run as an individual script too!")
print(sum(5, 10))

```


Output:

```

I am a module, but I can run as an individual script too!
15

```
There is a variable called __name__. When a Python file is imported as a module, Python sets __name__ to the name of the module. But if a Python file is executed as a script then __name__ is set to ‘__main__’. This is why you will see a conditional statement in many Python programs:

```
if __name__ == ‘__main__’:
    some code...

```

Use this condition in your calculator.py file and put the last two lines inside it.

```

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__':
    print("I am a module, but I can run as a individual script too!")
    print(sum(5, 10))

```

Now run the main.py file and you will see the output of calculator.py file is no longer showing.

By using the if __name__ == ‘__main__’ conditional, you are specifying that this part of the code will execute only when the file is run as a single script. Because __name__ == ‘__main__’ is only true when the file is treated as a standalone script.


A Python package is nothing but a folder containing some modules inside it. To initialize a folder as a Python package we need to create a file called ```__init__.py``` inside the folder.

For example, you can separate all the functions in your ```calculator.py``` module and put them into four different modules:

```
def sum(a, b):
    return a + b
```

```
def subtract(a, b):
    return a - b
```

```
def multiply(a, b):
    return a * b
```

```
def divide(a, b):
    return a / b
```

Now put them in a single folder called ```calc_pkg``` and create a file called ```__init__.py``` inside the folder. You just created a Python package called ```calc_pkg```.


### import <package_name.module_name>

```
import calc_pkg.sum, calc_pkg.subtract, calc_pkg.multiply, calc_pkg.divide

print(calc_pkg.sum.sum(5, 10))
print(calc_pkg.subtract.subtract(5, 10))
print(calc_pkg.multiply.multiply(5, 10))
print(calc_pkg.divide.divide(5, 10))

```

***Output:***

```
15
-5
50
0.5

```


