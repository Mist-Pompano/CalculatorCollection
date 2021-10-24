
x = int(input("What would you like your starting number to be?"))
y = int(input("What would you like your ending number to be?"))
        
for even in range(x, y, 2):
    for odd in range(x, y, 1):
        val = even + odd
        print(even, "+", odd, "=", val)
