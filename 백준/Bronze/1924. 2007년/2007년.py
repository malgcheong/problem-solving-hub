x, y = map(int,input().split())

# 1,3,5,7,8,10,12은 31일
# 4,6,9,11은 30일

thirtyOne = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]
twentyEight = [2]
days = 0

for month in range(x):
    if month in thirtyOne:
        days += 31
    elif month in thirty:
        days += 30
    elif month in twentyEight:
        days += 28
days += y

if days % 7 == 0:
    print('SUN')
if days % 7 == 1:
    print('MON')
elif days % 7 == 2:
    print('TUE')
elif days % 7 == 3:
    print('WED')
elif days % 7 == 4:
    print('THU')
elif days % 7 == 5:
    print('FRI')
elif days % 7 == 6:
    print('SAT')

