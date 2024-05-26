import random
def prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(k):
        a = random.randint(2,n-1)
        if pow(a,n-1,n) !=1:
            return False
    return True
num = 2
print(f"{num} is prime:", prime_fermat(num))
