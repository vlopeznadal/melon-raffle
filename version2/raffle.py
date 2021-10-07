"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

from customers import get_customers_from_file
import random

def pick_customer(customers):

    random_customer = random.choice(customers)

    return random_customer

def print_customer_info(random_customer):

    name = random_customer.name
    email = random_customer.email

    print(f"Congratulations {name} at {email}!")

def run_raffle():   
    customers = get_customers_from_file("customers.txt")
    random_customer = pick_customer(customers)
    print_customer_info(random_customer)

if __name__ == "__main__":
    run_raffle()