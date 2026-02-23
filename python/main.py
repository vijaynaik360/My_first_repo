# Program to calculate sum of 10 natural numbers

# Method 1: Using a loop
sum_total = 0
for i in range(1, 11):
    sum_total += i

print("Sum of 10 natural numbers (using loop):", sum_total)

# Method 2: Using built-in sum() function
sum_total2 = sum(range(1, 11))
print("Sum of 10 natural numbers (using sum()):", sum_total2)

# Method 3: Using mathematical formula n*(n+1)/2
n = 10
sum_total3 = (n * (n + 1)) // 2
print("Sum of 10 natural numbers (using formula):", sum_total3)