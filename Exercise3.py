hours_work = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter hourly pay rate: "))

if hours_work > 40:
    print("The gross pay is: ", (40*pay_rate)+((pay_rate*1.5)*(hours_work-40)))
else:
    print("The gross pay is: ", hours_work*pay_rate)