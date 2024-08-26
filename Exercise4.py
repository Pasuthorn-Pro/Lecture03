print("Select Operation 1.(+) 2.(-) 3.(*) 4.(/) -")
Operation = int(input("Select"))#กำหนดค่าของ Operation

if Operation <= 4 and Operation > 0:#Operation ต้องน้อยกว่าเท่ากับ 4 และ มากกว่า 0 โปรแกรมถึงจะทำงาน
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if Operation == 1:#ถ้า Operation เป็น 1 ให้นำ num1 ไปบวกกับ num2
        print(f"{num1} + {num2} = {(num1)+(num2)}")
    elif Operation == 2:#ถ้า Operation เป็น 1 ให้นำ num1 ไปลบกับ num2
        print(f"{num1} - {num2} = {(num1)-(num2)}")
    elif Operation == 3:#ถ้า Operation เป็น 1 ให้นำ num1 ไปคูณกับ num2
        print(f"{num1} x {num2} = {(num1)*(num2)}")
    elif Operation == 4:#ถ้า Operation เป็น 1 ให้นำ num1 ไปหารกับ num2
        print(f"{num1} / {num2} = {(num1)/(num2)}")
else:#ถ้าหาก Operation มีค่าไม่ตรงตามเงื่อในไขให้แสดงโปรแกรมด้านล่าง
    print("Invalid operation selected")