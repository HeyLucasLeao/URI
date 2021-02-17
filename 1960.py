import functools as fn

result = []
roman = {1000: "M", 500: "D", 100: "C",
         50: "L", 10: "X", 5: "V", 1: "I"
         }
number = int(input())
while number > 0:
    if roman.get(number):
        result.extend(roman[number])
        number -= number
    elif int(number / 1000) > 0:
        result.extend(roman[1000])
        number -= 1000
    elif int(number / 900) > 0:
        result.extend((roman[100], roman[1000]))
        number -= 900
    elif int(number / 500) > 0:
        result.extend(roman[500])
        number -= 500
    elif int(number / 400) > 0:
        result.extend((roman[100], roman[500]))
        number -= 400
    elif 100 > number > 89:
        result.extend((roman[10], roman[100]))
        number -= 90
    elif int(number / 100) > 0:
        result.extend(roman[100])
        number -= 100
    elif int(number / 50) > 0:
        result.extend(roman[50])
        number -= 50
    elif int(number / 40) > 0:
        result.extend((roman[10],roman[50]))
        number -= 40
    elif int(number / 10) > 0:
        result.extend(roman[10])
        number -= 10
    elif 9 > number > 5:
        result.extend(roman[5])
        number -= 5
    elif 4 > number > 0:
        result.extend(roman[1])
        number -= 1
    elif (number + 1) % 5 == 0 and 10 > number > 0:
        result.extend((roman[1], roman[number + 1]))
        number -= number
print(fn.reduce(lambda x, y: x + y, result))
