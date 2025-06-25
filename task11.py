n = int(input("Nechta son kiritasiz: "))

x = int(input("1-son: "))
min_val = x
max_val = x

for i in range(1, n):
    x = int(input(f"{i+1}-son: "))
    if x < min_val:
        min_val = x
    if x > max_val:
        max_val = x

avg = (min_val + max_val) / 2
print("O'rtacha:", avg)
