FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):            # <------ Custom Function
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:    # r - read
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file:  # w- write
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
