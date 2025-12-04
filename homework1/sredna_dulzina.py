n = int(input("Vuvedi broi nizove: "))
strings = []

for i in range(n):
   s = input(f"Vuvedi niz: ")
   strings.append(s)

dulzina = 0

for s in strings:
   dulzina += len(s)

sredna_dulzina = dulzina/n
print("Srednata dulzina na nizovete e : ", sredna_dulzina)