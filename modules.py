import math
import random
import sys
import os
import salary
import utility
print(dir(salary))
print("********************************")
print("sys modules:",sys.modules)
print("sys path :",sys.path)
print("os name:",os.name)
print("sys version:",sys.version)
print("get current working directory: ",os.getcwd())

print(utility.isLeapYear(1900))
print("prefered payment mode is :",utility.payment_modes[1])
salary.calculateSalary()
print("*"*60)
print("*"*60)

