x = float(input("กรอกระยะทาง "))

if x <= 50:
    print("เสียค่าส่ง 10 บาท")
elif x >= 51 and x < 100:
    print("้เสียค่าส่ง 15 บาท")
elif x >= 101 and x < 300:
    print("เสียค่าส่ง 25 บาท")
elif x >= 301 and x < 500:
    print("เสียค่าส่ง 35 บาท")
else:
    print("เสียค่าส่ง 45 บาท")