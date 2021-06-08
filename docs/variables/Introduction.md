# What is a Variable?
In programming, a variable is a storage location (identified by a memory address) paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value or in easy terms, a variable is a container for different types of data (like integer, float, String and etc...). The variable name is the usual way to reference the stored value, in addition to referring to the variable itself, depending on the context. This separation of name and content allows the name to be used independently of the exact information it represents. The identifier in computer source code can be bound to a value during run time, and the value of the variable may thus change during the course of program execution.

# Dynamically Typed vs Statically Typed Languages

Python is a dynamically typed programing language, Which means you don't have to define the type of the variable, variable can be created and assigned and the same time.

In case of a statically typed languages like golang, Java and many others. You need to define the type of the variable before assigning data to it.

# Naming Convention Standards
Variables is a pretty simple topic to understand but a proper naming convention and correct usage of variables make us a better programmer.

# Some standard naming styles in Python:
**single letter** - The lower the scope of variable, lower its size of letters.

For example, its better to name a variable with single letter when its scope is limited to a loop function.
```python
for n in range(100)
```

is better than
```python
for number in range(100)
```

**lowercase** over **UPPERCASE**
Declaring variables in lowercase is always a better approach.
```python
name = "Abhishek Veeramalla"
```

is better than
```python
NAME = "Abhishek Veeramalla"
```

**underscores** - Declaring a variable name with underscore sometimes helps you describe a variable better. However, this will increase the variable size in terms of number of characters, So I will recommend this only when the variable has a great significance and used many times in the code.

**CamelCasing** - Usage is pretty much similar to underscore. It is mostly the choice of the programmer to choice one between underscore and camelCasing.

There are many other appected ways of declaring variables in Python but above examples are most generally used conventions.

# General guidelines on how to name your identifiers:
* **Module**	-> lowercase
* **Class** ->	CapWords
* **Functions** ->	lowercase
* **Methods**	-> lowercase
* **Constants** ->	UPPERCASE
* **Package**	-> lowercase

Avoid the usage of 'l', 'O' or 'I' as a single variable name: these characters look similar to zero (0) and (1) in some fonts.
