from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']


def display_table():
    """
    Display product table
    """

    table.add_row([1, 'First sample item', 1.23, 'JAN-01-2019'])
    table.add_row([2, 'Second sample item', 2.34, 'JAN-02-2019'])
    print(table)
    table.clear_rows()


def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """

    while True:
        value = input('> ')
        if value == 'exit':
            break
        display_table()


if __name__ == '__main__':
    start()