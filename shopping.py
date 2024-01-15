budget = int(input())
n = input()

while n != "End":
    shopping_products = int(n)
    budget -= shopping_products  # budget = abs(shopping_products - budget)
    if budget < 0:
        print("You went in overdraft!")
        break
    n = input()
else:
    print("You bought everything needed.")