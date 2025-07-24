# def hello(name):
#     print("ค่าที่รับเข้ามาแสดงจาก function: ", name)

# name = input("ค่าที่รับ: ")
# hello(name)

# def sum(a,b):
#     result = a + b
#     return result

# num1 = int(input("กรอกเลข 1: "))
# num2 = int(input("กรอกเลข 2:"))

# result = sum(num1,num2)
# print(result)

# def add(num1,num2):
#     result = num1 + num2
#     return result

# def main():
#     num1 = int(input("กรอกเลขตัวที่ 1: "))
#     num2 = int(input("กรอกเลขตัวที่ 2: "))
#     result = add(num1,num2)
#     print("ผลลัพธ์การบวกคือ: ", result)
# main()

def add(num1,num2):
    result = num1 + num2
    return result

def minus(num1,num2):
    result = num1 - num2
    return result

def multi(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def is_even(num):
    if (num % 2) == 0:
        print("เป็นเลขคู่")


def main():
    num1 = int(input("กรอกเลขตัวที่ 1: "))
    num2 = int(input("กรอกเลขตัวที่ 2: "))
    print(" + - * / เลือกสักอัน ")
    print(" [1] + ")
    print(" [2] - ")
    print(" [3] * ")
    print(" [4] / ")
    operation = input("ชูสชูส: ")

    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ: ", result)
    elif (operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ: ", result)
    elif (operation == "3"):
        result = multi(num1,num2)
        print("ผลคูณคือ: ", result)
    elif (operation == "4"):
        result = divide(num1,num2)
        print("ผลหารคือ: ", result)
    print(is_even(result))
main()
