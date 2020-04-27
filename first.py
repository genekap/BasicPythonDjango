# ----------------------------------------------------------
# #Sum Program
# print("------------------------------")
# print("#Summationnnnnnn Program")
# print("#type 'Exit'to end the Program")
# print("------------------------------")

# # var bindind result

# sumdata = 0
# count = 1
# # Start input While Loop
# while True:
#     data = input(f"Enter Number{count}:")
#     # check the exit
#     if data == "exit":
#         break
#     # Sum the Input
#     sumdata += int(data)
#     count = count + 1
# # -----End Loop-----------
# print(f"Sum value is {sumdata}")

# #END of Script---------------------------------------------

# -------List-----------------------------------------
number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Javis', 'Watson']
mix = [10, 20, 35, 'Gene']

# Indexing
# print(number[0])
# Counting List Components
# print(len(number))
# Looping Function
# for n in number:
#     print(n)
# Sum from Loop
# sumnum = 0
# for num in number:
#     sumnum = sumnum + num
# print(sumnum)

# -----------------------Tuples-----------------------------
# TpNumber = (1, 2, 3, 4, 5)
# TpMixed = (10, 20, [5, 4, 3], True, 'Gene')
# print(TpNumber[2])
# print(TpMixed[2][1])

# ---------------------Dictionary---------------------------
DctScores = {
    'John': 1200,
    'Jame': 2000,
    'Jume': 4200
}
# print(DctScores)
# # Assign new Dct Value
# print(DctScores['Jame'])
# DctScores['Jona'] = 3200
# print(DctScores)
# Empty Dct
# DctPoint={}
# # Assign to Empty Dct
# DctPoint['Mr_A']=10.2
# DctPoint['Mr_B']=20.4
# DctPoint['Mr_C']=32.6
# print(DctPoint)
# Looping
# -------------------Function-----------------------
# No Return Value


def FnHello(name):
    print(f"Hello {name}")
# Return Value


def FnArea(width, height):
    RtTotal = width * height
    return RtTotal


# call Fnhello
FnHello("Gene")
# call FnArea
print("Area is ", FnArea(5, 8))

# Fn with DfArgVl


def FnShow_Info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language:{lang}")


FnShow_Info()
