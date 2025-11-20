numbers = []
n = int(input("Vuvedi broi elementi: "))
for i in range(n):
    num = int(input(f"Vuvedete element {i+1}: "))
    numbers.append(num)
numbers.sort()
print("Sortiran spisuk: ", numbers)