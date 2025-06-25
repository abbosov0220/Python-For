n = int(input("n: "))
sum_juft = 0
sum_toq = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_juft += i
    else:
        sum_toq += i
print(sum_juft, sum_toq)
