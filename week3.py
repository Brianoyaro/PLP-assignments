def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        if discount_percent > 100:
            discount_percent = 100
        rate = 100 - discount_percent
        return price * (rate / 100)
    return price

price = int(input('Enter the original price of an item: '))
discount = int(input('Enter the dicount percentage: '))
print(calculate_discount(price, discount))
