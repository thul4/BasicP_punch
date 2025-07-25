def show(pang,face):
    print("")


piz = [
        {'P': 'ตำซั่วหนานุ่ม', 'price': 'free'},
        {'P': 'ตำซั่วบางกรอบ', 'price': 'free'},
        {'P': 'ฮาวายเอี้ยนหนานุ่ม', 'price': 'free'},
        {'P': 'บางกรอบฮาวายเอี้ยน', 'price': 'free'},
    ]

open = True
while open:
    print("welcome to 'ร้านซิซพ่าซิกม่า")
    print("----วันนี้จะแดรกหรือไม่แดรก----")
    print("[1] แดรก")
    print("[2] ไม่")
    option = int(input(" "))
    if option == 1:
        print("[1] ชอบหนานุ่ม")
        print("[2] ชอบบางกรอบ")
        print("[3] ชอบเหมือนกัน")
        pang = int(input(" "))
        print("แป้งที่คุณเลือก",pang)
        if pang == 1 or 2:
            print("--------เลือกหน้าที่อยากอีส-------")
            print("[1] หน้าตำซั่ว")
            print("[2] หน้าพี่ติ๊ก")
            print("[3] หน้าฮาวายเอี้ยน")
            print("[4] หน้าร้ากอะ")
            face = int(input(" "))
            if face == 1:
                print(show(pang,face))
        elif pang == 3:
            print("เสียใจด้วย มีแฟนละจร้า")
    elif option == 2:
        print("อ๋า โชคดีละกั้น")
    break