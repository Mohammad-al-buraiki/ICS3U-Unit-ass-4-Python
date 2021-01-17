# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to determine whether the customer can
# get a discount or not


def main():
  # calculating the quantities
  number_of_quantities = input("Enter the number of the quantities:")
  try:
    number_of_quantities = int(number_of_quantities)
    price = 100 *(number_of_quantities)
    total = 1.13 * (price)
    discount = 0.10 *(total)
    after_discount = total - discount
    print("The total is {0: .2f} $.".format(total))
    if total > 1000:
      print("The shop will give you a discount of 10%")
      print("After the discount you have to pay {0} $.".format(after_discount))
    else:
      print("The shop will not give you a discount of 10%")

  except Exception:
    print("Sorry, that was not an integer")


if __name__ == "__main__":
    main()
