import sys, random

nums = int(sys.argv[2])
with open(sys.argv[1], mode='w') as file:
    for i in range(0, nums):
        file.write(str(random.randint(0,1000)) + " ")

