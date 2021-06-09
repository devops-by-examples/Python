# What is a Data Type?

In programming, a data type or simply type is an attribute of data which tells the compiler or interpreter how the programmer intends to use the data. Most programming languages support basic data types of integer numbers (of varying sizes), floating-point numbers (which approximate real numbers), characters and Booleans. A data type constrains the values that an expression, such as a variable or a function, might take. This data type defines the operations that can be done on the data, the meaning of the data, and the way values of that type can be stored. A data type provides a set of values from which an expression (i.e. variable, function, etc.) may take its values.

## Data Types in Python

Python has the following data types built-in by default, in these categories:

*Text Type*: str

*Numeric Types*: int, float, complex

*Sequence Types*: list, tuple, range

*Mapping Type*: dict

*Set Types*: set, frozenset

*Boolean Type*: bool

*Binary Types*: bytes, bytearray, memoryview

## How to find the Type of a Data ?

You can get the type using the type() function.

```python
name = "Abhishek Veeramalla"
type(name)
```

## Dynamically Typed vs Statically Typed Languages

Python is a dynamically typed programing language, Which means you don't have to define the type of the variable, variable can be created and assigned and the same time.

In case of a statically typed languages like golang, Java and many others. You need to define the type of the variable before assigning data to it.

```python
x = 5
```

In the above example, x becomes an Integer Data Type.

```python
x = "Abhishek Veeramalla"
```

In the above example, x becomes a String Data Type.

```python
x = ["Abhishek", "Veeramalla"]
```

In the above example, x becomes a List Data Type.

## Overview of Data Types in Python

### String

* s = "Abhishek Veeramalla"

### Integer

* i = 100

### Float

* f = 16.9

### Complex

* c = 4j

### List

* l = ["Abhishek", "Veeramalla"]

### Tuple

* t = ("Abhishek", "Veeramalla")

### Range

* r = range(100)

### Dictionary

* d = {"name" : "Abhishek", "surname" : "Veeramalla"}

### Set

* s = {"Abhishek", "Divya", "Sandeep"}

## FrozenSet

* fs = frozenset({"Abhishek", "Divya", "Sandeep"})

### Bool

* b = True

## Constructor

You can also create a variable of a specific type using constructor function.

For example, you can create a variable of type string as shown below.

```python
name = str("Abhishek Veeramalla")
```
