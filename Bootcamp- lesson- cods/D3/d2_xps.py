# XP 8

toppings = []

topping = input("Topping or Quit: ") 

while topping != "QUIT":

    toppings.append(topping) 
    print(f"Adding {topping} to pizza")
    topping = input("Topping or Quit: ") 

base_price = 10
toppings_price = 2.5 * len(toppings)

total_price = base_price + toppings_price

print("TOPPINGS:", toppings, "Total price:", total_price)