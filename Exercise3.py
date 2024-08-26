hours_work = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter hourly pay rate: "))

if hours_work > 40:#ถ้าชั่วโมงการทำงานมากกว่า 40 ชั่วโมงต่อสัปดาห์ ให้เพิ่มค่าแรง
    print("The gross pay is: ", (40*pay_rate)+((pay_rate*1.5)*(hours_work-40)))
    #แนวคิดการหาค่าแรงคือ [(40 ชั่วโมง * เรทค่าแรง)+(เรทค่าแรง * 1.5)*(ชั่วโมงการทำงาน - 40 ชั่วโมง)]
else:
    print("The gross pay is: ", hours_work*pay_rate)
    #ถ้าหากชั่วโมงการทำงานน้อยกว่า 40 ชั่วโมงให้คิดตามเรทค่าแรงปกติ