# n!/(k!⋅(n−k)!)

# The method which implements 'n choose k' formula.
def n_choose_k(n, k):

    return recursive_factorial(n) / (iterative_factorial(k) * recursive_factorial(n - k))


# Calculating factorial recursively
def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)


# Calculating factorial iteratively
def iterative_factorial(num):
    prod = 1
    for i in range(num):
        prod *= (i + 1)
    return prod


if __name__ == '__main__':
    print("Total possible combinations of hands to be dealt: " + str(n_choose_k(52, 2)))
    print("Total possible combinations of 5 cards, to be put down as Flop + Turn + River: " + str(n_choose_k(52, 5)))


