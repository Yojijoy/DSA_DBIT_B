def sum_tail(n, acc=0):
    if n == 0:
        return acc
    return sum_tail(n - 1, acc + n)
print("Sum up to 5:", sum_tail(5))
