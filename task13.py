
narx = int(input("1-telefon narxi: "))
min_price = narx
max_price = narx

for i in range(1, 5):
    narx = int(input(f"{i+1}-telefon narxi: "))
    if narx < min_price:
        min_price = narx
    if narx > max_price:
        max_price = narx

print("Eng arzon narx:", min_price)
print("Eng qimmat narx:", max_price)
