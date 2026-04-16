grocery_items = "milk cheese bread apples oranges chicken"
#d1- milk
#d2- cheese
#b1 - bread
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]
new_word = dairy1 + " " + dairy2 + " " + bakery1
print(f"We have dairy and bakery items: {dairy1}, {dairy2}, and {bakery1} in aisle 5.")