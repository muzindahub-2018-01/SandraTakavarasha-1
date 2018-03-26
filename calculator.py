# Add two numbers 
def add(num1, num2):
   return num1 + num2

# Subtract two numbers 
def subtract(num1, num2):
   return num1 - num2
   
# Multiply two numbers
def multiply(num1, num2):
   return num1 * num2

# Divide two numbers
def divide(num1, num2):
   return num1 / num2

print("Choose a number with the calculation you want to perform.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

status_message = "The answer is {}"

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(status_message.format(add(num1,num2)))

elif choice == '2':
   print(status_message.format(subtract(num1,num2)))

elif choice == '3':
   print(status_message.format(multiply(num1,num2)))

elif choice == '4':
   print(status_message.format(divide(num1,num2)))
else:
   print("The option you selected is not available")