# TODO
import cs50


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)

def get_cents():
    # TODO
    n = 0
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);
    return n

def calculate_quarters(cents):
    # TODO
    quarters = 0

    while cents >= 25:
        cents = cents - 25
        quarters += 1
    return quarters


def calculate_dimes(cents):
    # TODO
    dimes = 0

    while cents >= 10:
        cents = cents - 10
        dimes += 1
    return dimes

def calculate_nickels(cents):
    # TODO
    nickels = 0

    while cents >= 5:
        cents = cents - 5
        nickels += 1
    return nickels

def calculate_pennies(cents):
    # TODO
    pennies = 0

    while cents >= 1:
        cents = cents - 1
        pennies += 1
    return pennies

main()
