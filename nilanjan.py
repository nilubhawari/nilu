# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TmWPx2Y8HJ7VxG-YAXbTK0LJL7qPa9ZC
"""

Q = float(input("Enter the value of discharge:"))
T = int(input("Enter the value of top width:"))
g = float(input("Enter the value of acceleration due to Gravity:"))
y1 = float(input("Enter the value of upstream depth:"))
Z = float(input("Enter the value of hump:"))

# Discharge per meter width
q = Q / T
print("The value of discharge per meter width is:", q)

# Area Calculation
A1 = T * y1
print("The value of upstream area is:", A1)

# Calculation of Froude Number
Fr1 = ((Q * Q * T) / (g * A1 * A1 * A1)) ** 0.5
print("The value of Froude number is:", Fr1)
if Fr1 > 1:
    print("The flow is Super Critical Flow")
else:
    print("The flow is Sub Critical Flow")

# Upstream Energy
E1 = y1 + ((Q * Q) / (2 * g * A1 * A1))
print("The value of Energy at Initial Section is:", E1)

# Downstream Energy
E2 = E1 - Z
print("The value of Downstream Energy E2 is:", E2)

# Critical Depth
yc = (q * q / g) ** 0.3333
print("The value of critical depth is:", yc)

# Critical Energy
Ec = 1.5 * yc
print("The value of Critical Energy is", Ec)
if Ec > 2:
    print("Choking Condition")
else:
    print("SAFE")

# Calculation of Zmax
Zmax = E1 - Ec
print("The value of maximum hump is:", Zmax)