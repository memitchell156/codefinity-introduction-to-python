#define the apply discount
def apply_discount(price, discount=0.05):
    return price * (1 - discount)

#define apply tax
def apply_tax(price, tax=0.07):
    return price * (1 + tax) 
    
#define calculate total
def calculate_total(price, discount=0.05, tax=0.07):
    # uses apply_discount() and apply_discount() to return the total price
    discounted_price = apply_discount(price, discount=discount)
    total_price = apply_tax(discounted_price, tax=tax)
    return total_price

#call with default discount and tax
total_price_default = calculate_total(120)

#call with custom values
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)


print(f"Total cost with default discount and tax: ${total_price_default}")

print(f"Total cost with custom discount and tax: ${total_price_custom}")