customer_code = input("Please enter your customer code: ")
customer_name = input("Please enter your customer name: ")

print(f"Welcome {customer_name}! your customer code is {customer_code}")

total_item = 0
item_names = []
item_prices = []

for i in range(2):
    item_name = input("Please enter item name: ")
    item_price = input("Please enter item price: ")

    item_names.append(item_name)
    item_prices.append(int(item_price))
    total_item += int(item_price)
    
print(f"Total Price of 2 item {item_names} is {total_item}")