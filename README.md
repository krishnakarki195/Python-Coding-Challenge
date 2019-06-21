## Overview

You are the owner of a grocery store and would like to build an application for your employees to easily find items. 
Your task is to create an application that accepts user input and allows them to filter data from an existing CSV file.

## Project Setup

Install required packages:

```
pip3 install -r requirements.txt
```

## Instructions

All product data is stored in `products.csv`.

User input is format as `PRICE_MIN PRICE_MAX EXPIRES_START EXPIRES_STOP`
- `PRICE_MIN` - minimum price (* indicates no minimum)
- `PRICE_MAX` - maximum price (* indicates no maximum)
- `EXPIRES_START` - earliest expiration date (* indicates no earliest date)
- `EXPIRES_STOP` - latest expiration date (* indicates no latest date)

Example user input and output would be:

```
> 2.40 2.60 JAN-01-2019 JAN-31-2019
+-----+----------------+-------+-------------+
|  id |      name      | price |   expires   |
+-----+----------------+-------+-------------+
|  23 | Cheddar Cheese |  2.52 | JAN-16-2019 |
| 187 | Garlic Powder  |  2.55 | JAN-23-2019 |
+-----+----------------+-------+-------------+
```

## Completion

After you are finished with the challenge, commit your changes, push to your GitHub, and send us a link.
