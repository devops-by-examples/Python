# Bitwise Operators

Bitwise operators are used to perform bitwise operations on binary patterns.

Python supports below Bitwise operators.

* Bitwise AND
* Bitwise OR
* Bitwise NOT
* Bitwise XOR
* Bitwise right shift
* Bitwise left shift

```python
a = 11
b = 2

print(a & b)
print(a | b)
```

## Output

```txt
2
11
```

### Lets do a step by step break down of the output

a = 11 -> Bitwise representation -> 00001011

b = 2  -> Bitwise representation -> 00000010

`a & b` performs AND operation on each bit. Performing AND on each bit will return `00000010`

`a | b` performs OR operation on each bit. Performing OR on each bit will return `00001011`

## Try by yourself

a = 12, b = 4

Write a program to return the output of `a & b` and understand how the output is generated.
