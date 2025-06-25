min_val = int(input("1-son: "))

for i in range(6):
    x = int(input(f"{i+2}-son: "))
    if x < min_val:
        min_val = x

print("Eng kichik son:", min_val)
