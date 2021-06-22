# Dict Methods

Below are the in-built list methods supported by Python.

* `dict.clear()`
* `dict.get(<key>)`
* `dict.items()`
* `dict.keys()`
* `dict.values()`
* `dict.pop(<key>)`
* `dict.popitem()`
* `dict.update(<obj>)`

```python
dict1 = {'a': 100, 'b': 200, 'c': 300}
#Empties dictionary dict of all key-value pairs
print("\n Empty a dictionary")
dict1.clear()
print(dict1)

dict1 = {'a': 100, 'b': 200, 'c': 300}
#Returns the value for a key if it exists in the dictionary.Otherwise it returns None.
print("\n Value for the key is")
val = dict1.get('b')
print(val)
print(dict1.get('z'))
#If <key> is not found and the optional <default> argument is specified, that value is returned instead of None.
print(dict1.get('z', -1))

#Returns a list of tuples containing the key-value pairs in dict1. The first item in each tuple is the key, and the second item is the key’s value.
print("\n All items in dict1")
print(list(dict1.items()))
print(list(dict1.items())[1][0])
print(list(dict1.items())[1][1])

#Returns a iterable object of all keys in dict1
print("\n keys in dict1")
print(dict1.keys())

#Returns a iterable object of values in dict1
print("\n Values in dict1")
print(dict1.values())

#Removes a key from a dictionary, if it is present, and returns its value.
value = dict1.pop('b')
print(value)
print("\n Items after pop")
print(dict1)
value = dict1.pop('z')

dict1 = {'a': 100, 'b': 200, 'c': 300}
#Removes the last key-value pair added from dict1 and returns it as a tuple

value = dict1.popitem()
Print(value)
print("\n Items after popitem")
print(dict1)
print(dict1.popitem())
print(dict1)
print(dict1.popitem())
print(dict1.popitem())

dict1 = {'a': 100, 'b': 200, 'c': 300}
#To update an entry, you can just assign a new value to an existing key
dict1['b'] = 101
print("\n Items after update")
print(dict1)
```

Output:

```txt
Empty a dictionary
{}

Value for the key is
200
None
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
KeyError: 'z'

('c', 300)
Items after popitem
{'a': 100, 'b': 200}
('b', 200)
{'a': 100}
('a', 100)
KeyError: 'popitem(): dictionary is empty'

Items after update
{'a': 100, 'b': 101, 'c': 300}
```