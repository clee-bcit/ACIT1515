# Chris Chanwoo Lee
# ACIT1515 - SET B
# A01016225

"""
This module builds a restuarant order from a menu. Based on this order it
calculates the total bill including tax and tip. Each order can contain up
to three items.

Hints:
    Conditional Statement and Membership operator: in - https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/5/section/9?content_resource_id=49219380
    Function Basics - https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/4/section/1
    List Item Retrieval: https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/8/section/1
    Dictionary index and retrival -  https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/8/section/12  
    Docstrings and DocTests: 
        https://learn.zybooks.com/zybook/BCITACIT1515LaneFall2021/chapter/4/section/16?content_resource_id=49219776
        Course Content -> Class 4 -> Code Style -> Run-able Examples: doctest
"""
from typing import List

MENU = {
    "eggs": 6.00,
    "sausage and eggs": 8.00,
    "bacon and eggs": 7.50,
    "pancakes": 7.00,
    "cereal": 5.50,
    "coffee": 2.00,
    "tea": 1.50,
    "juice": 3.50,
}

# Add item_charge function, the docstring is below
"""Looks up and returns charge for individual item based on menu price

Args:
    item (str): the name of the item as it appears in the menu

Returns:
    float: the price of the item from the menu or 0 if not on the menu

Examples:
    >>> item_charge('eggs')
    6.0

    >>> item_charge('tea')
    1.5

    >>> item_charge('omelette')
    0
"""
def item_charge(item):
    if item in MENU:
        item_price = MENU[item]
    else:
        item_price = 0
    return item_price


# Add calculate_bill function, the docstring is below
    """
    Calculates and returns the total bill rounded to the nearest cent for list of items in order

    Adds up all of the items on the order (there will only be 0, 1, 2, or three items)

    This bill includes the following taxes:
        PST: 7%
        GST: 5%

    The bill also includes a tip of 15%

    The additional charges are only applied to the bill itself
    I.E.

        PST = item total * PST Rate
        GST = item total * GST Rate
        Tip = item total * Tip Rate

        Bill = item total + PST + GST + TIP

    Args:
        order (List[str]): a list of menu items

    Returns:
        float: total bill

    Examples:
        >>> calculate_bill(['eggs', 'coffee', 'juice'])
        14.6

        >>> calculate_bill(['bacon and eggs', 'cereal', 'tea'])
        18.41

    """
def calculate_bill (order):
    total_bill = 0
    tip = 0
    for item in range(len(order)):
        tip = MENU[order[item]] * 0.15
        tax_PST = MENU[order[item]] * 0.07
        tax_GST = MENU[order[item]] * 0.05

        total_price = MENU[order[item]] + tip + tax_PST + tax_GST
        total_bill += total_price
    return total_bill




    
def build_order() -> List[str]:
    """
    Prompt the user for up to three items that they want and add them to
    their order - a list of items.

    If the item is not on the menu inform them by printing:
       f"Sorry, we don't have {item}"

    After a inputing a failed item the user will continue with their next
    menu item.  They only have there items selections regardless of how many
    selections are actually on the menu

    Returns:
        List[str]:  order as a list of all of items names
    """
    order = []

    item1 = input("Please select a menu item for your order: ")
    if item1 in MENU:
        order.append(item1)
    else:
        print(f"Sorry, we don't have {item1}")

    item2 = input("Please select another menu item for your order: ")
    if item2 in MENU:
        order.append(item2)
    else:
        print(f"Sorry, we don't have {item2}")

    item3 = input("Please select another menu item for your order: ")
    if item3 in MENU:
        order.append(item3)
    else:
        print(f"Sorry, we don't have {item3}")

    return order


def main():
    """
    Build the customer order, calculate the bill, print the order and total cost
    """
    # Add Code to invoke build_order function
    order = build_order()

    # Add Code to invoke calculate_bill function
    total = calculate_bill(order)

    # Following print the items in the order
    print(f"Your order was: {order}")

    # Following prints the total bill
    print(f"Your bill will be: ${total:2.2f}")


if __name__ == "__main__":
    main()
