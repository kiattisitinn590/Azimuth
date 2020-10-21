username = input("UESR: ")
password = input("password: ")
if username == "admin" and password == "248617935":
    print("เข้าสู่ระบบเรียบร้อย")
    print("---------------------------------------")
    print("รายการสินค้า")
    print("1.มาม่า")
    print("2.ไข่")
    print("3.ข้าวสาร")
    Selected = input(">>")
    if Selected =="ไข่":
        num = int(input("จำนวน :"))
        price = 3
        print(num * price)
    elif Selected =="มาม่า":
        num = int(input("จำนวน :"))
        price = 6
        print(num * price)
    elif Selected =="ข้าวสาร":
        num = int(input("จำนวน :"))
        price = 50
        print(num * price)
