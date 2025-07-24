# x = ["Sun","Tik"]

# print(x)

# # index
# x[1] = "Vava"

# print(x)

# # เพิ่ม data
# x.append("Tun")

# print(x)

#-----------------------------

# x = ["Sun","Tik"]

# x.pop()

# print(x)

#-----------------------------

# x = ["Sun","Tik","Ton","Vava","Gap"]

# for i in range(len(x)):
#     print(x[i])

# ---------------------------\

# score = [99,10,23,50]
# sum = 0

# for i in range(len(score)):
#     print(sum)
#     sum += score[i]

# print("total: ", sum)

# ----------------------------

# num = [1,2,3,4,5,6,7,8,9,10]

# for number in num:
#     if number % 2 == 0:
#         print("Even: ", number)
#     else:
#         print("Odd: ",number)

#----------------------------

# x = {"name":"Sun",
#      "sid":404404}

# print(x["name"],x["sid"])

# x = {"name":"Sun",
#      "sid":404404}

# x["score"] = 100

# x["name"] = "Tik"

# print(x)

#-----------------------------------------
# students = [
#     {"name":"Sun","sid":12345,"score":100},
#     {"name":"Tik","sid":54321,"score":10}
# ]

# # print(students[0]["name"])

# for student in students:
#     print(student["name"],student["score"])

# -----------------------------------------

students = [
    {"name": "Tome", "score": 100}
    {"name": "Top", "score": 91}
    {"name": "Toshi", "score": 85}
    {"name": "Toey", "score": 73}
    {"name": "Toway", "score": 64}
    {"name": "Touin", "score": 56}
    {"name": "Touch", "score": 42}
]

for student in students:
    if student["score"] == 100:
        student["score"] = "∞"
    elif student["score"] >= 90:
        student["score"] = "A"
    elif student["score"] >= 80:
        student["score"] = "B"
    else:
        student["score"] = "F"
    print(student)