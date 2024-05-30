import random

def is_generator(g, p):

    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, power, p) for power in range(1, p))
    return required_set == actual_set

def find_generators(p):

    if p == 2:
        yield 1
    else:
        for g in range(2, p):
            if is_generator(g, p):
                yield g

def diffie_hellman(p, g, a, b):

    A = pow(g, a, p)
    B = pow(g, b, p)
    return A, B

def main():
    p = int(input("Enter the prime number: "))


    print(f"Generators of {p} are:")
    generators = list(find_generators(p))
    for generator in generators:
        print(generator)

    if not generators:
        print(f"No generators found for {p}: ")
        return

    g = int(input(f"Select a generator from the above list: "))
    if g not in generators:
        print("Invalid generator selected. Exiting.")
        return


    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)

    print("Randomly generated private key of Alice:", a)
    print("Randomly generated private key of Bob :", b)

    A, B = diffie_hellman(p, g, a, b)

    print("Public value of Alice :", A)
    print("Public value of Bob :", B)



main()
