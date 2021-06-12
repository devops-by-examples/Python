# Logical Operators

`and`, `or` and `not` are the Logical Operators supported by Python.

**and** - returns True only if both the operands are True.

**or** - returns True if one of the operands is True.

**not** - returns False if the operand is True and returns True if the operand is False.

Below program implements all the different types of Logical Operations one can use in Python.

```python
x = 5
y = 3
  
# Logical AND
print(x > y and x == 5)
  
# Logical OR
print(x > y or x == 5)
print(x > y or x == 3)
  
# Logical NOT
print(not x > y)
print(not x < y)
```

Output:

```txt
True
True
True
False
True
```
