'''A script showing examples of how to mutate list'''
m = [9, 15, 24]


def modify(k):
    '''appends the item 39 to given list

    Args:
        list k
    '''
    # In this case the original list gets mutated as we are only passing it's
    # reference into the modify function
    k.append(39)
    print("k =", k)


f = [14, 23, 37]


def replace(g):
    '''This function "replaces" the object g
    correctly, you'd say "this function moves the reference pointer of
    variable g to the newly defined array!"

    Args:
        list g
    '''
    # This function does not actually replace our passed array, as the
    # reassignment below simply moves the reference for g (orginally on our
    # passed in array) to the newly defined array
    g = [17, 28, 45]
    print("g =", g)


def banner(message, border='-'):
    '''Function showing off the default value for arguments
    printing a border with the given sign that is as long
    as the message passed in to the function!

    Args:
        message: A message the user wants printed
        border: the char that the user wants used for the border
        default is "-"
    returns:
        prints the message acompagnied by 2 borders top & bottom
    '''
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def add_spam(menu=None):
    '''This function shows the correct use of default values,
    which should be immutable and only be replaced in the function
    itself to avoid adding to the same default value again and again!

    Args:
        list of menu items, if provided
    returns:
        a menu-list'''
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    '''automatically executes all functions within objects.py
    when called via cli'''
    modify(m)
    replace(f)
    banner('standard message')
    add_spam()


if __name__ == '__main__':
    main()
