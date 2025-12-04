n = int(input("Vuvedi broi chisla: "))
numbers = []

for i in range(n):
    num = float(input(f"Vuvedete chislo: "))
    numbers.append(num)

sum_kvadrati = 0

for num in numbers:
    kvadrat = num * num
    sum_kvadrati += kvadrat

print("Sum ot kvadratite e : ", sum_kvadrati)