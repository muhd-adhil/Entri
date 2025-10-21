# accept input from user

a = input("enter the first number: ")
b = input("enter the second number: ")

num1 , num2 = int(a) , int(b)

# calculations

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2


print(f"""
    Addition: {num1 + num2} = {sum} \n
    Subtraction: {num1 - num2} = {sub} \n
    Multiplication: {num1 * num2} = {mul} \n
    Division: {num1 / num2} = {div} \n
 """)

# concatenation
print(f"concatenation string {a}+{b} ={a+b}")