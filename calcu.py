num1 = float(input("masukan angka pertama : "))
op = input("masukan operator : ")
num2 = float(input("masukan angka ke2 : "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
elif op == "%":
  print(num1 % num2)
elif op == "**":
  print(num1 ** num2)
elif op == "//":
  print(num1 // num2)
else:
  print("operator tidak tersedia")