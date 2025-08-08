first_num = int(input("enter the first number:"))
second_num = int(input("enter the second number:"))
operator = input("enter operator:")
if operator == "+":
    print(f"{first_num}+{second_num}={first_num+second_num})")

elif operator == "-":
    print(f"{first_num}-{second_num}={first_num-second_num}")

elif operator == "/":
    print(f"{first_num}/{second_num}={first_num/second_num}")

elif operator == "*":
    print(f"{first_num}*{second_num}={first_num*second_num}")

else:
    print("invalid operator")
