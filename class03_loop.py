# sum = 0
# n = 4

# for i in range(n):
#     sum += i+1

# print(sum)

# for i in range(10):
#     if(i % 2) == 0:
#         print("even num: ", i)

# for i in range(10):
#     print(i*i)

#---------------------------------------

# sud2 = int(input(""))

# for i in range(1, 13):
#     print(sud2, "*",i , "=", sud2*i)

#----------------------------------------

# i = 0
# while i < 5:
#     print("halo")
#     i += 1

# start = True
# while start:
#     print("เลือกข้อที่อยากทำ")
#     print("โจทย์ที่ [1]")
#     print("โจทย์ที่ [2]")
#     x = int(input("กรุณากรอกเลข: "))
#     if x == 1:
#         print("ทำโจทย์ที่ 1")
#     elif x == 2:
#         print("ทำโจทย์ที่ 2")
#     start = False

#------------------------------------------

monster = 100
weapon1 = 30
weapon2 = 60
weapon3 = 10

gamestart = True
while gamestart:
    print("อยากเป็นผู้กล้าหรือผู้แพ้")
    print("[1] เป็นผู้กล้าไร้เทียมทาม")
    print("[2] เป็น loser noob XD")
    point = int(input(" "))
    if point == 1:
        times = int(input("บอกเลยคั้บพี่อยากตีกี่ครั้ง "))
        for i in range(times):
            print("ในฐานะคนทำเกมและหน้าตาดี จะเสกอาวุธให้ 3 อย่าง")
            print("[1] มือถือที่ป็อปสยามใช้ live tiktok", weapon1, "damage")
            print("[2] spawn จารย์โอฬารมา attack", weapon2, "damage")
            print("[3] ไม้ tung tung tung", weapon3, "damage")
            print("---มอนเต้อพี่ติ๊ก:", monster, "HP")
        choose = int(input("โปรดเลือกอาวุธ for attack: "))
        if choose == 1:
            print("คุณเลือกป็อปสยาม ทำการโจทตี", weapon1, "damage")

    elif point == 2:
        print("GAMEOVER-โคตรกากเลยน้อง")
    break
