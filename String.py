string1 = "Mary"
string2 = "Mark"

if string1 == string2:  # ถ้า string1 เท่ากับ string2
    print(f'"{string1}" and "{string2}" are equal.')
else:  # ถ้า string1 ไม่เท่ากับ string2
    print(f'"{string1}" and "{string2}" are not equal.')

if string1 < string2:  # ถ้า string1 มาก่อน string2 ในลำดับตัวอักษร
    print(f'"{string1}" comes before "{string2}" in lexicographical order.')
elif string1 > string2:  # ถ้า string1 มาหลัง string2 ในลำดับตัวอักษร
    print(f'"{string1}" comes after "{string2}" in lexicographical order.')

if string1.lower() == string2.lower():  # ถ้า string1 เท่ากับ string2 เมื่อไม่สนใจตัวพิมพ์เล็ก/ใหญ่
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case is ignored.')