# 1st input: enter height in meters e.g: 1.65
height = input("enter height in meters e.g: 1.65\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter weight in kilograms e.g: 72\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_frt = float(height)
weight_frt = float(weight)
icm = int(weight_frt / (height_frt ** 2))

print(icm)