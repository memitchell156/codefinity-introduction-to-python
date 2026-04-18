grocery_inventory = {"Milk": ("Diary", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.50, 50)}
category, price, quantity = grocery_inventory["Eggs"]

if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price -= 1
    grocery_inventory["Eggs"] =(category, price, quantity)
else:
    pring("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

category, price, quantity = grocery_inventory["Milk"]
if quantity < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    quantity += 20
    grocery_inventory["Milk"] = (category, price, quantity)
else:
    print("Milk has sufficient stock.")

category, price, quantity = grocery_inventory["Apples"]
if price < 2:
    print("Apples removed from invenroty due to high price.")

print("Updated inventory:", grocery_inventory)

print(grocery_inventory)
