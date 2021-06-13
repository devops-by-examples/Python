# List Methods

Below are the in-built list methods supported by Python.

* `append()`
* `clear()`
* `copy()`
* `extend()`
* `insert()`
* `pop()`
* `remove()`
* `reverse()`
* `sort()`

We have looked into the `append` and `remove` functions in the Mutability section of Lists. Let's take a deeper look into the other in-built list functions.

```python
colors = ["red", "blue", "green"]
# Clear or empty a list.
print("\nEmpty a list")
colors.clear()
print(str(colors))

colors = ["red", "blue", "green"]
# Create a copy of a list.
print("\ncopy a list")
c = colors.copy()
print(str(c))

# Add a list to end of another list using extend().
print("\nAdd a list to another")
moreColors = ["white", "black"]
colors.extend(moreColors)
print(str(colors))

# Insert an element at a specific index.
print("\nInsert an element at a specific index")
colors.insert(0, "violet")
print(str(colors))

# Remove an element at a specific index using pop().
print("\nRemove an element at a specific index")
colors.pop(0)
print(str(colors))

# Reverse a list.
print("\nReverse list")
colors.reverse()
print(str(colors))

# Sort a list.
print("\nSort list")
colors.sort()
print(str(colors))
```

Output:

```txt
Empty a list
[]

copy a list
['red', 'blue', 'green']

Add a list to another
['red', 'blue', 'green', 'white', 'black']

Insert an element at a specific index
['violet', 'red', 'blue', 'green', 'white', 'black']

Remove an element at a specific index
['red', 'blue', 'green', 'white', 'black']

Reverse list
['black', 'white', 'green', 'blue', 'red']

Sort list
['black', 'blue', 'green', 'red', 'white']
```
