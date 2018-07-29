# Dictionaries

#### General
- access through the `['key']` syntax
- as in JS contains key - value pairs, keys have to be unique
- key objects **must** be immutable, so strings, numbers & tuples are fine.
    list are not
- order is not to be relied upon!
- the `in` & `not in` operators can be used w/ only the keys of the dict

- For a better presentation of dicts the `Pretty Printing` module should be used (pprint func)

#### The `dict()` Constructor
- We can convert other iterables containing key - value pairs into dicts using the 
    `dict()` constructor
- We are also able to simply pass keys & values directly into the constructor:
```python
my_dic = dict(a= 'alfa', b='beta', c= 'charlie')
```

#### Copying && Extending dicts
Of the two copy methods - *both shallow*, the second is very much preferred:
- `dict.copy()`
- passing the dict we want to copy into the `dict()` constructor

- the simplest way to extend a dict is the `.update()` method
    - can also be used to update actual values of keys, old one will be overwritten

#### Iterating over dicts
- We can either iterate over the keys of a dict by simply using a for loop
- Or go over the values by iterating over `dict.values()` (array of all values)

- **Most commonly though, we want to iterate over both keys AND values**
    - this is achieved by iterating over **`dicts.items()`**:
```python
for key, value in dict.items():
    print('{key} => {value}'.format(key=key, value=value))
```

