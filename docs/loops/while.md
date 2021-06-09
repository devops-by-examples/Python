# While loop

Use while loop to execute a set of statements as long as a condition is true.

```python
n = 0
while n < 10:
  print(n)
  n += 1
```

In the above program, number of iterations depends on the value of `n`. This is an example of why `while` loop is considered as condition based loop.

## Break

A `break` statement can be used to control the loop iterations. In a nutshell, `break` breaks the loop execution when a condition is matched.

```python
n = 0
while n < 6:
  print(n)
  if n == 3:
    break
  n += 1
```

## Continue

A `continue` statement can be used to skip an Iteration of a loop. In a nutshell, `continue` skips the current iteration and moves to the next iteration.

Example: Print numbers less than 10 but skip 5.

```python
n = 0
while n < 6:
  n += 1
  if n == 5:
    continue
  print(n)
```

