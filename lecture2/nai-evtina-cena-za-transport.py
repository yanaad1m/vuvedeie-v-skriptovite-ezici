n = int(input("Enter km: "))
daytime = str(input("Enter time(d/n):"))

if n < 20:
    print("Taxi is the only way!")
    if daytime == "day":
        price = (0.79 * n) + 0.7
    elif daytime == "night":
        price = (0.9 * n) + 0.7
elif n > 20 and n <= 100:
    print("Bus is the better option!")
    price = 0.09 * n
elif n > 100:
    print("Train is your best option!")
    price = 0.06 * n
print("price = ", price)


