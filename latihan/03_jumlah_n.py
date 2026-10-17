def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("n = 1:", jumlah_n(1))
print("n = 5:", jumlah_n(5))
print("n = 10:", jumlah_n(10))
print("n = 100:", jumlah_n(100))

print("\nPerbandingan dengan rumus n(n+1)/2:")
for n in [1, 5, 10, 100]:
    rumus = n * (n + 1) / 2
    print(f"n = {n}: {rumus}")