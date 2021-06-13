# List

List is one of the sequence data types in Python. It can be referred as a collection of homogenous items.

```txt
emptyList = []
strList = ["red", "blue", "green"]
numList = [1, 2, 3, 4, 5]
```

## List Indices

List stores both index and value of its items. The left most item of a list holds the index `0`. Index is incremented by 1 for the items from left to right.

```python
l = ["red", "blue", "green"]
print(l[0])
print(l[1])
print(l[2])
```

Output:

```txt
red
blue
green
```

A list can also be accessed in reverse order using negative indexing. In case of negative indexing, last item in a list can be accessed using the index `-1`.

```python
l = ["red", "blue", "green"]
print(l[-1])
print(l[-2])
print(l[-3])
```

Output:

```txt
green
blue
red
```

## Access range of items

A child list with indices x to y can be accessed from a list using `:` operator.

```python
l = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(l[1:5])
```

Output:

```txt
['two', 'three', 'four', 'five']
```

## Mutable

List is mutable. A list can be added, updated and deleted after creation.

* append() -> Adds items to a list.
* remove() -> Removes items from a list.

Let's look at a simple Python program that performs `append`, update and `remove` on a list.

```python
strList = ["red", "blue", "green"]
print("Items in list are")
for s in strList:
    print(s)

strList.append("black")
print("\nAdd items to a list")
for s in strList:
    print(s)

strList[3] = "white"
print("\nUpdate items to a list")
for s in strList:
    print(s)

strList.remove("white")
print("\nRemove items from a list")
for s in strList:
    print(s)
```

Output:

```txt
Items in list are
red
blue
green

Add items to a list
red
blue
green
black

Update items to a list
red
blue
green
white

remove items from a list
red
blue
green
```
