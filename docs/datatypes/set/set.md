# Set

Sets are one of the built-in data types in Python. It can be referred as a collection of items.

Sets can **also** be used efficiently to perform MATH operations like `union`, `intersection` and `symmetric_intersection`.

```python
s = {"red", "blue", "green"}
```

Unlike `Lists` and `Tuples`, Sets are `unordered` and `unindexed`, which means you cannot be sure about the order of Set elements.

```python
s = {"red", "blue", "green"}
print(s)
```

## **List vs Tuple vs Set**

| Tuple      | List | Set |
| ----------- | ----------- | ---------- |
| Tuple is Immutable      | List is Mutable       | Set can be added and deleted but not updated |
| Tuple is more appropriate for accessing data      | List is more appropriate for performing insertion, updating and deletion| Set is mostly used to perform MATH Operations |
| Initialized using ()   | Initialized using []| Initialized using {} |

Execute the above program multiple times to notice that the order of set elements is not the same every time.

## No Duplicates

In Python, Sets does not allow you to store duplicates.

```python
s = {"red", "blue", "green", "red"}
print(s)
```

## No Modifications

Elements in a set cannot be modified. However, elements can be added and removed.
