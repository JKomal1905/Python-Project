menu = {
    'Pizza':440,
    'Pasta':70,
    'Burger':120,
    'Coffee':90,
}
#greet
print("welcome to restaurant")
print("Pizza: Rs440\nPasta: Rs70\nBurger: 120\nCoffee: 90")
Order_Total = 0
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    Order_Total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet")
another_order = input("do you want to add another item?(Yes/No)")
if another_order == "Yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
       Order_Total += menu[item_2]
       print(f"item {item_2} has been added to order")
    else:
       print(f"ordered item {item_2} is not available!")
print(f"The total amount of items to pay is {Order_Total}")
