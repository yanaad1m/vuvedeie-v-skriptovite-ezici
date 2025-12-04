K = int(input("Vuvedi broi cifri: "))

digits = 1
pages = 0
count = 9

while K > count * digits:
    K -= count * digits
    pages += count
    digits += 1
    count *= 10

pages += K // digits

print("Broi stranici:", pages)
