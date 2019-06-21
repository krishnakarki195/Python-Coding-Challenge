
from prettytable import PrettyTable
import csv
import datetime

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']

def display_table(filtered_values):
    """
    Display product table
    """ 
    for product in filtered_values:
        table.add_row(product)
    print(table)
    table.clear_rows()

def search(product_list, input_value):
    filtered_values = []
    for product in product_list:
        m,d,y = map(int,product[3].split('/'))
        product_date = datetime.date(y,m,d)
        if float(product[2]) > input_value['min_price'] and float(product[2]) < input_value['max_price']:
            if product_date > input_value['expire_start'] and product_date < input_value['expire_stop']:
                formated_date = product_date.strftime('%b').upper()+'-'+str(product_date.day)+'-'+str(product_date.year)
                product[3] = formated_date
                filtered_values.append(product)
    return filtered_values

def process_input(user_input):
    input_value = {}
    months = {
            'JAN':1,
            'FEB':2,
            'MAR':3,
            'APR':4,
            'MAY':5,
            'JUN':6,
            'JUL':7,
            'AUG':8,
            'SEP':9,
            'OCT':10,
            'NOV':11,
            'DEC':12
        }
    try:
        min_price,max_price,expire_start,expire_stop = user_input.split()
        min_price,max_price = map(float,[min_price,max_price])
        input_value['min_price'] = min_price
        input_value['max_price'] = max_price
        m,d,y = expire_start.split('-')
        input_value['expire_start'] = datetime.date(int(y),months[m],int(d))
        m,d,y = expire_stop.split('-')
        input_value['expire_stop'] = datetime.date(int(y),months[m],int(d))
        return input_value
    except ValueError:
        raise ValueError("Plesae inter min_price max_price expire_start expire_stop format!")

def start():
    """
    Start accepting user input
    Quit program when user types 'exit'
    """
    product_list = []
    with open('products.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            product_list.append(row)
    while True:
        value = input('> ')
        if value == 'exit':
            break
        display_table(search(product_list,process_input(value)))

if __name__ == '__main__':
    start()
