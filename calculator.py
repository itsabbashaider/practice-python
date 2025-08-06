# Start
#   ↓
# Display operation menu
#   ↓
# Get user choice
#   ↓
# Get first and second numbers
#   ↓
# IF choice == 1 → Add
# ELIF choice == 2 → Subtract
# ELIF choice == 3 → Multiply
# ELIF choice == 4 → Check if second number == 0
#     ↳ If yes → Show error
#     ↳ If no  → Divide
# ELSE → Show "Invalid choice"
#   ↓
# Display result
#   ↓
# End

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
def Modulo(x, y):
    return int(x % y)
def Percent(x, y):
    return round((x / y )* 100, 2)

print("Select operation")
print("1.add")
print("2.multipy")
print("3.subtract")
print("4.divide")
print("5.Modulo")
print("Percent")

choice = input("Enter choice (1/2/3/4/5/6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", (add(num1, num2)))
elif choice == '2':
    print("Result:", (subtract(num1, num2)))
elif choice == '3':
    print("Result:", (multiply(num1, num2)))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", Modulo(num1, num2))
elif choice == '6':
    print("Result:", str(Percent(num1, num2)) +"%")
else:
    print("Invalid input")
