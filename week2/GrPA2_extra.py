import re
nums = list()
with open("C:/Users/PC-Kanak/Documents/University/OB/PDSA/week2/GrPA2_input.txt", "r") as file:
    with open("C:/Users/PC-Kanak/Documents/University/OB/PDSA/week2/GrPA2_output.txt", "w") as ofile:
        txt = file.read()
        nums =  re.split("\s", txt)
        for num in nums:
           print(num, file = ofile)

print(nums)