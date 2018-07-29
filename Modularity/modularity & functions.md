# functions 
- have an implicit return of None
- will return one liners properly
- defining a main() function (or smth with the functionality but a different name) that executes what is necessary is considered good practice
- 2 blank lines between root level functions, 1 between methods
- the **def** keyword binds a function definition to a name

- default arguments:
    - basically making arguments optional for the function in question
    - they can be modified like any other object
    - it is important to remember that default argument values are evaluated 
    when def is evaluated, this happens only once.
        - you'll realize this the moment you try to run a function twice with only it's default arguments
            as the argument stays the same (given an empty list, we will keep adding to that list forever)
        - **to avoid this, we'll use immutable objects as defaults such as None and then create the default in an if statement**
- **if we wish, we can pass our arguments in any order we'd like as long as we preface**
    **the value by the variable name given in the function definition**


# modularity 

- we can define imports as:
    - import _module_
    - from _module_ import function / class / object
    - from _module_ import *  <-- **only** for casual use in the repl, as this can cause massive namespace problems in larger projects

#### documenting your code using docstrings

- first line of a function should be used to document it's use
- docstrings are used to do this, they are initiated by """ *content* """ 
- content: 
    - functionality
    - Args:
    - Returns: 
- **the content of our docstrings can be called by using the _help_ command from the cli with the function / class / object name as parameter**

#### comments

- while generally docstrings should do most of the documenting for us comments should still be used when:
    - it is not inherently clear why a certain technique was chosen
    - why we are accessing a particular index of something 
    - and all other things that might be confusing for someone that has to maintain our code / ourselves