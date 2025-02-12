print("".center(80, "-"))
print("FIBONACCI SEQUENCE".center(80, " "))
print("By Ethan A. Minja".center(80, "-"))

Limit = int(input("How many Fibonacci values would you like to print: "))

x = 0
y = 1

print(x)
print(y)

for N in range(Limit):
    Fib = x + y
    x = y
    y = Fib
    print(Fib)
