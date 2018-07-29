# Objects

**Everything in python is an object**

- all variable assignments in python are references to objects (even simple integers)
- once all references to an object are gone, it will be garbage collected and we lose access to them
- using the .id() method, we can get a unique identifier for an object
- the **is** comparison operator uses the .id() method and checks for actual equality
    - value - equivalent "contents" (==)
    - identity refers to the same object (.id())

- **very similar to JS as if the referenced object changes, all variables referencing the object change too**
- **python doesn't really have variables in a classical sense (variable containing a value) but rather only has named**
    **references to objects**

- using the **dir** method on anything will give us an overview of every property / method etc of that object
    - the \__doc__ property includes all doc strings attached  
    - this is a repl thing

## Summary:

- Think of named references to objects rather than variables
    - Assignment attaches a name to an object
    - Assigning from one reference to another puts two name tags on the same object
- the garbage collector reclaims unreachable objects
- `id()` returns a unique and constant identifier
    - rarely used in production
- The `is` operator determines equality of identity
- Test for equivalence using `==` 
- Function arguments are passed by object reference
    - functions can modify mutable arguments
- Reference is lost if a formal function argument is rebound
    - To change a mutable argument, replace it's `contents`
- even `return` passes by obvject-reference
- Function arguments can be specified with defaults
- Default argument expressions are evaluated only once, when `def` is executed
- Python uses `dynamic typing`
    - We don't specify types in advance
- Python uses strong typing
    - Types are not coerced to match

- Names are looked up in four nested scopes
    - **LEGB rule: Local, Enclosing, Global and Built-ins**
- Global references can be read from a local scope
- Use `global` to assign to global references from a local scope
- `Everything` in Python is an object
    - This includes modules and functions
    - They can be treated just like other objects

- `import` and `def` result in binding to named references
- `type` can be used to determine the type of an object 
- `dir()` can be used to introspect an object and get its attributes 
- the name of a function or module object can be accessed through its `__name__` attribute
- the docstring for a function or module object can be accessed through its `__doc__` attribute or calling `help()` on it 

- Use len() to measure the length of a string
- You can mulitply a string by an integer!
    - Produces a new string with multiple copies of the operand
    - this is called the `'repetition'` operation