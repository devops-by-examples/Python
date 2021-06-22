# Dict Methods

Below are the in-built list methods supported by Python.

* `clear()`
* `get()`
* `items()`
* `keys()`
* `values()`
* `pop()`
* `popitem()`
* `update()`

Lets look into each of these built-in functions to understand how they are used.

```python

# clear()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print(dict1)
print("Perform Clear on Dict")
dict1.clear()
print(dict1)

# get()
dict1 = {'a': 100, 'b': 200, 'c': 300}
print("\n")
print(dict1)
print("Get value of the key b")
val = dict1.get('b')
print(val)

# return None for the key that does not exist.
print("\n Get value of the key b")
print(dict1.get('z'))

# returned default instead of None.
print("\n Get value of the key z")
print(dict1.get('z', -1))

# items()
print("\n All items in dict1")
print(list(dict1.items()))
print(list(dict1.items())[1][0])
print(list(dict1.items())[1][1])

# keys()
# Returns a iterable object of all keys in dict1
print("\n keys in dict1")
print(dict1.keys())

# values()
#Returns a iterable object of values in dict1
print("\n Values in dict1")
print(dict1.values())

# pop()
# Removes a key from a dictionary.
value = dict1.pop('b')
print(value)
print("\n Items after pop")
print(dict1)

# popitem()
dict1 = {'a': 100, 'b': 200, 'c': 300}
#Removes the last key-value pair added from dict1 and returns it as a tuple
value = dict1.popitem()
print(value)
print("\n Items after popitem")
print(dict1)
print(dict1.popitem())
print(dict1)
print(dict1.popitem())
print(dict1.popitem())

# update
dict1 = {'a': 100, 'b': 200, 'c': 300}
#To update an entry, you can just assign a new value to an existing key
dict1['b'] = 101
print("\n Items after update")
print(dict1)
```

Output:

```txt
{'a': 100, 'b': 200, 'c': 300}
Perform Clear on Dict
{}


{'a': 100, 'b': 200, 'c': 300}
Get value of the key b
200

 Get value of the key b
None

 Get value of the key z
-1

 All items in dict1
[('a', 100), ('b', 200), ('c', 300)]
b
200

 keys in dict1
dict_keys(['a', 'b', 'c'])

 Values in dict1
dict_values([100, 200, 300])
200

 Items after pop
{'a': 100, 'c': 300}
('c', 300)

 Items after popitem
{'a': 100, 'b': 200}
('b', 200)
{'a': 100}
('a', 100)
```
