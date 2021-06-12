# Identity Operators

Identity Operators are used to verify if both the operators are identical. Which means, both the variables are located on the same part of memory.

```python
x = 5
y = 3
z = 5

a = ["Abhishek", "Veeramalla"]
b = ["Abhishek", "Veeramalla"]

print(x is z)
print(x is not y)
print(a is b)
```

Output:

```txt
True
True
False
```
