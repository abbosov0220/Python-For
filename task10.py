max_val = int(input("1-son: "))

for i in range(6):
    x = int(input(f"{i+2}-son: "))
    if x > max_val:
        max_val = x

print("katta son:", max_val)
