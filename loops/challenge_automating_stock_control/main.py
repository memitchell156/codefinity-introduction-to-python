# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    stock = inventory[item][0]
    minimun = inventory[item][1]
    restock_qty = inventory[item][2]
    on_sale = inventory[item][3]
    # Restock using while loop
    while stock < minimun:
        stock += restock_qty

    # update stock
    inventory[item][0] = stock

    # apply discount rule
    if stock > discount_threshold and not on_sale:
        inventory[item][3] = True

print("Processing completed")



    