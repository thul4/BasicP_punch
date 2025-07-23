# username = input("Username: ")
# password = input("Password: ")

# if username == "admin":
#     if password == "admin888":
#         print("you're admin")
#     else:
#         print("wrong")
# elif username == "user":
#     if password == "user404":
#         print("you're user")
#     else:
#         print("wrong")
# else:
#     print("not found")

#-----------------------------------------------------

# x = "ต๊ะแหน่ว"

# x += "เดอะมอลบางแค"

# print(x)

meme = input("text meme: ")
word = ""


if meme == "ต๊ะแหน่ว":
    word += "ต๊ะแหน่ว"
    a = input("เลือกสาขา")
    if a == "เดอะมอลบางแค":
        word += a
    else:
        word += "เดอะมอลบางกะปิ"


print(word)