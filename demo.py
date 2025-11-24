a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("\nSelect Operation:")
print("1. Add")
print("2. Subtract")

choice = input("\nEnter choice (1/2): ")

if choice == "1":
    print("Result =", a + b)
else:
    print("Result =", a - b)
