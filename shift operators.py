#shift operators
# >>, <<

num1 = 8
num2 = 2
result1 = num1 >> num2
#rt shift base is always 2
# num1 divide by base power num2
result2 = num1 << num2

result3 = result2 >> num2

print("result1:",result1)
print("result2:",result2)
print("result3:",result3)
