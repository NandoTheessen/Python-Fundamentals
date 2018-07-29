# Scope 

- Scopes are contexts in which named references can be looked up (same as in JS)
- Scopes found in python: 
    - **Local:** Inside the current function
    - **Enclosing:** Any and all enclosing functions (Closure)
    - **Global:** Top-level of module
    - **Built-in:** Provided by the builtins module
- important to note: not every indented block signals a new scope! 
    - for loops and if statements f.e. don't

- if we want to re-assign references from the global scope in a function, we have to use the global keyword in compination
    with the reference name

Together these scopes define the **LEGB** rule:

*Names are looked up in the narrowest relevant context*