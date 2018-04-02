#PiterPG
nums = []

for c in range(1,6):
    num = float(input("{}° Número: ".format(c)))
    nums.append(num)
    
num1,num2 = max(nums),min(nums)
    
print("\nO Maior Número é {:.2f} \n\
O Menor Número é {:.2f} \n".format(num1,num2))