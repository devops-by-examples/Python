# Questions

## What are the key differences between Tuple and a List ?

Please refer to the difference table provided in the previous section.

## Why Tuple consumes less memory than List ?

Tuple is Immutable, So at the time of initialization, Python knows the amount of memory to allocate. A list is a mutable hence implying dynamic allocation of memory, so to avoid allocating space each time you append or modify the list. It allocates additional space for future append, modifications. However, the amount of additional space allocated depends on the platform and type of Python.

## Why is Tuple faster than List ?

Tuple directly reference their elements whereas in case of lists there is an additional layer of indirection to an external array of pointers.

## Can you perform sort on a Tuple ?

No. Tuple is Immutable and ordered. We cannot update/modify or delete an item in Tuple.

## How do you create a Tuple with single element ?

t = ("test",)

To store a tuple with a single item, we need to make sure to add a `,` after the item. Python fails to recognize a tuple if `,` is missed.

## How do you Concatenate two Tuples ?

Like strings, We can Concatenate two Tuples using the `+` operator.

## Can you list some practical use-cases of Tuple ?

Now that we have learnt the nature of tuples, you should be able to give a thought about the practical use-cases of Tuple.
